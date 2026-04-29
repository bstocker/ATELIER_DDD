```markdown
# Décisions et informations manipulées
**Domaine métier** : Gestion des demandes urgentes de dosage anti-Xa dans le SIL
**Date** : [À compléter]
**Version** : 1.0
**Auteurs** : Analyste Métier
**Sources** : Livrables étape 1 (01_reformulation_du_besoin.md, 02_acteurs_du_domaine.md, 03_concepts_metier_initiaux.md, 04_contraintes_et_risques.md, 05_vision_globale_du_domaine.md)

---

## 1. Introduction
Ce document identifie et décrit :
- Les **décisions métier** prises dans le circuit des demandes urgentes de dosage anti-Xa.
- L’**acteur responsable** de chaque décision.
- Les **informations nécessaires** pour prendre la décision.
- Les **informations produites ou transformées** au cours du processus.
- Les **dépendances entre décisions**.
- Les **informations manquantes ou insuffisamment fiables**.

Il s’appuie sur les livrables de l’étape 1 et met en lumière les **logiques métier implicites**, les **règles de décision**, et les **contraintes informationnelles**.

---

## 2. Décisions métier par acteur

### 2.1. Cliniciens prescripteurs
**Services concernés** :
- Urgences
- Réanimation
- Bloc opératoire
- Services extérieurs

---

#### **Décisions clés**
| **Décision** | **Détail** | **Acteur responsable** | **Informations nécessaires** | **Informations produites** | **Source** |
|--------------|------------|------------------------|------------------------------|---------------------------|------------|
| **Prescrire un dosage anti-Xa en urgence** | Évaluer la nécessité clinique et prescrire le dosage pour un patient sous AOD. | Clinicien prescripteur | - Identité du patient <br> - Service prescripteur <br> - Contexte clinique (ex. : hémorragie active) <br> - Protocoles locaux ou recommandations HAS/ANSM <br> - Historique du patient (traitements en cours) | - Prescription électronique (ou papier) <br> - Statut de la demande : "en attente" <br> - Données contextuelles saisies (si applicable) | 02_acteurs_du_domaine.md, 03_concepts_metier_initiaux.md |
| **Classer manuellement une demande par niveau d’urgence** | Attribuer un niveau de priorité à une demande si le SIL ne le fait pas automatiquement. | Clinicien prescripteur | - Critères de priorisation (ex. : hémorragie active = urgence absolue) <br> - Données cliniques du patient <br> - Protocoles locaux | - Niveau de priorité attribué (ex. : "urgence absolue") <br> - Alerte au SIL ou au laboratoire si nécessaire | 05_v