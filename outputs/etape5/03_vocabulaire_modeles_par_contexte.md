# **Vocabulaire et modèles par Bounded Context**
**Domaine métier** : Gestion des demandes urgentes de dosage anti-Xa dans le SIL
**Date** : 2024-06-10
**Version** : 1.0
**Auteurs** : Analyste DDD
**Sources principales** :
- Livrables étape 1 : `01_reformulation_du_besoin.md`, `02_acteurs_du_domaine.md`, `03_concepts_metier_initiaux.md`, `04_contraintes_et_risques.md`, `05_vision_globale_du_domaine.md`
- Livrables étape 2 : `01_cartographie_acteurs_responsabilites.md`, `02_attentes_objectifs_acteurs.md`, `03_decisions_informations_manipulees.md`, `04_regles_metier.md`, `05_priorites_exceptions_contraintes.md`, `06_conflits_objectifs_arbitrages.md`, `07_base_modelisation_comportementale.md`, `08_glossaire_metier.md`
- Livrables étape 4 : `01_zones_fonctionnelles_domaine.md`, `02_proposition_sous_domaines.md`, `03_classification_sous_domaines.md`, `04_interactions_sous_domaines.md`, `05_priorites_conception_sous_domaines.md`, `06_synthese_decoupage_sous_domaines.md`

---

---

## **1. Introduction**
Ce document identifie et analyse le **vocabulaire métier** et les **modèles conceptuels** pour chaque **Bounded Context candidat**, en mettant en lumière :
- Les **termes clés** avec leur **sens stable** dans le contexte.
- Les **concepts partagés** entre contextes et les **risques d'ambiguïté**.
- Les **différences de signification** selon le contexte.
- Les **termes à éviter** ou à **traduire** entre contextes.
- Les **points à valider** avec les experts métier pour éviter les malentendus.

L'objectif est de :
- **Clarifier les frontières sémantiques** entre les Bounded Contexts.
- **Éviter les ambiguïtés** dans les échanges entre contextes.
- **Préparer les contrats d'échange** entre contextes (ex. : prescription → priorisation).
- **Fonder la modélisation comportementale** sur un vocabulaire partagé et non ambigu.

---

---

## **2. Tableau synthétique des Bounded Contexts et de leur vocabulaire**

