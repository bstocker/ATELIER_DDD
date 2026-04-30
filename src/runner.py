import argparse
import os
import shutil
import sys
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
LIVRABLES_DIR = BASE_DIR / "livrables"
STEP1_OUTPUT_DIR = OUTPUT_DIR / "etape1"
STEP2_OUTPUT_DIR = OUTPUT_DIR / "etape2"
STEP3_OUTPUT_DIR = OUTPUT_DIR / "etape3"
STEP4_OUTPUT_DIR = OUTPUT_DIR / "etape4"
STEP5_OUTPUT_DIR = OUTPUT_DIR / "etape5"
STEP6_OUTPUT_DIR = OUTPUT_DIR / "etape6"
STEP1_LIVRABLES_DIR = LIVRABLES_DIR / "etape1"
STEP2_LIVRABLES_DIR = LIVRABLES_DIR / "etape2"
STEP3_LIVRABLES_DIR = LIVRABLES_DIR / "etape3"
STEP4_LIVRABLES_DIR = LIVRABLES_DIR / "etape4"
STEP5_LIVRABLES_DIR = LIVRABLES_DIR / "etape5"
STEP6_LIVRABLES_DIR = LIVRABLES_DIR / "etape6"

ALLOWED_INPUT_EXTENSIONS = {".md", ".txt", ".log", ".csv"}

