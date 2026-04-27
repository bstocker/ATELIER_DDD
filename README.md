# DDD Anti-Xa — Étape 1 : Comprendre le domaine métier

Ce projet est un prototype CrewAI destiné à produire les livrables de l'étape 1 d'une démarche DDD : **comprendre le domaine métier**.

Le cas étudié concerne l'évolution d'un SIL pour améliorer la gestion des demandes urgentes de dosage anti-Xa chez les patients sous anticoagulants oraux directs.

## Objectif de l'étape 1

Produire une connaissance globale du domaine, sans encore concevoir le modèle DDD détaillé, les bounded contexts, les agrégats ou l'architecture technique.

## Livrables produits

Le runner génère les fichiers suivants dans le dossier `outputs/` :

```text
01_reformulation_du_besoin.md
02_acteurs_du_domaine.md
03_concepts_metier_initiaux.md
04_contraintes_et_risques.md
05_vision_globale_du_domaine.md
```

Le livrable principal est :

```text
05_vision_globale_du_domaine.md
```

## Arborescence

```text
ddd_antixa_step1/
├── README.md
├── requirements.txt
├── .env.example
├── config/
│   ├── agents.yaml
│   └── tasks.yaml
├── data/
│   └── input/
│       └── demande_biologiste.md
├── outputs/
└── src/
    ├── runner.py
    └── loaders.py
```

## Installation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Puis renseigner la clé API dans `.env`.

## Exécution

```bash
python src/runner.py
```

## Remarque

Ce projet traite uniquement l'étape 1 de la méthode DDD. Les étapes suivantes — règles métier, langage commun, sous-domaines, bounded contexts, agrégats, événements métier, cas d'usage et architecture — ne sont pas incluses volontairement.
