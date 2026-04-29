# ATELIER DDD - Processus général de la démarche DDD  
<img width="1024" height="1536" alt="Processus_DDD" src="https://github.com/user-attachments/assets/e24f9027-e444-457a-98d5-9742973f1da3" />

# Étape 1 : Comprendre le domaine métier

Ce projet est un prototype de programmation d'Agents IA destiné à produire les livrables de l'étape 1 d'une démarche DDD : **comprendre le domaine métier**.

Le cas étudié concerne l'évolution d'un SIL pour améliorer la gestion des demandes urgentes de dosage anti-Xa chez les patients sous anticoagulants oraux directs.

## Objectif de l'étape 1

Produire une connaissance globale du domaine, sans encore concevoir le modèle DDD détaillé, les bounded contexts, les agrégats ou l'architecture technique.

## Les inputs

Les inputs (demandes utilisateurs) sont à déposer dans le répertoire data/input. Dans cet exemple, vous trouverez dans le répertoire inputs la demande d'évolution d'un SI émise par un biologiste.    
  
## Livrables produits

Le runner des Agents AI génère les fichiers suivants dans le dossier `outputs/etape1/` :

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

## Installation
## 1) Lancer le projet dans Codespaces
- Faite un Fork de ce Repository Github (bouton Fork en haut à gauche)
- Créez, dans votre Repository, le Secret Codespaces suivant :
  **OPENAI_API_KEY** qui contiendra l'API Key de votre ChatGPT   
- Cliquez ensuite sur le bouton **[Code]** → **Create codespace on main**
- Dernière étape, dans le Terminal de votre Codespace, exécutez les commandes suivantes :  
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 2) Exécution

```bash
python src/runner.py --step 1
```

L'étape 2 utilise les livrables de `outputs/etape1/` comme inputs et dépose ses
livrables dans `outputs/etape2/` :

```bash
python src/runner.py --step 2
```

## Remarque

Ce projet traite les premières étapes de la méthode DDD. Il ne produit pas encore
de modèle DDD détaillé, de bounded contexts, d'agrégats, d'événements métier
détaillés, de cas d'usage applicatifs ou d'architecture technique.