STEP_CONFIGS: Dict[str, Dict[str, Any]] = {
    "1": {
        "label": "Étape 1",
        "agent_key": "domain_understanding_analyst",
        "agents_file": CONFIG_DIR / "agents_step1.yaml",
        "tasks_file": CONFIG_DIR / "tasks_step1.yaml",
        "input_dir": INPUT_DIR,
        "output_dir": STEP1_OUTPUT_DIR,
        "post_run_copies": [
            {
                "source": STEP1_OUTPUT_DIR / "05_vision_globale_du_domaine.md",
                "destination": STEP1_LIVRABLES_DIR / "Vision_Globale_etape1.md",
            }
        ],
        "instructions": [
            "Rester strictement dans l'étape 1 : compréhension du domaine métier.",
            "Ne pas produire de modèle DDD détaillé.",
            "Ne pas produire de schéma d'architecture technique.",
            "Ne pas inventer d'information clinique absente du corpus.",
            "Distinguer explicitement les faits, les hypothèses et les points à clarifier.",
            "Identifier les éventuelles contradictions entre les sources.",
            "Citer les sources utilisées quand c'est utile.",
            "Produire une réponse en français, structurée en Markdown.",
        ],
    },
    "2": {
        "label": "Étape 2",
        "agent_key": "actor_rules_analyst",
        "agents_file": CONFIG_DIR / "agents_step2.yaml",
        "tasks_file": CONFIG_DIR / "tasks_step2.yaml",
        "input_dir": STEP1_OUTPUT_DIR,
        "output_dir": STEP2_OUTPUT_DIR,
        "post_run_copies": [
            {
                "source": STEP2_OUTPUT_DIR / "07_base_modelisation_comportementale.md",
                "destination": STEP2_LIVRABLES_DIR / "Référentiel_Metier_etape2.md",
            }
        ],
        "instructions": [
            "Rester strictement dans l'étape 2 : structuration des acteurs, responsabilités, décisions, informations et règles métier.",
            "Utiliser les livrables de l'étape 1 comme corpus d'entrée principal.",
            "Ne pas produire de modèle DDD détaillé, d'agrégats, de bounded contexts ou d'architecture technique.",
            "Ne pas inventer d'information clinique absente du corpus.",
            "Distinguer explicitement les faits, les hypothèses et les points à clarifier.",
            "Signaler les règles métier implicites comme hypothèses à confirmer.",
            "Identifier les éventuelles contradictions entre les sources.",
            "Produire une réponse en français, structurée en Markdown.",
        ],
    },
    "3": {
        "label": "Étape 3",
        "agent_key": "ubiquitous_language_analyst",
        "agents_file": CONFIG_DIR / "agents_step3.yaml",
        "tasks_file": CONFIG_DIR / "tasks_step3.yaml",
        "input_dirs": [STEP1_OUTPUT_DIR, STEP2_OUTPUT_DIR],
        "output_dir": STEP3_OUTPUT_DIR,
        "post_run_copies": [
            {
                "source": STEP2_OUTPUT_DIR / "08_glossaire_metier.md",
                "destination": STEP3_LIVRABLES_DIR / "08_glossaire_metier.md",
            }
        ],
        "instructions": [
            "Rester strictement dans l'étape 3 : établissement d'un langage commun partagé.",
            "Utiliser les livrables des étapes 1 et 2 comme corpus d'entrée principal.",
            "Stabiliser le vocabulaire métier sans concevoir encore d'agrégats, de bounded contexts ou d'architecture technique.",
            "Définir chaque concept avec un nom clair, unique et cohérent.",
            "Repérer les synonymes, ambiguïtés, termes concurrents et divergences d'interprétation.",
            "Distinguer explicitement les termes validés, les hypothèses terminologiques et les termes à clarifier.",
            "Produire des formulations réutilisables dans les ateliers, la documentation, les user stories, les tests et le code.",
            "Ne pas inventer d'information clinique absente du corpus.",
            "Produire une réponse en français, structurée en Markdown.",
        ],
    },
    "4": {
        "label": "Étape 4",
        "agent_key": "subdomain_decomposition_analyst",
        "agents_file": CONFIG_DIR / "agents_step4.yaml",
        "tasks_file": CONFIG_DIR / "tasks_step4.yaml",
        "input_dirs": [STEP1_OUTPUT_DIR, STEP2_OUTPUT_DIR],
        "output_dir": STEP4_OUTPUT_DIR,
        "post_run_copies": [
            {
                "source": STEP4_OUTPUT_DIR / "06_synthese_decoupage_sous_domaines.md",
                "destination": STEP4_LIVRABLES_DIR / "Cartographie_etape4.md",
            }
        ],
        "instructions": [
            "Rester strictement dans l'étape 4 : découpage du domaine global en sous-domaines cohérents.",
            "Utiliser les livrables des étapes 1 et 2 comme corpus d'entrée principal.",
            "Identifier les zones fonctionnelles, leurs finalités propres, leurs règles spécifiques et leurs interactions.",
            "Distinguer explicitement les sous-domaines de coeur stratégique, de support et génériques.",
            "Ne pas concevoir encore de bounded contexts définitifs, d'agrégats, de cas d'usage détaillés ou d'architecture technique.",
            "Ne pas inventer d'information clinique absente du corpus.",
            "Distinguer explicitement les faits, les hypothèses et les points à clarifier.",
            "Signaler les découpages incertains ou alternatifs comme hypothèses à valider avec les experts métier.",
            "Produire une réponse en français, structurée en Markdown.",
        ],
    },
    "5": {
        "label": "Étape 5",
        "agent_key": "bounded_contexts_analyst",
        "agents_file": CONFIG_DIR / "agents_step5.yaml",
        "tasks_file": CONFIG_DIR / "tasks_step5.yaml",
        "input_dirs": [STEP1_OUTPUT_DIR, STEP2_OUTPUT_DIR, STEP4_OUTPUT_DIR],
        "output_dir": STEP5_OUTPUT_DIR,
        "post_run_copies": [
            {
                "source": STEP5_OUTPUT_DIR / "06_cartographie_bounded_contexts.md",
                "destination": STEP5_LIVRABLES_DIR / "Cartographie_Bounded_Contexts_etape5.md",
            }
        ],
        "instructions": [
            "Rester strictement dans l'étape 5 : délimitation des Bounded Contexts.",
            "Utiliser les livrables des étapes 1, 2 et 4 comme corpus d'entrée principal.",
            "Transformer le découpage en sous-domaines en frontières explicites de responsabilité.",
            "Identifier les espaces où le vocabulaire, les règles et les modèles gardent un sens stable et non ambigu.",
            "Clarifier les dépendances, contrats d'échange et risques de couplage entre contextes.",
            "Ne pas concevoir encore l'architecture technique détaillée, les agrégats définitifs ou l'implémentation applicative.",
            "Ne pas inventer d'information clinique absente du corpus.",
            "Distinguer explicitement les faits, les hypothèses et les points à clarifier.",
            "Produire une réponse en français, structurée en Markdown.",
        ],
    },
    "6": {
        "label": "Étape 6",
        "agent_key": "domain_model_architect",
        "agents_file": CONFIG_DIR / "agents_step6.yaml",
        "tasks_file": CONFIG_DIR / "tasks_step6.yaml",
        "input_dirs": [STEP5_OUTPUT_DIR],
        "output_dir": STEP6_OUTPUT_DIR,
        "post_run_copies": [
            {
                "source": STEP6_OUTPUT_DIR / "06_diagramme_classes_uml.md",
                "destination": STEP6_LIVRABLES_DIR / "Modele_Metier_UML_etape6.md",
            }
        ],
        "instructions": [
            "Rester strictement dans l'étape 6 : modélisation du domaine métier au sein des Bounded Contexts.",
            "Utiliser les livrables de l'étape 5 comme corpus d'entrée principal.",
            "Se concentrer en priorité sur les Bounded Contexts relevant du coeur stratégique.",
            "Distinguer rigoureusement agrégats, entités et objets valeur selon leurs propriétés DDD.",
            "Formaliser les invariants et règles métier directement associés à leur agrégat responsable.",
            "Ne pas concevoir l'architecture technique, les bases de données, les APIs ou l'infrastructure.",
            "Ne pas inventer d'information clinique absente du corpus.",
            "Distinguer explicitement les faits, les hypothèses et les points à clarifier.",
            "Nommer les événements de domaine au passé et les commandes à l'impératif.",
            "Produire le diagramme UML final en syntaxe classDiagram Mermaid, sans texte avant ni après le bloc.",
            "Produire une réponse en français, structurée en Markdown.",
        ],
    },
}


