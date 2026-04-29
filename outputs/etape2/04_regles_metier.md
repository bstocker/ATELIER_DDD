```markdown
# Règles métier
**Domaine métier** : Gestion des demandes urgentes de dosage anti-Xa dans le SIL
**Date** : [À compléter]
**Version** : 1.0
**Auteurs** : Analyste Métier
**Sources** : Livrables étape 1 (01_reformulation_du_besoin.md, 02_acteurs_du_domaine.md, 03_concepts_metier_initiaux.md, 04_contraintes_et_risques.md, 05_vision_globale_du_domaine.md)

---

## 1. Introduction
Ce document formalise les **règles métier** qui encadrent le fonctionnement du domaine des **demandes urgentes de dosage anti-Xa**, en distinguant :
- Les **règles explicites** présentes dans les livrables de l’étape 1.
- Les **règles implicites ou probables** déduites du contexte métier.
- Les **conditions d’application** de chaque règle.
- Les **acteurs concernés** par chaque règle.
- Les **conséquences en cas de non-respect**.
- Les **règles à valider** avec les experts métier.

Ces règles couvrent :
- La **validation des demandes**
- La **priorisation des analyses**
- Les **exigences pré-analytiques**
- L’**interprétation des résultats**
- La **traçabilité et la sécurité**
- Les **droits d’accès**
- Les **enchaînements obligatoires**
- Les **contraintes réglementaires**

---

## 2. Règles métier explicites

### 2.1. Règles de prescription et validation des demandes

| **ID** | **Règle métier** | **Description** | **Acteurs concernés** | **Conditions d'application** | **Conséquences en cas de non-respect** | **Source** |
|--------|------------------|-----------------|-----------------------|-----------------------------|----------------------------------------|------------|
| **RME-01** | **Prescription électronique obligatoire** | Toute demande de dosage anti-Xa doit être formalisée via une prescription électronique dans le SIL. | Cliniciens prescripteurs, SIL | - Patient sous AOD <br> - Contexte clinique justifiant le dosage (ex. : hémorragie active, chirurgie en urgence) | - Risque de perte de traçabilité <br> - Erreur de transcription <br> - Non-respect des protocoles locaux | 02_acteurs_du_domaine.md, 03_concepts_metier_initiaux.md |
| **RME-02** | **Respect des protocoles locaux** | La prescription doit respecter les indications définies par les protocoles de la Commission des Anti-infectieux et des Anticoagulants (CAI). | Cliniciens prescripteurs, CAI | - Protocoles locaux en vigueur <br> - Recommandations HAS/ANSM | - Prescription inappropriée → risque clinique <br> - Non-conformité réglementaire | 02_acteurs_du_domaine.md |
| **RME-03** | **Validation biologique des demandes** | Toute demande de dosage anti-Xa doit être validée par un biologiste avant analyse. | Biologistes médicaux | - Demande reçue dans le SIL <br> - Données contextuelles complètes | - Analyse non pertinente → résultat inutilisable <br> - Retard dans la prise en charge | 02_acteurs_du_domaine.md |
| **RME-04** | **Rejet des demandes non conformes** | Les demandes ne respectant pas les protocoles ou les critères cliniques doivent être rejetées avec justification. | Biologistes médicaux | - Demande ne respectant pas les indications <br> - Données manquantes ou incohérentes | - Perte de temps pour le laboratoire <br> - Risque de surcharge inutile | 02_acteurs_du