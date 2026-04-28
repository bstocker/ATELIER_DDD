import os
from pathlib import Path
from typing import Any, Dict, List

import yaml
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process, LLM


# Racine du projet : /workspaces/ATELIER_DDD
BASE_DIR = Path(__file__).resolve().parent.parent

CONFIG_DIR = BASE_DIR / "config"
DATA_DIR = BASE_DIR / "data"
INPUT_FILE = DATA_DIR / "input" / "demande_biologiste.md"

# Dossier de sortie relatif au projet
OUTPUT_DIR = BASE_DIR / "outputs"


def load_yaml(path: Path) -> Dict[str, Any]:
    """Charge un fichier YAML et vérifie qu'il contient un dictionnaire."""
    if not path.exists():
        raise FileNotFoundError(f"Fichier YAML introuvable : {path}")

    with path.open("r", encoding="utf-8") as file:
        content = yaml.safe_load(file)

    if not isinstance(content, dict):
        raise ValueError(f"Le fichier YAML est vide ou invalide : {path}")

    return content


def load_input_text(path: Path) -> str:
    """Charge le fichier de demande métier."""
    if not path.exists():
        raise FileNotFoundError(f"Fichier d'entrée introuvable : {path}")

    content = path.read_text(encoding="utf-8").strip()

    if not content:
        raise ValueError(f"Le fichier d'entrée est vide : {path}")

    return content


def build_task_description(base_description: str, input_text: str) -> str:
    """Construit la consigne complète transmise à l'agent."""
    return f"""
{base_description}

---
DEMANDE MÉTIER À ANALYSER
---
{input_text}

---
CONSIGNES GÉNÉRALES
---
- Rester strictement dans l'étape 1 : compréhension du domaine métier.
- Ne pas produire de modèle DDD détaillé.
- Ne pas produire de schéma d'architecture technique.
- Ne pas inventer d'information clinique absente de la demande.
- Signaler explicitement les hypothèses et les points à clarifier.
- Produire une réponse en français, structurée en Markdown.
""".strip()


def ensure_project_structure() -> None:
    """Crée les répertoires nécessaires s'ils n'existent pas."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def build_agent(agents_config: Dict[str, Any], llm: LLM) -> Agent:
    """Construit l'agent principal d'analyse du domaine."""
    agent_key = "domain_understanding_analyst"

    if agent_key not in agents_config:
        raise KeyError(f"Agent absent dans agents_step1.yaml : {agent_key}")

    agent_config = agents_config[agent_key]

    required_fields = ["role", "goal", "backstory"]
    for field in required_fields:
        if field not in agent_config:
            raise KeyError(f"Champ manquant pour l'agent {agent_key} : {field}")

    return Agent(
        role=agent_config["role"],
        goal=agent_config["goal"],
        backstory=agent_config["backstory"],
        llm=llm,
        verbose=True,
        allow_delegation=False,
    )


def build_tasks(
    tasks_config: Dict[str, Any],
    domain_agent: Agent,
    input_text: str,
) -> List[Task]:
    """Construit les tâches CrewAI avec des chemins de sortie relatifs."""
    tasks: List[Task] = []

    for task_key, task_config in tasks_config.items():
        required_fields = ["description", "expected_output", "output_file"]

        for field in required_fields:
            if field not in task_config:
                raise KeyError(f"Champ manquant dans la tâche {task_key} : {field}")

        output_file = task_config["output_file"]

        # Sécurité : on force les sorties dans outputs/
        output_path = Path(output_file)

        if output_path.is_absolute():
            raise ValueError(
                f"La tâche {task_key} utilise un chemin absolu interdit : {output_file}. "
                "Utilise plutôt un chemin relatif du type outputs/nom_du_fichier.md"
            )

        if output_path.parts[0] != "outputs":
            output_path = Path("outputs") / output_path

        # Création du dossier parent depuis la racine projet
        absolute_output_parent = BASE_DIR / output_path.parent
        absolute_output_parent.mkdir(parents=True, exist_ok=True)

        task = Task(
            description=build_task_description(
                task_config["description"],
                input_text,
            ),
            expected_output=task_config["expected_output"],
            agent=domain_agent,

            # Important :
            # On transmet un chemin relatif à CrewAI pour éviter
            # l'affichage parasite /workspaces/ATELIER_DDD/outputs dans VSCode.
            output_file=str(output_path),
        )

        tasks.append(task)

    if not tasks:
        raise ValueError("Aucune tâche définie dans tasks_step1.yaml")

    return tasks


def main() -> None:
    """Point d'entrée principal."""
    os.chdir(BASE_DIR)

    load_dotenv(BASE_DIR / ".env")

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise EnvironmentError(
            "OPENAI_API_KEY est absent. Crée un fichier .env à la racine du projet."
        )

    model_name = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

    ensure_project_structure()

    agents_config = load_yaml(CONFIG_DIR / "agents_step1.yaml")
    tasks_config = load_yaml(CONFIG_DIR / "tasks_step1.yaml")
    input_text = load_input_text(INPUT_FILE)

    llm = LLM(model=model_name)

    domain_agent = build_agent(agents_config, llm)
    tasks = build_tasks(tasks_config, domain_agent, input_text)

    crew = Crew(
        agents=[domain_agent],
        tasks=tasks,
        process=Process.sequential,
        verbose=True,
    )

    result = crew.kickoff()

    print("\nExécution terminée.")
    print(f"Livrables générés dans : {OUTPUT_DIR.relative_to(BASE_DIR)}")
    print("\nFichiers attendus :")

    for task_config in tasks_config.values():
        output_file = Path(task_config["output_file"])

        if output_file.is_absolute():
            continue

        if output_file.parts[0] != "outputs":
            output_file = Path("outputs") / output_file

        print(f"- {output_file}")

    print("\nRésultat global :")
    print(result)


if __name__ == "__main__":
    main()