def load_yaml(path: Path) -> Dict[str, Any]:
    if not path.exists():
        raise FileNotFoundError(f"Fichier YAML introuvable : {path}")

    with path.open("r", encoding="utf-8") as file:
        content = yaml.safe_load(file)

    if not isinstance(content, dict):
        raise ValueError(f"Le fichier YAML est vide ou invalide : {path}")

    return content


def build_missing_input_hint(input_dir: Path) -> str:
    if input_dir == STEP1_OUTPUT_DIR:
        return "Exécute d'abord l'étape 1 : python src/runner.py --step 1"

    if input_dir == STEP2_OUTPUT_DIR:
        return "Exécute d'abord l'étape 2 : python src/runner.py --step 2"

    if input_dir == STEP4_OUTPUT_DIR:
        return "Exécute d'abord l'étape 4 : python src/runner.py --step 4"

    if input_dir == STEP5_OUTPUT_DIR:
        return "Exécute d'abord l'étape 5 : python src/runner.py --step 5"

    return f"Dépose au moins un fichier exploitable dans {input_dir.relative_to(BASE_DIR)}."


def load_inputs_from_directory(input_dir: Path) -> str:
    """
    Lit tous les fichiers texte exploitables du dossier data/input/
    et les concatène dans un corpus unique.
    """
    if not input_dir.exists():
        raise FileNotFoundError(f"Dossier d'entrée introuvable : {input_dir}")

    files = sorted(
        file
        for file in input_dir.iterdir()
        if file.is_file() and file.suffix.lower() in ALLOWED_INPUT_EXTENSIONS
    )

    if not files:
        raise ValueError(
            f"Aucun fichier exploitable trouvé dans {input_dir}. "
            f"Extensions acceptées : {', '.join(sorted(ALLOWED_INPUT_EXTENSIONS))}. "
            f"{build_missing_input_hint(input_dir)}"
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
        raise ValueError(
            f"Les fichiers trouvés dans {input_dir} sont vides. "
            f"{build_missing_input_hint(input_dir)}"
        )

    return "\n\n".join(blocks)


def load_inputs_from_directories(input_dirs: List[Path]) -> str:
    corpus_blocks: List[str] = []

    for input_dir in input_dirs:
        corpus_blocks.append(load_inputs_from_directory(input_dir))

    return "\n\n".join(corpus_blocks)


def build_task_description(
    base_description: str,
    input_text: str,
    instructions: List[str],
) -> str:
    formatted_instructions = "\n".join(
        f"- {instruction}" for instruction in instructions
    )

    return f"""
{base_description}

---
CORPUS MÉTIER À ANALYSER
---
{input_text}

---
CONSIGNES GÉNÉRALES
---
{formatted_instructions}
""".strip()


def ensure_project_structure() -> None:
    INPUT_DIR.mkdir(parents=True, exist_ok=True)
    STEP1_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    STEP2_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    STEP3_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    STEP4_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    STEP5_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    STEP6_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    STEP1_LIVRABLES_DIR.mkdir(parents=True, exist_ok=True)
    STEP2_LIVRABLES_DIR.mkdir(parents=True, exist_ok=True)
    STEP3_LIVRABLES_DIR.mkdir(parents=True, exist_ok=True)
    STEP4_LIVRABLES_DIR.mkdir(parents=True, exist_ok=True)
    STEP5_LIVRABLES_DIR.mkdir(parents=True, exist_ok=True)
    STEP6_LIVRABLES_DIR.mkdir(parents=True, exist_ok=True)


def run_post_run_copies(step_config: Dict[str, Any]) -> List[Path]:
    copied_files: List[Path] = []

    for copy_config in step_config.get("post_run_copies", []):
        source = copy_config["source"]
        destination = copy_config["destination"]

        if not source.exists():
            raise FileNotFoundError(
                f"Impossible de copier le livrable : fichier source introuvable : {source}"
            )

        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, destination)
        copied_files.append(destination)

    return copied_files


