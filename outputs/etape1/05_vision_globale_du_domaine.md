```markdown
# Vision globale du domaine

## Synthèse du domaine

### Contexte général
Le domaine métier concerne la **gestion des demandes urgentes de dosage anti-Xa** dans le cadre de la prise en charge des patients sous **anticoagulants oraux directs (AOD)**. Ces demandes proviennent principalement des services d'urgence, de réanimation, du bloc opératoire et de services extérieurs. Le dosage anti-Xa est une analyse biologique critique, utilisée pour évaluer l'efficacité et la sécurité des AOD, notamment en situation d'urgence où les délais sont critiques (ex. : hémorragie active, chirurgie en urgence).

Le circuit actuel présente des **défauts majeurs** :
- **Non-conformité des échantillons** (tubes non conformes, délais de transport dépassés).
- **Absence de priorisation automatique** des demandes.
- **Traçabilité insuffisante** (pas de suivi en temps réel, risque de perte d'information).
- **Sécurité non garantie** (risque d'erreur d'interprétation ou de transmission).

L'objectif est de **faire évoluer le SIL** pour mettre en place un **circuit informatisé sécurisé, tracé et priorisé**, intégrant :
- Une **priorisation automatique** des demandes en fonction de l'urgence clinique.
- Une **vérification des exigences pré-analytiques** (type de tube, volume, délai de transport).
- Une **intégration des données contextuelles** (traitement, heure de prise, fonction rénale) pour faciliter l'interprétation.
- Une **traçabilité complète** et un **accès sécurisé** aux données.

---

## Acteurs principaux

### Acteurs humains
1. **Cliniciens prescripteurs** (urgentistes, réanimateurs, chirurgiens, etc.)
   - Rôle : Prescrire le dosage anti-Xa en urgence et saisir les données contextuelles.
   - Responsabilités : Respecter les protocoles, vérifier la conformité des tubes, adapter le traitement.

2. **Biologistes médicaux**
   - Rôle : Valider les demandes, prioriser les analyses, interpréter les résultats et émettre des recommandations thérapeutiques.
   - Responsabilités : Garantir la qualité des résultats, respecter les délais critiques, assurer la traçabilité.

3. **Techniciens de laboratoire**
   - Rôle : Préparer et analyser les échantillons, vérifier la conformité des tubes, saisir les résultats.
   - Responsabilités : Respecter les procédures pré-analytiques et analytiques, signaler les non-conformités.

4. **Pharmaciens hospitaliers**
   - Rôle : Conseiller les cliniciens sur l'adaptation des anticoagulants et analyser les interactions médicamenteuses.
   - Responsabilités : Vérifier la cohérence du traitement avec les résultats du dosage.

5. **Personnel administratif/coordinateurs de soins**
   - Rôle : Gérer les flux de demandes et coordonner les prélèvements.
   - Responsabilités : Assurer la logistique et suivre les délais.

6. **Patients**
   - Rôle : Être informé des résultats et donner son consentement.
   - Responsabilités : Informer les cliniciens de la dernière prise d'AOD et signaler les effets indésirables.

7. **Équipe informatique (DSI)**
   - Rôle : Maintenir et faire évoluer le SIL pour répondre aux besoins du circuit.
   - Responsabilités : Garantir la sécurité, la disponibilité et l'interopérabilité du système.

8. **Autorités réglementaires** (HAS, ANSM, ARS, CNIL)
   - Rôle : Vérifier la conformité aux normes (ISO 15189, RGPD).
   - Responsabilités : Auditer les processus et sanctionner les non-conformités.

---

### Acteurs organisationnels
1. **Comité de pilotage du projet SIL**
   - Rôle : Superviser l'évolution du SIL.
   - Responsabilités : Valider les priorités fonctionnelles et allouer les ressources.

2. **Commission des Anti-infectieux et des Anticoagulants (CAI)**
   - Rôle : Définir les protocoles locaux.
   - Responsabilités : Mettre à jour les recommandations et grilles d'interprétation.

3. **Équipe de gestion des risques**
   - Rôle : Identifier et atténuer les risques.
   - Responsabilités : Mettre en place des barrières de sécurité (ex. : alertes automatiques).

---

### Acteurs techniques
1. **Système d'Information de Laboratoire (SIL)**
   - Rôle : Centraliser les demandes, résultats et données contextuelles.
   - Responsabilités : Automatiser la priorisation, assurer la traçabilité et la sécurité.

2. **Dossier Patient Informatisé (DPI)**
   - Rôle : Stocker les données médicales du patient.
   - Responsabilités : Fournir les données au SIL pour l'interprétation.

3. **Analyseurs de laboratoire** (ex. : ACL TOP, STA R Max)
   - Rôle : Réaliser le dosage anti-Xa.
   - Responsabilités : Respecter les procédures analytiques et transmettre les résultats au SIL.

4. **Middleware de laboratoire**
   - Rôle : Gérer les flux d'échantillons et les échanges de données.
   - Responsabilités : Vérifier les conformités pré-analytiques et router les échantillons.

5. **Systèmes d'alerte et de priorisation**
   - Rôle : Classer les demandes et envoyer des alertes.
   - Responsabilités : Intégrer des règles métiers prédéfinies.

---

## Parcours métier actuel supposé

### 1. **Prescription**
- **Acteurs** : Cliniciens (urgentistes, réanimateurs, etc.).
- **Processus** :
  - Le clinicien prescrit un dosage anti-Xa en urgence via un support papier ou un système informatique (si disponible).
  - Il saisit les données contextuelles : type d'AOD, posologie, heure de la dernière prise, fonction rénale, contexte clinique (ex. : hémorragie active).
  - Il vérifie la conformité des tubes (si applicable) et les envoie au laboratoire.
- **Problèmes identifiés** :
  - Prescription papier → risque d'erreur de transcription.
  - Données contextuelles parfois manquantes ou erronées.
  - Absence de vérification automatique de la conformité des tubes.

---

### 2. **Prélèvement et transport**
- **Acteurs** : Personnel soignant (IDE), personnel administratif, coordinateurs de soins.
- **Processus** :
  - Prélèvement sanguin dans un tube citraté 3.2% (à confirmer).
  - Vérification de la conformité du tube (type, volume, délai de transport).
  - Transport rapide vers le laboratoire (température contrôlée, protection de la lumière).
- **Problèmes identifiés** :
  - Non-conformité des tubes (type incorrect, volume insuffisant, délai de transport dépassé).
  - Absence de vérification systématique de la conformité.
  - Retards dans le transport (ex. : attente prolongée avant analyse).

---

### 3. **Réception et vérification des échantillons**
- **Acteurs** : Techniciens de laboratoire.
- **Processus** :
  - Réception des tubes et vérification de la conformité (type, volume, délai de transport).
  - Signalement des non-conformités (si détectées).
  - Préparation des échantillons pour l'analyse (centrifugation, dilution si nécessaire).
- **Problèmes identifiés** :
  - Absence de vérification automatique → analyse d'échantillons non conformes.
  - Retard dans la détection des non-conformités → perte de temps.

---

### 4. **Analyse**
- **Acteurs** : Techniciens de laboratoire, analyseurs automatisés.
- **Processus** :
  - Réalisation du dosage anti-Xa sur l'analyseur.
  - Transmission automatique des résultats bruts au SIL (si intégration disponible).
- **Problèmes identifiés** :
  - Absence d'intégration entre l'analyseur et le SIL → saisie manuelle des résultats → risque d'erreur.
  - Retard dans la transmission des résultats.

---
### 5. **Interprétation**
- **Acteurs** : Biologistes médicaux.
- **Processus** :
  - Récupération des résultats et des données contextuelles (type d'AOD, posologie, heure de la dernière prise, fonction rénale, contexte clinique).
  - Interprétation du résultat en fonction du profil du patient.
  - Rédaction d'un compte-rendu avec recommandations thérapeutiques (ex. : adaptation de la posologie, arrêt temporaire du traitement).
  - Transmission des résultats aux cliniciens (messagerie sécurisée, téléphone, ou système informatique).
- **Problèmes identifiés** :
  - Données contextuelles manquantes ou erronées → interprétation incorrecte.
  - Absence d'aide à la décision → variabilité dans les interprétations.
  - Retard dans la transmission des résultats aux cliniciens.

---
### 6. **Prise en charge thérapeutique**
- **Acteurs** : Cliniciens, pharmaciens.
- **Processus** :
  - Adaptation du traitement anticoagulant en fonction des résultats et des recommandations.
  - Administration d'un antidote si nécessaire (ex. : andexanet alfa pour les anti-Xa).
  - Surveillance du patient.
- **Problèmes identifiés** :
  - Retard dans l'adaptation du traitement → complications graves.
  - Absence de recommandations claires → décisions thérapeutiques inadaptées.

---
### 7. **Traçabilité et archivage**
- **Acteurs** : Biologistes, techniciens de laboratoire, SIL.
- **Processus** :
  - Enregistrement des étapes du circuit (prescription, prélèvement, analyse, interprétation).
  - Conservation des données pour les audits (durée minimale : 10 ans).
- **Problèmes identifiés** :
  - Traçabilité incomplète → impossibilité de retracer les actions en cas d'erreur ou d'audit.
  - Absence de signature électronique → impossibilité de prouver la validité des résultats.

---

## Irritants métier

### 1. **Non-conformité des échantillons**
- **Problème** :
  Les tubes ne respectent pas toujours les exigences pré-analytiques (type incorrect, volume insuffisant, délai de transport dépassé).
- **Conséquences** :
  - Rejet des échantillons → retard dans la prise en charge.
  - Résultats erronés → interprétation incorrecte.
- **Causes racines** :
  - Absence de vérification systématique de la conformité.
  - Manque de formation des personnels soignants.
  - Absence de feedback immédiat en cas de non-conformité.

---
### 2. **Délais critiques non respectés**
- **Problème** :
  Les délais entre la prescription et la transmission des résultats sont souvent dépassés, notamment pour les cas urgents.
- **Conséquences** :
  - Aggravation de l'état clinique du patient.
  - Complications thrombotiques ou hémorragiques.
- **Causes racines** :
  - Absence de priorisation automatique des demandes.
  - Flux de travail inefficace (ex. : traitement séquentiel des demandes).
  - Retards dans le transport ou l'analyse des échantillons.

---
### 3. **Données contextuelles manquantes ou erronées**
- **Problème** :
  Les données nécessaires à l'interprétation (type d'AOD, posologie, heure de la dernière prise, fonction rénale) sont parfois absentes ou incorrectes.
- **Conséquences** :
  - Interprétation erronée du résultat.
  - Adaptation thérapeutique inadaptée.
- **Causes racines** :
  - Saisie manuelle des données → erreurs de transcription.
  - Absence d'intégration entre le SIL et le DPI → données non synchronisées.
  - Manque de formation des cliniciens.

---
### 4. **Absence de priorisation automatique**
- **Problème** :
  Les demandes ne sont pas classées par ordre d'urgence, ce qui entraîne des retards pour les cas critiques.
- **Conséquences** :
  - Traitement séquentiel des demandes → retard pour les cas urgents.
  - Accumulation des demandes non traitées.
- **Causes racines** :
  - Absence de règles métiers prédéfinies dans le SIL.
  - Circuit manuel → risque d'erreur de classement.

---
### 5. **Traçabilité insuffisante**
- **Problème** :
  Les étapes du circuit ne sont pas systématiquement tracées, ce qui rend difficile la retrace des actions en cas d'erreur ou d'audit.
- **Conséquences** :
  - Impossibilité de prouver la conformité en cas d'audit.
  - Difficulté à identifier les causes des retards ou des erreurs.
- **Causes racines** :
  - Absence de journal électronique (audit trail) dans le SIL.
  - Enregistrement manuel des données → risque d'oubli ou d'erreur.

---
### 6. **Sécurité non garantie**
- **Problème** :
  Les données du circuit ne sont pas suffisamment protégées (accès non autorisé, absence de chiffrement, etc.).
- **Conséquences** :
  - Fuite de données patients → violation du RGPD.
  - Modification frauduleuse des résultats → adaptation thérapeutique dangereuse.
- **Causes racines** :
  - Absence d'authentification forte.
  - Droits d'accès non différenciés.
  - Absence de chiffrement des données sensibles.

---
### 7. **Manque de collaboration pluridisciplinaire**
- **Problème** :
  La communication entre les acteurs (cliniciens, biologistes, pharmaciens) est parfois inefficace.
- **Conséquences** :
  - Retard dans la transmission des informations.
  - Décisions thérapeutiques non optimales.
- **Causes racines** :
  - Absence de canaux de communication dédiés (ex. : messagerie sécurisée intégrée au SIL).
  - Protocoles locaux non partagés ou obsolètes.

---
### 8. **Surcharge de travail pour les équipes**
- **Problème** :
  Le circuit actuel est inefficace, ce qui entraîne une surcharge de travail pour les cliniciens, biologistes et techniciens.
- **Conséquences** :
  - Stress accru → risque d'erreur.
  - Burn-out des équipes.
- **Causes racines** :
  - Absence d'automatisation (priorisation, vérification des conformités).
  - Flux de travail manuel → perte de temps.

---

## Objectifs du futur circuit informatisé

### 1. **Automatiser et sécuriser le circuit**
- **Priorisation automatique** :
  - Classer les demandes en fonction de leur urgence clinique (ex. : hémorragie active → priorité absolue, chirurgie programmée → priorité haute).
  - Intégrer des règles métiers prédéfinies dans le SIL.
- **Vérification des exigences pré-analytiques** :
  - Alerter en temps réel si le type de tube ou le volume est incorrect.
  - Bloquer l'analyse si le délai de transport est dépassé.
  - Signalement au prescripteur et au laboratoire pour demande de complément.
- **Sécurité des données** :
  - Mettre en place une authentification forte (ex. : carte CPS).
  - Différencier les droits d'accès (ex. : les cliniciens ne peuvent pas modifier les résultats validés).
  - Chiffrer les données sensibles.

---
### 2. **Améliorer la conformité des échantillons**
- **Vérification systématique** :
  - Intégrer un module de vérification automatique de la conformité des tubes dans le SIL.
  - Bloquer l'analyse si l'échantillon est non conforme.
- **Procédure de gestion des non-conformités** :
  - Définir un protocole clair pour gérer les échantillons non conformes (refus, demande de complément, escalade).
  - Automatiser la transmission des alertes aux prescripteurs.

---
### 3. **Faciliter l'interprétation des résultats**
- **Intégration des données contextuelles** :
  - Récupérer automatiquement les données depuis le DPI (fonction rénale, traitements en cours).
  - Proposer des listes déroulantes pour le type d'AOD et la posologie.
  - Afficher les données contextuelles de manière claire et structurée.
- **Aide à la décision** :
  - Intégrer des grilles d'interprétation pour chaque AOD et chaque contexte clinique.
  - Proposer des recommandations thérapeutiques automatiques (ex. : adaptation de la posologie, administration d'un antidote).
  - Afficher des seuils d'alerte en cas de surdosage ou de sous-dosage.

---
### 4. **Garantir la traçabilité et l'auditabilité**
- **Journal électronique (audit trail)** :
  - Enregistrer systématiquement toutes les actions (prescription, prélèvement, analyse, interprétation, transmission).
  - Horodater chaque action et associer l'identifiant de l'utilisateur.
  - Permettre l'export des logs pour les audits internes/externes.
- **Signature électronique** :
  - Implémenter une signature électronique pour les résultats validés.
  - Garantir la non-répudiation des actions.

---
### 5. **Optimiser les flux de travail**
- **Disponibilité 24/7 du SIL** :
  - Garantir la redondance des serveurs et les sauvegardes automatiques.
  - Planifier les maintenances en dehors des périodes critiques.
- **Gestion des astreintes** :
  - Définir une liste des services couverts par l'astreinte.
  - Mettre en place une procédure de déclenchement automatique (ex. : alerte via le SIL).
  - Permettre aux biologistes d'astreinte d'accéder aux données patients et aux protocoles locaux.

---
### 6. **Améliorer la collaboration pluridisciplinaire**
- **Canaux de communication dédiés** :
  - Intégrer une messagerie sécurisée dans le SIL pour faciliter la communication entre cliniciens, biologistes et pharmaciens.
  - Automatiser la transmission des résultats et des recommandations.
- **Partage des protocoles** :
  - Centraliser les protocoles locaux dans le SIL.
  - Mettre à jour automatiquement les grilles d'interprétation.

---
### 7. **Impliquer le patient**
- **Portail patient** :
  - Permettre aux patients d'accéder à leurs résultats et aux recommandations thérapeutiques.
  - Envoyer des alertes en cas d'anomalie.
  - Respecter le RGPD (authentification forte, consentement éclairé).

---
### 8. **Garantir la conformité réglementaire**
- **Respect des normes** :
  - Mettre en place des mécanismes pour garantir la conformité aux normes ISO 15189, RGPD, et aux recommandations HAS/ANSM.
  - Permettre les audits internes/externes via l'export des logs.

---

## Informations à collecter avant de passer à l’étape 2

### 1. **Exigences pré-analytiques**
- **Critères de conformité des tubes** :
  - Type de tube exact (ex. : tube citraté 3.2%).
  - Volume minimal requis.
  - Délai maximal entre prélèvement et analyse.
  - Conditions de transport (température, protection de la lumière).
- **Procédure de gestion des non-conformités** :
  - Qui valide la conformité des tubes ? (Biologiste, IDE, système automatisé ?)
  - Que faire en cas de non-conformité ? (Refus systématique, demande de complément, escalade ?)

---
### 2. **Critères de priorisation**
- **Grille de priorisation complète** :
  - Liste des critères d'urgence clinique (ex. : hémorragie active, chirurgie en urgence, suspicion de surdosage).
  - Délais maximaux acceptables pour chaque niveau de priorité.
- **Règles d'escalade** :
  - Que faire en cas de conflit de priorités ? (Ex. : deux demandes en urgence absolue ?)

---
### 3. **Données contextuelles à collecter**
- **Liste exhaustive** :
  - Type d'AOD (apixaban, rivaroxaban, édoxaban, etc.).
  - Posologie (dose et fréquence).
  - Heure de la dernière prise (précision requise : minutes/heures ?).
  - Fonction rénale (clairance de la créatinine, formule utilisée : CKD-EPI ou MDRD ?).
  - Contexte clinique (hémorragie active, chirurgie programmée, etc.).
  - Autres traitements (antiagrégants, autres anticoagulants).
- **Méthode de saisie** :
  - Saisie manuelle ou intégration automatique depuis le DPI ?
  - Champs obligatoires et formatage automatique.

---
### 4. **Rôles et responsabilités**
- **Validation des demandes** :
  - Qui valide les demandes ? (Biologiste, technicien, système automatisé ?)
- **Accès aux résultats** :
  - Qui a accès aux résultats et dans quelles conditions ? (Cliniciens, pharmaciens, patient ?)
- **Recommandations thérapeutiques** :
  - Qui émet les recommandations ? (Biologiste, pharmacien, système automatisé ?)

---
### 5. **Intégration avec les systèmes existants**
- **Compatibilité du SIL** :
  - Le SIL actuel permet-il une telle évolution ? (Compatibilité avec le DPI, les analyseurs, etc.)
  - Existence d'API ou de connecteurs pour échanger des données ?
- **Interfaces dédiées** :
  - Faut-il prévoir une interface spécifique pour les cliniciens ?

---
### 6. **Gestion des exceptions**
- **Hors heures ouvrables** :
  - Liste des services couverts par l'astreinte.
  - Procédure de déclenchement de l'astreinte.
- **Demandes non conformes** :
  - Que faire en cas de non-conformité des tubes ? (Refus, demande de complément, escalade ?)

---
### 7. **Exigences réglementaires**
- **Normes à respecter** :
  - Liste des normes applicables (ISO 15189, RGPD, recommandations HAS/ANSM).
  - Durée de conservation des données.
  - Format des logs d'audit.
- **Signature électronique** :
  - Faut-il prévoir une signature électronique pour les résultats ?

---
### 8. **Retours d'expérience**
- **Analyse des dysfonctionnements actuels** :
  - Quels sont les principaux irritants du circuit actuel ?
  - Quelles sont les causes racines des retards ou des erreurs ?
- **Bonnes pratiques** :
  - Existe-t-il des retours d'expérience d'autres établissements ayant mis en place un circuit similaire ?

---
### 9. **Attentes des utilisateurs**
- **Cliniciens** :
  - Quelles fonctionnalités attendent-ils du futur SIL ? (Ex. : priorisation automatique, intégration des données contextuelles.)
- **Biologistes** :
  - Quels outils d'aide à la décision souhaitent-ils ? (Ex. : grilles d'interprétation, seuils d'alerte.)
- **Techniciens de laboratoire** :
  - Quels modules de vérification automatique des conformités souhaitent-ils ?

---
### 10. **Budget et planning**
- **Budget alloué** :
  - Quel est le budget disponible pour le projet ?
- **Planning** :
  - Quels sont les délais impartis pour la mise en place du nouveau circuit ?
```