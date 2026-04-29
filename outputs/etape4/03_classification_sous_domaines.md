```markdown
# Classification des sous-domaines métier
**Gestion des demandes urgentes de dosage anti-Xa dans le SIL**
**Date** : [À compléter]
**Version** : 1.0
**Auteurs** : Analyste DDD
**Sources** : Livrables étape 1 et 2 (01_reformulation_du_besoin.md, 02_acteurs_du_domaine.md, 03_concepts_metier_initiaux.md, 04_contraintes_et_risques.md, 05_vision_globale_du_domaine.md, 01_cartographie_acteurs_responsabilites.md, 02_attentes_objectifs_acteurs.md, 03_decisions_informations_manipulees.md, 04_regles_metier.md, 05_priorites_exceptions_contraintes.md, 06_conflits_objectifs_arbitrages.md, 07_base_modelisation_comportementale.md)

---

## 1. Introduction
Ce document **classe les sous-domaines proposés** selon leur contribution à la **valeur métier** du domaine des **demandes urgentes de dosage anti-Xa**, en s’appuyant sur les enjeux, risques, différenciation, criticité et spécificité métier identifiés dans les étapes 1 et 2.

L’objectif est de :
- **Différencier clairement** les sous-domaines selon leur impact stratégique, opérationnel ou générique.
- **Justifier la classification** par des critères objectifs (valeur métier, criticité, différenciation, risques).
- **Identifier les arbitrages** à confirmer avec les experts métier.
- **Préparer l’étape suivante** de modélisation comportementale (étape 3) en identifiant les frontières potentielles entre sous-domaines.

---

## 2. Tableau de classification des sous-domaines

| **Sous-domaine** | **Classification** | **Justification métier** | **Niveau de criticité** | **Niveau de différenciation** | **Risques associés à une mauvaise modélisation** | **Incertitudes/arbitrages à confirmer** |
|------------------|--------------------|--------------------------|-------------------------|-------------------------------|--------------------------------------------------|------------------------------------------|
| **Gestion des prescriptions et priorisation** | **Cœur stratégique** | - **Valeur métier centrale** : Garantit la pertinence clinique des demandes et la priorisation automatique, évitant les prescriptions inappropriées et les retards critiques. <br> - **Différenciation concurrentielle** : Automatisation de la priorisation et intégration des protocoles CAI. <br> - **Criticité élevée** : Un dysfonctionnement entraîne des erreurs de prescription, des retards critiques et des risques cliniques majeurs (hémorragies, thromboses). <br> - **Enjeux réglementaires** : Respect des protocoles HAS/ANSM et traçabilité des prescriptions. | **Critique** (niveau 1) | **Élevé** (niveau 3) | - Prescriptions inappropriées → erreurs thérapeutiques. <br> - Retards dans les cas urgents → complications graves. <br> - Non-respect des protocoles → sanctions réglementaires. <br> - Traçabilité insuffisante → impossibilité de prouver la conformité en cas d’audit. | - **Automatisation de la priorisation** : Le SIL doit-il classer automatiquement les demandes, ou cette tâche reste-t-elle manuelle ? <br> - **Critères exacts de rejet** : Quels sont les seuils pour rejeter une demande ? <br> - **Rôle de la CAI** : La CAI valide-t-elle les protocoles, ou participe-t-elle aussi à la validation des demandes ? |
| **Gestion pré-analytique et logistique des échantillons** | **Support** | - **Valeur métier** : Garantit la validité des échantillons avant analyse, évitant les résultats invalides et les rejets. <br> - **Différenciation** : Automatisation de la vérification des conformités et intégration avec le SIL. <br> - **Criticité élevée** : Un dysfonctionnement entraîne des résultats invalides, des rejets d’échantillons et des retards critiques. <br> - **Enjeux réglementaires** : Respect des normes ISO 15189 et des bonnes pratiques pré-analytiques. | **Critique** (niveau 1) | **Moyen** (niveau 2) | - Résultats invalides → erreurs d’interprétation. <br> - Rejets d’échantillons → retards dans la prise en charge. <br> - Non-conformité des tubes → dégradation des échantillons. <br> - Traçabilité insuffisante des non-conformités → impossibilité de prouver la conformité. | - **Critères exacts de conformité** : Quel est le type de tube exact requis ? Quel est le volume minimal ? Quel est le délai maximal entre prélèvement et analyse ? <br> - **Rôle du clinicien dans la vérification des tubes** : Le clinicien vérifie-t-il la conformité avant envoi, ou cette tâche est-elle entièrement déléguée au laboratoire ? <br> - **Procédure de gestion des non-conformités en astreinte** : Qui gère les non-conformités la nuit ou le week-end ? |
| **Réalisation analytique et saisie des résultats** | **Support** | - **Valeur métier** : Garantit la précision et la rapidité des analyses, ainsi que la transmission sans erreur des résultats. <br> - **Différenciation** : Intégration automatique entre analyseurs et SIL pour éviter les erreurs de saisie. <br> - **Criticité élevée** : Un dysfonctionnement entraîne des erreurs de saisie, des résultats erronés et des erreurs d’interprétation. <br> - **Enjeux réglementaires** : Respect des normes ISO 15189 et des procédures analytiques. | **Critique** (niveau 1) | **Moyen** (niveau 2) | - Erreurs de saisie → résultats erronés → erreurs d’interprétation. <br> - Absence d’int