| **Bounded Context** | **Termes clés avec sens stable** | **Concepts partagés** | **Différences de signification** | **Termes à éviter ou traduire** | **Points à valider** |
|---------------------|----------------------------------|-----------------------|----------------------------------|---------------------------------|----------------------|
| **BC-AXA-01 : Prescription Clinique** | **Prescription électronique**, **Protocoles locaux (CAI)**, **Validation biologique**, **Contexte clinique**, **AOD** | **AOD**, **Contexte clinique**, **Délai critique** | **"Prescription"** : Dans BC-AXA-01 = acte médical formalisé. Dans BC-AXA-03 = demande classée par urgence. | **"Urgence"** : À éviter dans BC-AXA-01 (préférer "niveau de priorité"). **"Résultat"** : À éviter (préférer "prescription validée"). | - Qui valide définitivement une prescription rejetée ? <br> - Comment gérer les exceptions aux protocoles ? |
| **BC-AXA-02 : Gestion Pré-Analytique** | **Tube citraté 3.2%**, **Volume minimal**, **Délai de transport**, **Non-conformité**, **Conformité pré-analytique** | **AOD**, **Contexte clinique**, **Traçabilité** | **"Non-conformité"** : Dans BC-AXA-02 = rejet de l'échantillon. Dans BC-AXA-07 = alerte sur un résultat aberrant. | **"Urgence"** : À éviter (préférer "échantillon conforme"). **"Validation"** : À préciser (technicien vs. biologiste). | - Quels sont les critères exacts de conformité par AOD ? <br> - Qui valide définitivement un tube non conforme ? |
| **BC-AXA-03 : Ordonnancement et Priorisation** | **Niveau d'urgence**, **Délai critique**, **Ordonnancement**, **Conflit de priorité**, **Ressources disponibles** | **AOD**, **Contexte clinique**, **Traçabilité** | **"Priorité"** : Dans BC-AXA-03 = classement automatique. Dans BC-AXA-01 = validation biologique. | **"Prescription"** : À éviter (préférer "demande validée"). **"Résultat"** : À éviter (préférer "niveau de priorité attribué"). | - Quels sont les critères exacts pour classer une demande en "urgence absolue" ? <br> - Qui a l'autorité finale en cas de conflit ? |
| **BC-AXA-04 : Analyse Laboratoire** | **Résultat brut**, **Intégration automatique**, **Résultats aberrants**, **Contrôle qualité** | **AOD**, **Traçabilité**, **Contexte clinique** | **"Résultat"** : Dans BC-AXA-04 = donnée brute de l'analyseur. Dans BC-AXA-05 = interprétation clinique. | **"Urgence"** : À éviter (préférer "résultat conforme"). **"Validation"** : À préciser (technicien vs. biologiste). | - Quels sont les seuils d'alerte pour les résultats aberrants ? <br> - Les analyseurs sont-ils compatibles avec le SIL ? |
| **BC-AXA-05 : Interprétation Clinique** | **Résultat interprété**, **Grilles d'interprétation**, **Recommandations thérapeutiques**, **Seuil d'alerte**, **Aide à la décision** | **AOD**, **Contexte clinique**, **Traçabilité** | **"Recommandation"** : Dans BC-AXA-05 = conseil thérapeutique. Dans BC-AXA-07 = alerte sur un résultat critique. | **"Prescription"** : À éviter (préférer "recommandation validée"). **"Urgence"** : À éviter (préférer "seuil d'alerte déclenché"). | - Quels sont les seuils exacts pour chaque AOD et contexte clinique ? <br> - Qui émet les recommandations finales ? |
| **BC-AXA-06 : Collaboration et Communication** | **Messagerie sécurisée**, **Alertes critiques**, **Archivage des communications**, **Traçabilité des échanges** | **AOD**, **Traçabilité**, **Contexte clinique** | **"Alerte"** : Dans BC-AXA-06 = notification sécurisée. Dans BC-AXA-03 = classement automatique. | **"Prescription"** : À éviter (préférer "communication validée"). **"Résultat"** : À éviter (préférer "information partagée"). | - Quels canaux de communication sont utilisés actuellement ? <br> - Comment gérer les communications en dehors des heures ouvrables ? |
| **BC-AXA-07 : Gestion des Exceptions** | **Astreinte biologique**, **Non-conformité en astreinte**, **Escalade**, **Procédures d'urgence** | **AOD**, **Traçabilité**, **Contexte clinique** | **"Non-conformité"** : Dans BC-AXA-07 = gestion en astreinte. Dans BC-AXA-02 = rejet de l'échantillon. | **"Urgence"** : À éviter (préférer "astreinte activée"). **"Validation"** : À préciser (biologiste d'astreinte). | - Quels sont les services couverts par l'astreinte ? <br> - Comment gérer les non-conformités en astreinte ? |
| **BC-AXA-08 : Intégration des Données** | **Intégration automatique**, **Formats de données (HL7 FHIR, API)**, **Compatibilité technique**, **Données patients** | **AOD**, **Contexte clinique**, **Traçabilité** | **"Donnée"** : Dans BC-AXA-08 = flux technique entre systèmes. Dans BC-AXA-01 = prescription médicale. | **"Prescription"** : À éviter (préférer "donnée patient intégrée"). **"Résultat"** : À éviter (préférer "donnée analytique transmise"). | - Le SIL est-il compatible avec le DPI et les analyseurs ? <br> - Quels formats de données sont utilisés pour les échanges ? |
| **BC-AXA-09 : G