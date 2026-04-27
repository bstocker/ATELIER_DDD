import os
from pathlib import Path

import yaml
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process, LLM

from loaders import read_text_file


BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_DIR = BASE_DIR / "config"
INPUT_FILE = BASE_DIR / "data" / "input" / "demande_biologiste.md"
OUTPUT_DIR = BASE_DIR / "outputs"


def load_yaml(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as file:
        return yaml.safe_load(file)


def build_agent(agent_config: dict, llm: LLM) -> Agent:
    return Agent(
        role=agent_config["role"],
        goal=agent_config["goal"],
        backstory=agent_config["backstory"],
        allow_delegation=agent_config.get("allow_delegation", False),
        verbose=agent_config.get("verbose", True),
        llm=llm,
    )


def build_task(task_config: dict, agent: Agent) -> Task:
    output_file = task_config.get("output_file")
    if output_file:
        output_file = str(BASE_DIR / output_file)

    return Task(
        description=task_config["description"],
        expected_output=task_config["expected_output"],
        agent=agent,
        output_file=output_file,
    )


def main() -> None:
    load_dotenv(BASE_DIR / ".env")
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    model_name = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
    llm = LLM(model=model_name)

    agents_config = load_yaml(CONFIG_DIR / "agents.yaml")
    tasks_config = load_yaml(CONFIG_DIR / "tasks.yaml")

    domain_request = read_text_file(INPUT_FILE)

    domain_agent = build_agent(
        agents_config["domain_understanding_analyst"],
        llm,
    )

    tasks = [
        build_task(tasks_config["analyser_demande_initiale"], domain_agent),
        build_task(tasks_config["identifier_acteurs_domaine"], domain_agent),
        build_task(tasks_config["identifier_concepts_metier"], domain_agent),
        build_task(tasks_config["identifier_contraintes_risques"], domain_agent),
        build_task(tasks_config["produire_vision_globale"], domain_agent),
    ]

    crew = Crew(
        agents=[domain_agent],
        tasks=tasks,
        process=Process.sequential,
        verbose=True,
    )

    result = crew.kickoff(inputs={"domain_request": domain_request})

    print("\n=== Analyse terminée ===")
    print(f"Livrables générés dans : {OUTPUT_DIR}")
    print(result)


if __name__ == "__main__":
    main()
