# **Règles Métier et Invariants des Agrégats**
**Domaine métier** : Gestion des demandes urgentes de dosage anti-Xa dans le SIL
**Date** : 2024-06-15
**Version** : 1.0
**Auteurs** : Architecte DDD
**Sources** : Livrables étape 5 (`01_contextes_candidats.md`, `02_frontieres_responsabilites_contextes.md`, `03_vocabulaire_modeles_par_contexte.md`, `04_dependances_contrats_contextes.md`, `05_risques_arbitrages_contextes.md`, `06_cartographie_bounded_contexts.md`, `07_synthese_bounded_contexts.md`)

---

---

## **1. Introduction**
Ce document formalise les **règles métier** et les **invariants** pour chaque **agrégat** identifié dans le système de gestion des demandes urgentes de dosage anti-Xa. Les invariants sont des **règles de cohérence** qui doivent toujours être respectées à l'intérieur d'un agrégat, quelle que soit l'opération effectuée. Les règles métier sont traduites en **contraintes précises**, vérifiables et directement associées à leur agrégat responsable.

**Objectifs** :
- **Formaliser** les règles métier et les invariants pour chaque agrégat.
- **Traduire** les règles issues du corpus métier en contraintes vérifiables.
- **Associer** chaque règle/invariant à son agrégat responsable.
- **Identifier** les règles encore incertaines ou à valider avec les experts métier.
- **Fournir** une base pour la conception des services de domaine et la validation des modèles.

**Méthodologie** :
- Pour chaque agrégat, analyser les **règles métier critiques** et les **décisions clés** issues du corpus.
- Formaliser les invariants comme des **règles de cohérence transactionnelle**.
- Documenter les **préconditions** et **postconditions** pour chaque opération métier.
- **Associer** chaque règle/invariant à son agrégat responsable.
- **Identifier** les règles encore incertaines ou à valider avec les experts métier.

---

---

## **2. BC-AXA-01 : Prescription Clinique**
**Type** : Cœur stratégique
**Responsabilité principale** :
Gérer la **prescription électronique** des dosages anti-Xa en urgence et valider leur **pertinence clinique** selon les protocoles locaux (CAI) et les recommandations HAS/ANSM.

---

### **2.1. Agrégat : `Prescription`**
#### **Invariants de Cohérence**

| **ID** | **Invariant** | **Description** | **Violation** | **Source** |
|--------|---------------|-----------------|---------------|------------|
| **INV-PRE-01** | **Exhaustivité des données** | Une prescription doit contenir toutes les données obligatoires : `patientId`, `aodType`, `lastDoseTime`, `creatinineClearance`, `clinicalContextType`. | La prescription est marquée comme `incomplete` et bloquée pour validation. | `RBC-0