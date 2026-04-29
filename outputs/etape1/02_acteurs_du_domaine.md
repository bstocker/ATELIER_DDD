```markdown
# Acteurs du domaine

## Acteurs humains

### 1. **Cliniciens prescripteurs**
- **Services concernés** :
  - Urgences
  - Réanimation
  - Bloc opératoire
  - Services extérieurs (ex. : cardiologie, médecine interne)
- **Rôle** :
  - Prescrire le dosage anti-Xa en urgence pour les patients sous AOD.
  - Évaluer le contexte clinique du patient (ex. : hémorragie active, chirurgie programmée).
  - Saisir les données contextuelles nécessaires à l'interprétation (ex. : heure de la dernière prise d'AOD, fonction rénale).
- **Responsabilités** :
  - Respecter les indications de dosage anti-Xa (protocoles locaux ou recommandations HAS/ANSM).
  - Vérifier la conformité des tubes avant envoi au laboratoire (si applicable).
  - Utiliser les résultats pour adapter la prise en charge thérapeutique.
- **Interactions principales** :
  - Avec le **SIL** (prescription électronique).
  - Avec le **laboratoire de biologie** (demande de dosage, transmission des données contextuelles).
  - Avec le **pharmacien** (pour ajuster le traitement si nécessaire).

---

### 2. **Biologistes médicaux**
- **Rôle** :
  - Valider les demandes de dosage anti-Xa et prioriser les analyses en fonction de l'urgence clinique.
  - Interpréter les résultats en tenant compte :
    - Du type d'AOD et de la posologie.
    - De l'heure de la dernière prise.
    - De la fonction rénale du patient.
    - Du contexte clinique (ex. : suspicion de surdosage).
  - Rédiger un compte-rendu d'interprétation avec recommandations thérapeutiques si nécessaire.
- **Responsabilités** :
  - Garantir la qualité et la fiabilité des résultats.
  - Respecter les délais critiques pour les demandes urgentes.
  - Assurer la traçabilité des analyses (audit trail).
- **Interactions principales** :
  - Avec le **SIL** (validation des résultats, saisie des interprétations).
  - Avec les **cliniciens** (communication des résultats et recommandations).
  - Avec les **techniciens de laboratoire** (supervision des analyses).

---
### 3. **Techniciens de laboratoire (ou manipulateurs en électroradiologie)**
- **Rôle** :
  - Préparer et analyser les échantillons biologiques (dosage anti-Xa).
  - Vérifier la conformité des tubes (type, volume, délai de transport).
  - Saisir les résultats dans le SIL.
- **Responsabilités** :
  - Respecter les procédures pré-analytiques et analytiques.
  - Signaler les non-conformités des échantillons.
  - Participer à la maintenance des équipements de dosage.
- **Interactions principales** :
  - Avec le **SIL** (saisie des résultats, gestion des échantillons).
  - Avec les **biologistes** (transmission des échantillons et des résultats bruts).

---
### 4. **Pharmaciens hospitaliers**
- **Rôle** :
  - Conseiller les cliniciens sur le choix et l'adaptation des anticoagulants (AOD).
  - Analyser les interactions médicamenteuses et les contre-indications.
  - Participer à la gestion des urgences hémorragiques (ex. : administration d'antidotes).
- **Responsabilités** :
  - Vérifier la cohérence du traitement prescrit avec les résultats du dosage anti-Xa.
  - Alerter en cas de risque de surdosage ou de sous-dosage.
- **Interactions principales** :
  - Avec les **cliniciens** (collaboration thérapeutique).
  - Avec les **biologistes** (interprétation conjointe des résultats).

---
### 5. **Personnel administratif ou coordinateurs de soins**
- **Rôle** :
  - Gérer les flux de demandes entre les services et le laboratoire.
  - Coordonner les prélèvements et le transport des échantillons.
- **Responsabilités** :
  - Assurer la logistique des prélèvements (ex. : acheminement rapide des tubes).
  - Suivre les délais de traitement des demandes.
- **Interactions principales** :
  - Avec les **cliniciens** (organisation des prélèvements).
  - Avec le **laboratoire** (suivi des échantillons).

---
### 6. **Patients**
- **Rôle implicite** :
  - Être informé de la nécessité du dosage et des résultats.
  - Donner son consentement éclairé pour l'analyse (si applicable).
- **Responsabilités** :
  - Informer les cliniciens de la dernière prise d'AOD.
  - Signaler tout effet indésirable (ex. : saignement).
- **Interactions principales** :
  - Avec les **cliniciens** (communication des symptômes).
  - Avec le **SIL** (accès aux résultats via un portail patient, si prévu).

---
### 7. **Équipe informatique (DSI ou éditeur du SIL)**
- **Rôle** :
  - Maintenir et faire évoluer le SIL pour répondre aux besoins du circuit des demandes urgentes.
  - Intégrer les modules de priorisation, traçabilité et aide à l'interprétation.
- **Responsabilités** :
  - Garantir la sécurité et la disponibilité du système.
  - Former les utilisateurs (cliniciens, biologistes, techniciens).
- **Interactions principales** :
  - Avec les **biologistes** et **cliniciens** (recueil des besoins fonctionnels).
  - Avec les **fournisseurs d'équipements de laboratoire** (intégration des analyseurs).

---
### 8. **Autorités réglementaires (ex. : HAS, ANSM, ARS)**
- **Rôle** :
  - Vérifier la conformité du circuit avec les bonnes pratiques et les normes (ex. : ISO 15189, RGPD).
- **Responsabilités** :
  - Auditer les processus et les résultats.
  - Sanctionner en cas de non-conformité.
- **Interactions principales** :
  - Avec le **laboratoire** (audits).
  - Avec la **direction de l'établissement** (rapports de conformité).

---
## Acteurs organisationnels

### 1. **Comité de pilotage du projet SIL**
- **Rôle** :
  - Superviser l'évolution du SIL pour intégrer le circuit des demandes urgentes de dosage anti-Xa.
- **Responsabilités** :
  - Valider les priorités fonctionnelles.
  - Allouer les ressources nécessaires.
- **Interactions** :
  - Avec la **DSI**, les **biologistes** et les **cliniciens**.

---
### 2. **Commission des anti-infectieux et des anticoagulants (CAI)**
- **Rôle** :
  - Définir les protocoles locaux pour la prescription et l'interprétation des dosages anti-Xa.
- **Responsabilités** :
  - Mettre à jour les recommandations en fonction des données scientifiques.
- **Interactions** :
  - Avec les **cliniciens**, les **biologistes** et les **pharmaciens**.

---
### 3. **Équipe de gestion des risques**
- **Rôle** :
  - Identifier et atténuer les risques liés au circuit (ex. : erreurs de dosage, retards).
- **Responsabilités** :
  - Mettre en place des barrières de sécurité (ex. : alertes automatiques).
- **Interactions** :
  - Avec le **laboratoire** et la **DSI**.

---
## Acteurs techniques

### 1. **Système d'Information de Laboratoire (SIL)**
- **Rôle** :
  - Centraliser les demandes de dosage, les résultats et les données contextuelles.
  - Automatiser la priorisation des demandes.
  - Assurer la traçabilité et la sécurité des données.
- **Responsabilités** :
  - Respecter les normes d'interopérabilité (ex. : HL7, FHIR).
  - Garantir la disponibilité 24/7 pour les urgences.
- **Interactions** :
  - Avec les **utilisateurs humains** (cliniciens, biologistes).
  - Avec les **systèmes externes** (DPI, logiciels de gestion des prélèvements).

---
### 2. **Dossier Patient Informatisé (DPI)**
- **Rôle** :
  - Stocker les données médicales du patient (ex. : fonction rénale, traitements en cours).
  - Fournir ces données au SIL pour l'interprétation des résultats.
- **Responsabilités** :
  - Assurer l'intégrité et la confidentialité des données.
- **Interactions** :
  - Avec le **SIL** (échanges de données via interfaces).

---
### 3. **Analyseurs de laboratoire (ex. : ACL TOP, STA R Max)**
- **Rôle** :
  - Réaliser le dosage anti-Xa sur les échantillons biologiques.
- **Responsabilités** :
  - Respecter les procédures analytiques et les contrôles qualité.
- **Interactions** :
  - Avec le **SIL** (transmission des résultats bruts).
  - Avec les **techniciens de laboratoire**.

---
### 4. **Logiciels de gestion des prélèvements (ex. : middleware de laboratoire)**
- **Rôle** :
  - Gérer les flux d'échantillons entre les services et le laboratoire.
  - Automatiser la vérification des conformités pré-analytiques.
- **Responsabilités** :
  - Optimiser les délais de traitement.
- **Interactions** :
  - Avec le **SIL** et les **systèmes de prélèvement**.

---
### 5. **Systèmes d'alerte et de priorisation**
- **Rôle** :
  - Classer les demandes en fonction de leur urgence clinique.
  - Envoyer des alertes aux biologistes et aux cliniciens en cas de criticité.
- **Responsabilités** :
  - Intégrer des règles métiers prédéfinies (ex. : priorité absolue pour les hémorragies actives).
- **Interactions** :
  - Avec le **SIL** et les **utilisateurs**.

---
## Zones de dépendance entre acteurs

### 1. **Dépendance des cliniciens envers le SIL et le DPI**
- **Pourquoi ?** :
  - Les cliniciens ont besoin du SIL pour prescrire les dosages et du DPI pour accéder aux données patients.
- **Risques** :
  - Indisponibilité du SIL → blocage des prescriptions.
  - Données manquantes dans le DPI → interprétation erronée des résultats.

---
### 2. **Dépendance des biologistes envers les techniciens et le SIL**
- **Pourquoi ?** :
  - Les biologistes s'appuient sur les techniciens pour les analyses et sur le SIL pour la traçabilité.
- **Risques** :
  - Erreur de saisie des résultats par les techniciens → erreur d'interprétation.
  - Défaillance du SIL → perte de traçabilité.

---
### 3. **Dépendance du laboratoire envers les systèmes externes (DPI, SIL)**
- **Pourquoi ?** :
  - Le laboratoire a besoin des données du DPI (fonction rénale, traitements) et du SIL pour gérer les demandes.
- **Risques** :
  - Retard dans la transmission des données → retard dans l'analyse.
  - Incompatibilité des formats de données → erreur d'interprétation.

---
### 4. **Dépendance des systèmes techniques (SIL, analyseurs) envers la DSI**
- **Pourquoi ?** :
  - La DSI maintient et fait évoluer les systèmes critiques.
- **Risques** :
  - Mise à jour non planifiée → indisponibilité du système.
  - Manque de formation des utilisateurs → erreurs d'utilisation.

---
### 5. **Dépendance des cliniciens et biologistes envers les protocoles de la CAI**
- **Pourquoi ?** :
  - Les protocoles définissent les indications de dosage et les seuils d'interprétation.
- **Risques** :
  - Protocoles obsolètes → décisions thérapeutiques inadaptées.
  - Absence de protocole → variabilité des pratiques.

---
### 6. **Dépendance des patients envers les cliniciens et le SIL**
- **Pourquoi ?** :
  - Les patients dépendent des cliniciens pour prescrire les dosages et du SIL pour la transmission des résultats.
- **Risques** :
  - Mauvaise communication des résultats → retard de prise en charge.
  - Accès limité aux résultats → anxiété du patient.

---
## Synthèse des interactions clés
| **Acteur A**               | **Acteur B**               | **Type d'interaction**                     | **Enjeu**                                  |
|----------------------------|----------------------------|--------------------------------------------|--------------------------------------------|
| Cliniciens                 | SIL                       | Prescription, saisie des données contextuelles | Rapidité et exhaustivité des données      |
| Cliniciens                 | Laboratoire                | Transmission des échantillons et des demandes | Respect des délais et conformité des tubes |
| Biologistes                | SIL                       | Validation des résultats, interprétation   | Traçabilité et sécurité des données        |
| Techniciens de laboratoire | SIL                       | Saisie des résultats                      | Fiabilité des données                     |
| SIL                        | DPI                       | Échanges de données (fonction rénale, traitements) | Cohérence des informations                |
| SIL                        | Analyseurs                | Transmission des résultats bruts          | Intégration des données analytiques        |
| CAI                        | Cliniciens/Biologistes    | Mise à jour des protocoles                 | Adaptation aux bonnes pratiques            |
| DSI                        | SIL                       | Maintenance et évolution du système        | Disponibilité et sécurité du SIL           |
| Patient                    | Cliniciens/SIL             | Accès aux résultats et consentement       | Transparence et information du patient     |
```