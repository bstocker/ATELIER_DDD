```markdown
# Base pour la modélisation comportementale
**Domaine métier** : Gestion des demandes urgentes de dosage anti-Xa dans le SIL
**Date** : [À compléter]
**Version** : 1.0
**Auteurs** : Analyste Métier
**Sources** : Livrables étape 1 (01_reformulation_du_besoin.md, 02_acteurs_du_domaine.md, 03_concepts_metier_initiaux.md, 04_contraintes_et_risques.md, 05_vision_globale_du_domaine.md)

---

## 1. Introduction
Ce document synthétise les résultats de l'**étape 2** de la démarche DDD pour le domaine des **demandes urgentes de dosage anti-Xa**, en fournissant une base fiable pour la **modélisation comportementale** future. Il ne définit pas encore d'architecture technique, mais établit les fondations métier nécessaires pour :

- **Comprendre les acteurs et leurs responsabilités**
- **Identifier les décisions clés et les informations manipulées**
- **Formaliser les règles métier structurantes**
- **Mettre en lumière les priorités, exceptions et contraintes**
- **Repérer les conflits d'objectifs à arbitrer**

Cette synthèse servira de référence pour l'étape 3 (modélisation comportementale) et garantit que la future application répondra aux besoins métier tout en respectant les contraintes réglementaires et organisationnelles.

---

## 2. Synthèse des acteurs et responsabilités

### 2.1. Acteurs humains et organisationnels

| **Acteur** | **Rôle principal** | **Responsabilités clés** | **Points de vigilance** |
|------------|-------------------|--------------------------|-------------------------|
| **Cliniciens prescripteurs** | Prescrire et adapter le traitement anticoagulant | - Respecter les protocoles locaux et recommandations HAS/ANSM <br> - Saisir les données contextuelles (type d'AOD, posologie, heure de dernière prise, fonction rénale) <br> - Vérifier la conformité des tubes avant envoi <br> - Adapter le traitement en fonction des résultats | - **Priorisation manuelle** des demandes si le SIL ne le fait pas automatiquement <br> - **Saisie manuelle** des données contextuelles → risque d'erreur <br> - **Responsabilité partagée** sur la gestion des non-conformités des tubes |
| **Biologistes médicaux** | Valider, prioriser et interpréter les résultats | - Valider les demandes de dosage <br> - Prioriser les analyses selon l'urgence clinique <br> - Interpréter les résultats en contexte (type d'AOD, fonction rénale, heure de dernière prise) <br> - Rédiger des recommandations thérapeutiques <br> - Assurer la traçabilité (audit trail) | - **Validation biologique obligatoire** avant analyse <br> - **Interprétation complexe** nécessitant des données contextuelles complètes <br> - **Collaboration avec les pharmaciens** pour valider les recommandations |
| **Techniciens de laboratoire** | Préparer et analyser les échantillons | - Vérifier la conformité des tubes (type, volume, délai de transport) <br> - Réaliser le dosage anti-Xa <br> - Saisir les résultats dans le SIL <br> - Signaler les non-conformités ou résultats aberrants | - **Validation partagée** des tubes avec les biologistes <br> - **Saisie manuelle** des résultats → risque d'erreur <br> - **Maintenance des équipements** critique pour la fiabilité des analyses |
| **Pharmaciens hospitaliers** | Conseiller sur l'adaptation des anticoagulants | - Analyser les interactions médicamenteuses <br> - Proposer l'administration d'antidotes (ex. : andexanet alfa) <br> - Valider ou contester les recommandations des biologistes | - **Rôle consultatif** mais décisionnel en cas de divergence <br> - **Collaboration pluridisciplinaire** essentielle pour l'optimisation thérapeutique |
| **Personnel administratif** | Coordonner les flux logistiques | - Organiser les prélèvements et le transport des échantillons <br> - Suivre les délais de traitement <br> - Relancer les services en cas de retard ou non-conformité | - **Gestion des exceptions** (hors heures ouvrables, urgences) <br> - **Coordination avec le SIL** pour la visibilité en temps réel |
| **Patients** | Être informé et impliqué | - Donner son consentement éclairé <br> - Informer les cliniciens des effets indésirables <br> - Accéder aux résultats (via portail patient si disponible) | - **Accès sécurisé** aux résultats pour éviter l'anxiété <br> - **Consentement implicite** en cas d'urgence vitale |
| **Équipe informatique (DSI)** | Maintenir et faire évoluer le SIL | - Garantir la disponibilité 24/7 du SIL <br> - Intégrer les modules de priorisation, traçabilité et aide à l'interprétation <br> - Former les utilisateurs | - **Compatibilité technique** avec les systèmes existants (DPI, analyseurs) <br> - **Budget et délais** contraints pour le déploiement |
| **Autorités réglementaires** | Vérifier la conformité | - Auditer les processus et résultats <br> - Appliquer des sanctions en cas de non-conformité | - **Respect strict** des normes (ISO 15189, RGPD) <br> - **Traçabilité complète** obligatoire |
| **Comité de pilotage du projet SIL** | Superviser le projet | - Valider les priorités fonctionnelles <br> - Allouer les ressources nécessaires <br> - Suivre les délais et livrables | - **Alignement stratégique** avec les besoins métier <br> - **Arbitrer les compromis** entre sécurité, rapidité et coût |
| **Commission des Anti-infectieux et des Anticoagulants (CAI)** | Définir les protocoles | - Mettre à jour les protocoles locaux <br> - Former les équipes <br> - Auditer les pratiques | - **Protocoles à jour** et adaptés aux dernières recommandations <br> - **Flexibilité** pour gérer les exceptions cliniques |
| **Équipe de gestion des risques** | Identifier et atténuer les risques | - Analyser les risques cliniques, réglementaires et opérationnels <br> - Mettre en place des barrières de sécurité (alertes automatiques) | - **Priorisation des risques** pour une mitigation efficace <br> - **Collaboration avec la DSI** pour les aspects techniques |

---

### 2.2. Acteurs techniques

| **Acteur** | **Rôle principal** | **Responsabilités clés** | **Points de vigilance** |
|------------|-------------------|--------------------------|-------------------------|
| **Système d'Information de Laboratoire (SIL)** | Centraliser et automatiser le circuit | - Enregistrer les prescriptions électroniques <br> - Prioriser automatiquement les demandes <br> - Vérifier les conformités pré-analytiques <br> - Assurer la traçabilité et la sécurité des données <br> - Intégrer les données du DPI et des analyseurs | - **Priorisation automatique** basée sur des règles métiers validées <br> - **Vérification en temps réel** des non-conformités <br> - **Disponibilité 24/7** critique pour les urgences |
| **Dossier Patient Informatisé (DPI)** | Stocker et fournir les données patients | - Fournir les données médicales pertinentes (fonction rénale, traitements) au SIL <br> - Garantir l'intégrité et la confidentialité des données | - **Interopérabilité** avec le SIL (format des données, API) <br> - **Synchronisation en temps réel** des données |
| **Analyseurs de laboratoire** | Réaliser le dosage anti-Xa | - Effectuer le dosage avec précision <br> - Respecter les procédures analytiques <br> - Transmettre les résultats bruts au SIL | - **Intégration automatique** avec le SIL pour éviter les erreurs de saisie <br> - **Compatibilité technique** avec le SIL actuel |
| **Middleware de laboratoire** | Gérer les flux d'échantillons | - Router les échantillons vers les analyseurs <br> - Vérifier les conformités pré-analytiques <br> - Transmettre les résultats au SIL | - **Fonctionnalités déjà implémentées** vs. à ajouter <br> - **Compatibilité** avec le SIL et les analyseurs |
| **Systèmes d'alerte et de priorisation** | Classer les demandes et alerter | - Appliquer les règles de priorisation <br> - Envoyer des alertes aux acteurs concernés | - **Canaux d'alerte** (messagerie sécurisée, SMS, notification dans le SIL) <br> - **Règles de priorisation** claires et validées |

---

## 3. Décisions métier structurantes

### 3.1. Décisions clés par acteur

| **Acteur** | **Décision** | **Informations nécessaires** | **Informations produites** | **Dépendances** | **Risques en cas de non-respect** |
|------------|--------------|------------------------------|---------------------------|-----------------|-----------------------------------|
| **Cliniciens prescripteurs** | Prescrire un dosage anti-Xa en urgence | - Identité du patient <br> - Service prescripteur <br> - Contexte clinique (ex. : hémorragie active) <br> - Protocoles locaux ou recommandations HAS/ANSM <br> - Historique du patient (traitements en cours) | - Prescription électronique (ou papier) <br> - Statut de la demande : "en attente" <br> - Données contextuelles saisies | - Disponibilité du SIL <br> - Accès aux données du DPI | - Perte de traçabilité <br> - Erreur de transcription <br> - Non-respect des protocoles |
| **Cliniciens prescripteurs** | Classer manuellement une demande par niveau d'urgence | - Critères de priorisation (ex. : hémorragie active = urgence absolue) <br> - Données cliniques du patient <br> - Protocoles locaux | - Niveau de priorité attribué (ex. : "urgence absolue") <br> - Alerte au SIL ou au laboratoire si nécessaire | - Absence de priorisation automatique dans le SIL | - Retard dans les cas critiques <br> - Surcharge du laboratoire <br> - Frustration des cliniciens |
| **Biologistes médicaux** | Valider ou rejeter une demande de dosage | - Demande reçue dans le SIL <br> - Données contextuelles complètes <br> - Protocoles locaux | - Statut de la demande : "validée" ou "rejetée" <br> - Justification du rejet (si applicable) | - Données contextuelles complètes <br> - Respect des protocoles | - Analyse non pertinente → résultat inutilisable <br> - Retard dans la prise en charge |
| **Biologistes médicaux** | Prioriser une analyse | - Niveau d'urgence clinique <br> - Délais critiques <br> - Disponibilité des ressources | - Niveau de priorité attribué (ex. : "urgence absolue") <br> - Ordonnancement des analyses | - Règles de priorisation validées <br> - Disponibilité des techniciens et analyseurs | - Retard dans les cas critiques <br> - Surcharge du laboratoire |
| **Biologistes médicaux** | Interpréter un résultat de dosage anti-Xa | - Résultat brut du dosage <br> - Type d'AOD et posologie <br> - Heure de la dernière prise <br> - Fonction rénale (clairance de la créatinine) <br> - Contexte clinique <br> - Recommandations de la CAI | - Compte-rendu d'interprétation <br> - Recommandations thérapeutiques (ex. : adaptation de la posologie, arrêt temporaire du traitement) <br> - Seuil d'alerte si applicable | - Données contextuelles complètes <br> - Grille d'interprétation validée | - Interprétation erronée → erreur thérapeutique <br> - Risque clinique pour le patient |
| **Techniciens de laboratoire** | Valider la conformité d'un tube | - Type de tube (citraté 3.2%) <br> - Volume minimal requis <br> - Délai maximal entre prélèvement et analyse <br> - Conditions de transport (température, protection de la lumière) | - Statut de conformité : "conforme" ou "non conforme" <br> - Alerte au biologiste si non conforme | - Critères de conformité validés <br> - Formation des techniciens | - Analyse d'un échantillon non conforme → résultat invalide <br> - Retard dans la prise en charge |
| **Techniciens de laboratoire** | Signaler une non-conformité ou un résultat aberrant | - Détection d'une non-conformité ou d'un résultat aberrant <br> - Procédure de gestion des non-conformités | - Alerte au biologiste <br> - Demande de complément (nouveau prélèvement) si nécessaire <br> - Archivage de l'échantillon non conforme | - Procédure formalisée <br> - Canaux de communication clairs | - Perte de temps et de ressources <br> - Risque de surcharge du laboratoire |
| **Pharmaciens hospitaliers** | Proposer l'administration d'un antidote | - Résultats du dosage anti-Xa <br> - Données d'interactions médicamenteuses <br> - Protocoles locaux de gestion des urgences hémorragiques | - Recommandation d'administration d'antidote (ex. : andexanet alfa) <br> - Justification clinique | - Collaboration avec les biologistes <br> - Accès aux données patients | - Retard dans l'administration de l'antidote → risque vital <br> - Erreur d'administration |
| **Personnel administratif** | Relancer un service en cas de retard ou non-conformité | - Statut des prélèvements (en attente, en cours, terminés) <br> - Alertes de non-conformité ou de retard | - Relance du service prescripteur <br> - Mise à jour du statut dans le SIL | - Visibilité en temps réel des statuts <br> - Procédure de relance formalisée | - Retard dans la prise en charge <br> - Aggravation de l'état clinique du patient |

---

### 3.2. Enchaînements obligatoires

| **Processus** | **Étapes obligatoires** | **Acteurs impliqués** | **Dépendances** | **Risques en cas d'écart** |
|---------------|-------------------------|-----------------------|-----------------|----------------------------|
| **Prescription → Analyse** | 1. Prescription électronique dans le SIL <br> 2. Validation biologique de la demande <br> 3. Vérification de la conformité des tubes <br> 4. Réalisation du dosage anti-Xa | Cliniciens, Biologistes, Techniciens de laboratoire | - Disponibilité du SIL <br> - Critères de conformité validés <br> - Intégration avec les analyseurs | - Perte de traçabilité <br> - Résultat invalide <br> - Retard dans la prise en charge |
| **Analyse → Interprétation** | 1. Transmission des résultats bruts au SIL <br> 2. Validation des résultats par le biologiste <br> 3. Interprétation en contexte clinique <br> 4. Rédaction du compte-rendu d'interprétation | Techniciens de laboratoire, Biologistes | - Intégration automatique entre analyseurs et SIL <br> - Données contextuelles complètes <br> - Grille d'interprétation validée | - Erreur d'interprétation <br> - Recommandations thérapeutiques inadaptées |
| **Interprétation → Adaptation thérapeutique** | 1. Transmission des recommandations au clinicien <br> 2. Adaptation du traitement par le clinicien <br> 3. Collaboration avec le pharmacien si nécessaire | Biologistes, Cliniciens, Pharmaciens | - Communication efficace entre acteurs <br> - Accès aux données patients | - Retard dans l'adaptation thérapeutique <br> - Erreur d'adaptation |
| **Traçabilité** | 1. Enregistrement systématique de toutes les actions (prescription, validation, analyse, interprétation, transmission) <br> 2. Conservation des logs pendant 10 ans <br> 3. Signature électronique pour les résultats validés | SIL, Biologistes, Techniciens de laboratoire | - Fonctionnalités de traçabilité dans le SIL <br> - Respect des normes (ISO 15189, RGPD) | - Impossibilité de prouver la conformité en cas d'audit <br> - Sanctions réglementaires |

---

## 4. Informations clés manipulées

### 4.1. Données patients et cliniques

| **Catégorie** | **Données spécifiques** | **Source** | **Utilisation** | **Contraintes** |
|---------------|-------------------------|------------|-----------------|-----------------|
| **Identification** | - Identité du patient (nom, prénom, numéro de dossier) <br> - Service prescripteur | DPI, SIL | - Traçabilité <br> - Communication entre acteurs | - Respect du RGPD <br> - Accès sécurisé |
| **Traitement anticoagulant** | - Type d'AOD (apixaban, rivaroxaban, édoxaban) <br> - Posologie (dose et fréquence) <br> - Heure de la dernière prise | Prescription électronique, DPI | - Interprétation du dosage anti-Xa <br> - Adaptation thérapeutique | - Précision à la minute près <br> - Intégration automatique depuis le DPI |
| **Contexte clinique** | - Contexte clinique (hémorragie active, chirurgie en urgence, suspicion de surdosage) <br> - Autres traitements (antiagrégants, autres anticoagulants) | Prescription électronique, Cliniciens | - Priorisation des demandes <br> - Interprétation du résultat | - Saisie manuelle → risque d'erreur <br> - Intégration avec le DPI |
| **Fonction rénale** | - Clairance de la créatinine (formule CKD-EPI ou MDRD) <br> - Seuil critique : clairance < 30 mL/min | DPI | - Interprétation du dosage anti-Xa <br> - Adaptation posologique | - Formule de calcul validée <br> - Seuil critique à confirmer |
| **Résultats du dosage** | - Résultat brut du dosage anti-Xa <br> - Seuil d'alerte pour chaque AOD | Analyseurs, SIL | - Interprétation par le biologiste <br> - Recommandations thérapeutiques | - Intégration automatique entre analyseurs et SIL <br> - Grille d'interprétation validée |

---

### 4.2. Données de gestion et logistiques

| **Catégorie** | **Données spécifiques** | **Source** | **Utilisation** | **Contraintes** |
|---------------|-------------------------|------------|-----------------|-----------------|
| **Prescription** | - Date et heure de la prescription <br> - Niveau de priorité attribué <br> - Statut de la demande (en attente, validée, rejetée) | SIL | - Traçabilité <br> - Priorisation des analyses <br> - Communication entre acteurs | - Enregistrement systématique <br> - Respect des délais critiques |
| **Conformité des tubes** | - Type de tube (citraté 3.2%) <br> - Volume minimal requis <br> - Délai maximal entre prélèvement et analyse <br> - Conditions de transport (température, protection de la lumière) <br> - Statut de conformité | Techniciens de laboratoire, SIL | - Validation avant analyse <br> - Rejet des échantillons non conformes | - Critères de conformité validés <br> - Vérification en temps réel |
| **Traçabilité** | - Identité de l'utilisateur ayant effectué l'action <br> - Horodatage de chaque action <br> - Type d'action (création, modification, validation) <br> - Résultat final et recommandations | SIL, Biologistes, Techniciens de laboratoire | - Preuve de conformité <br> - Audit interne/extern