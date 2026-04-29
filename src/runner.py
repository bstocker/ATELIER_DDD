import os
from pathlib import Path
from typing import Any, Dict, List

import yaml
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process, LLM


BASE_DIR = Path(__file__).resolve().parent.parent

CONFIG_DIR = BASE_DIR / "config"
DATA_DIR = BASE_DIR / "data"
INPUT_DIR = DATA_DIR / "input"
OUTPUT_DIR = BASE_DIR / "outputs"
STEP1_OUTPUT_DIR = OUTPUT_DIR / "etape1"


def load_yaml(path: Path) -> Dict[str, Any]:
    if not path.exists():
        raise FileNotFoundError(f"Fichier YAML introuvable : {path}")

    with path.open("r", encoding="utf-8") as file:
        content = yaml.safe_load(file)

    if not isinstance(content, dict):
        raise ValueError(f"Le fichier YAML est vide ou invalide : {path}")

    return content


def load_inputs_from_directory(input_dir: Path) -> str:
    """
    Lit tous les fichiers texte exploitables du dossier data/input/
    et les concatène dans un corpus unique.
    """
    if not input_dir.exists():
        raise FileNotFoundError(f"Dossier d'entrée introuvable : {input_dir}")

    allowed_extensions = {".md", ".txt", ".log", ".csv"}

    files = sorted(
        file
        for file in input_dir.iterdir()
        if file.is_file() and file.suffix.lower() in allowed_extensions
    )

    if not files:
        raise ValueError(
            f"Aucun fichier exploitable trouvé dans {input_dir}. "
            f"Extensions acceptées : {', '.join(sorted(allowed_extensions))}"
        )

    blocks: List[str] = []

    for file in files:
        content = file.read_text(encoding="utf-8").strip()

        if not content:
            continue

        blocks.append(
            f"""
==============================
SOURCE : {file.name}
CHEMIN : {file.relative_to(BASE_DIR)}
==============================

{content}
""".strip()
        )

    if not blocks:
        raise ValueError(f"Les fichiers trouvés dans {input_dir} sont vides.")

    return "\n\n".join(blocks)


def build_task_description(base_description: str, input_text: str) -> str:
    return f"""
{base_description}

---
CORPUS MÉTIER À ANALYSER
---
{input_text}

---
CONSIGNES GÉNÉRALES
---
- Rester strictement dans l'étape 1 : compréhension du domaine métier.
- Ne pas produire de modèle DDD détaillé.
- Ne pas produire de schéma d'architecture technique.
- Ne pas inventer d'information clinique absente du corpus.
- Distinguer explicitement les faits, les hypothèses et les points à clarifier.
- Identifier les éventuelles contradictions entre les sources.
- Citer les sources utilisées quand c'est utile.
- Produire une réponse en français, structurée en Markdown.
""".strip()


def ensure_project_structure() -> None:
    INPUT_DIR.mkdir(parents=True, exist_ok=True)
    STEP1_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def resolve_step1_output_path(output_file: str, task_key: str) -> Path:
    output_path = Path(output_file)

    if output_path.is_absolute():
        raise ValueError(
            f"La tâche {task_key} utilise un chemin absolu interdit : {output_file}. "
            "Utilise un chemin relatif du type outputs/etape1/nom_du_fichier.md"
        )

    if not output_path.parts:
        raise ValueError(f"La tâche {task_key} utilise un chemin de sortie vide.")

    if output_path.parts[0] == "outputs":
        if len(output_path.parts) > 1 and output_path.parts[1] == "etape1":
            return output_path

        return Path("outputs") / "etape1" / Path(*output_path.parts[1:])

    return Path("outputs") / "etape1" / output_path


def build_agent(agents_config: Dict[str, Any], llm: LLM) -> Agent:
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
    tasks: List[Task] = []

    for task_key, task_config in tasks_config.items():
        required_fields = ["description", "expected_output", "output_file"]

        for field in required_fields:
            if field not in task_config:
                raise KeyError(f"Champ manquant dans la tâche {task_key} : {field}")

        output_file = task_config["output_file"]
        output_path = resolve_step1_output_path(output_file, task_key)

        absolute_output_parent = BASE_DIR / output_path.parent
        absolute_output_parent.mkdir(parents=True, exist_ok=True)

        task = Task(
            description=build_task_description(
                task_config["description"],
                input_text,
            ),
            expected_output=task_config["expected_output"],
            agent=domain_agent,
            output_file=str(output_path),
        )

        tasks.append(task)

    if not tasks:
        raise ValueError("Aucune tâche définie dans tasks_step1.yaml")

    return tasks


def main() -> None:
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

    input_text = load_inputs_from_directory(INPUT_DIR)

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
    print(f"Sources analysées depuis : {INPUT_DIR.relative_to(BASE_DIR)}")
    print(f"Livrables générés dans : {STEP1_OUTPUT_DIR.relative_to(BASE_DIR)}")

    print("\nFichiers de sortie attendus :")
    for task_key, task_config in tasks_config.items():
        output_file = resolve_step1_output_path(task_config["output_file"], task_key)
        print(f"- {output_file}")

    print("\nRésultat global :")
    print(result)


if __name__ == "__main__":
    main()