def resolve_step_output_path(output_file: str, task_key: str, output_dir: Path) -> Path:
    output_path = Path(output_file)
    relative_output_dir = output_dir.relative_to(BASE_DIR)

    if output_path.is_absolute():
        raise ValueError(
            f"La tâche {task_key} utilise un chemin absolu interdit : {output_file}. "
            f"Utilise un chemin relatif du type {relative_output_dir}/nom_du_fichier.md"
        )

    if not output_path.parts:
        raise ValueError(f"La tâche {task_key} utilise un chemin de sortie vide.")

    relative_output_parts = relative_output_dir.parts

    if output_path.parts[: len(relative_output_parts)] == relative_output_parts:
        return output_path

    if output_path.parts[0] == "outputs":
        if len(output_path.parts) == 1:
            raise ValueError(
                f"La tâche {task_key} doit préciser un nom de fichier de sortie."
            )

        return output_path

    return relative_output_dir / output_path


def build_agent(agents_config: Dict[str, Any], llm: LLM, agent_key: str) -> Agent:
    if agent_key not in agents_config:
        raise KeyError(f"Agent absent dans le fichier de configuration : {agent_key}")

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
    output_dir: Path,
    instructions: List[str],
) -> List[Task]:
    tasks: List[Task] = []

    for task_key, task_config in tasks_config.items():
        required_fields = ["description", "expected_output", "output_file"]

        for field in required_fields:
            if field not in task_config:
                raise KeyError(f"Champ manquant dans la tâche {task_key} : {field}")

        output_file = task_config["output_file"]
        output_path = resolve_step_output_path(output_file, task_key, output_dir)

        absolute_output_parent = BASE_DIR / output_path.parent
        absolute_output_parent.mkdir(parents=True, exist_ok=True)

        task = Task(
            description=build_task_description(
                task_config["description"],
                input_text,
                instructions,
            ),
            expected_output=task_config["expected_output"],
            agent=domain_agent,
            output_file=str(output_path),
        )

        tasks.append(task)

    if not tasks:
        raise ValueError("Aucune tâche définie dans le fichier de configuration")

    return tasks


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Exécute une étape de l'atelier DDD avec les agents CrewAI."
    )
    parser.add_argument(
        "--step",
        "-s",
        choices=sorted(STEP_CONFIGS.keys()),
        default="1",
        help="Étape DDD à exécuter. Valeur par défaut : 1.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    step_config = STEP_CONFIGS[args.step]

    os.chdir(BASE_DIR)

    load_dotenv(BASE_DIR / ".env")

    api_key = os.getenv("MISTRAL_API_KEY")
    if not api_key:
        raise EnvironmentError(
            "MISTRAL_API_KEY est absent. Crée un fichier .env à la racine du projet."
        )

    model_name = os.getenv("MISTRAL_MODEL", "mistral/mistral-small-latest")

    ensure_project_structure()

    agents_config = load_yaml(step_config["agents_file"])
    tasks_config = load_yaml(step_config["tasks_file"])

    if "input_dirs" in step_config:
        input_text = load_inputs_from_directories(step_config["input_dirs"])
    else:
        input_text = load_inputs_from_directory(step_config["input_dir"])

    llm = LLM(model=model_name)

    domain_agent = build_agent(agents_config, llm, step_config["agent_key"])
    tasks = build_tasks(
        tasks_config,
        domain_agent,
        input_text,
        step_config["output_dir"],
        step_config["instructions"],
    )

    crew = Crew(
        agents=[domain_agent],
        tasks=tasks,
        process=Process.sequential,
        verbose=True,
    )

    result = crew.kickoff()
    copied_files = run_post_run_copies(step_config)

    print("\nExécution terminée.")
    print(f"Étape exécutée : {step_config['label']}")
    if "input_dirs" in step_config:
        analyzed_sources = ", ".join(
            str(input_dir.relative_to(BASE_DIR))
            for input_dir in step_config["input_dirs"]
        )
    else:
        analyzed_sources = str(step_config["input_dir"].relative_to(BASE_DIR))

    print(f"Sources analysées depuis : {analyzed_sources}")
    print(f"Livrables générés dans : {step_config['output_dir'].relative_to(BASE_DIR)}")

    print("\nFichiers de sortie attendus :")
    for task_key, task_config in tasks_config.items():
        output_file = resolve_step_output_path(
            task_config["output_file"],
            task_key,
            step_config["output_dir"],
        )
        print(f"- {output_file}")

    if copied_files:
        print("\nCopies de livrables générées :")
        for copied_file in copied_files:
            print(f"- {copied_file.relative_to(BASE_DIR)}")

    print("\nRésultat global :")
    print(result)


if __name__ == "__main__":
    try:
        main()
    except (EnvironmentError, FileNotFoundError, KeyError, ValueError) as error:
        print(f"\nErreur : {error}", file=sys.stderr)
        sys.exit(1)
