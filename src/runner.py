import os
from pathlib import Path
from typing import Any, Dict

import yaml
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process, LLM


BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_DIR = BASE_DIR / "config"
INPUT_FILE = BASE_DIR / "modules" / "antixa" / "data" / "input" / "demande_biologiste.md"
OUTPUT_DIR = BASE_DIR / "modules" / "antixa" / "outputs"


def load_yaml(path: Path) -> Dict[str, Any]:
    if not path.exists():
        raise FileNotFoundError(f"Fichier introuvable : {path}")

    with path.open("r", encoding="utf-8") as file:
        content = yaml.safe_load(file)

    if not isinstance(content, dict):
        raise ValueError(f"Le fichier YAML est vide ou invalide : {path}")

    return content


def load_input_text(path: Path) -> str:
    if not path.exists():
        raise FileNotFoundError(f"Fichier d'entrée introuvable : {path}")

    return path.read_text(encoding="utf-8")


def build_task_description(base_description: str, input_text: str) -> str:
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


def main() -> None:
    load_dotenv(BASE_DIR / ".env")

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise EnvironmentError(
            "OPENAI_API_KEY est absent. Crée un fichier .env à la racine du projet."
        )

    model_name = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    agents_config = load_yaml(CONFIG_DIR / "agents_step1.yaml")
    tasks_config = load_yaml(CONFIG_DIR / "tasks_step1.yaml")
    input_text = load_input_text(INPUT_FILE)

    llm = LLM(model=model_name)

    agent_config = agents_config["domain_understanding_analyst"]
    domain_agent = Agent(
        role=agent_config["role"],
        goal=agent_config["goal"],
        backstory=agent_config["backstory"],
        llm=llm,
        verbose=True,
        allow_delegation=False,
    )

    tasks = []
    for task_key, task_config in tasks_config.items():
        output_file = task_config.get("output_file")
        if not output_file:
            raise ValueError(f"La tâche {task_key} ne définit pas output_file.")

        task = Task(
            description=build_task_description(task_config["description"], input_text),
            expected_output=task_config["expected_output"],
            agent=domain_agent,
            output_file=str(BASE_DIR / output_file),
        )
        tasks.append(task)

    crew = Crew(
        agents=[domain_agent],
        tasks=tasks,
        process=Process.sequential,
        verbose=True,
    )

    result = crew.kickoff()

    print("\nExécution terminée.")
    print(f"Livrables générés dans : {OUTPUT_DIR}")
    print("\nRésultat global :")
    print(result)


if __name__ == "__main__":
    main()
