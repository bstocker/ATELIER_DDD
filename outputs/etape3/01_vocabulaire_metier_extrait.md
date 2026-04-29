# **Vocabulaire métier extrait**
**Domaine** : Gestion des demandes urgentes de dosage anti-Xa dans le SIL
**Version** : 1.0
**Date** : [À compléter]
**Auteurs** : Analyste DDD
**Sources** : Livrables étapes 1 et 2 (01_reformulation_du_besoin.md, 02_acteurs_du_domaine.md, 03_concepts_metier_initiaux.md, 04_contraintes_et_risques.md, 05_vision_globale_du_domaine.md, 01_cartographie_acteurs_responsabilites.md, 02_attentes_objectifs_acteurs.md, 03_decisions_informations_manipulees.md, 04_regles_metier.md, 05_priorites_exceptions_contraintes.md, 06_conflits_objectifs_arbitrages.md, 07_base_modelisation_comportementale.md)

---

## **1. Liste des termes métier identifiés**

### **1.1. Acteurs humains et organisationnels**

| **Terme** | **Type** | **Source principale** | **Définition** | **Statut** |
|-----------|----------|-----------------------|----------------|------------|
| **Cliniciens prescripteurs** | Acteur | 02_acteurs_du_domaine.md | Professionnels de santé (urgentistes, réanimateurs, chirurgiens) qui prescrivent un dosage anti-Xa en urgence pour les patients sous AOD. Ils évaluent le contexte clinique, saisissent les données contextuelles et adaptent le traitement en fonction des résultats. | **Validé** |
| **Biologistes médicaux** | Acteur | 02_acteurs_du_domaine.md | Professionnels de santé responsables de la validation des demandes de dosage anti-Xa, de la priorisation des analyses, de l’interprétation des résultats et de la rédaction de recommandations thérapeutiques. Ils garantissent la qualité et la fiabilité des résultats. | **Validé** |
| **Techniciens de laboratoire** | Acteur | 02_acteurs_du_domaine.md | Professionnels qui préparent et analysent les échantillons biologiques, vérifient la conformité des tubes, réalisent le dosage anti-Xa et saisissent les résultats dans le SIL. Ils signalent les non-conformités ou résultats aberrants. | **Validé** |
| **Pharmaciens hospitaliers** | Acteur | 02_acteurs_du_domaine.md | Professionnels qui conseillent les cliniciens sur le choix et l’adaptation des anticoagulants, analysent les interactions médicamenteuses et participent à la gestion des urgences hémorragiques (ex. : administration d’antidotes). | **Validé** |
| **Personnel administratif / Coordinateurs de soins** | Acteur | 02_acteurs_du_domaine.md | Professionnels qui gèrent les flux de demandes entre les services et le laboratoire, coordonnent les prélèvements et le transport des échantillons, et suivent les délais de traitement. | **Validé** |
| **Patients** | Acteur | 02_acteurs_du_domaine.md | Personnes sous AOD pour lesquelles un dosage anti-Xa est prescrit. Ils doivent être informés des résultats, donner leur consentement éclairé (si applicable) et signaler les effets indésirables aux cliniciens. | **Validé** |
| **Équipe informatique (DSI)** | Acteur | 02_acteurs_du_domaine.md | Équipe responsable de la maintenance et de l’évolution du SIL pour répondre aux besoins du circuit des demandes urgentes. Elle garantit la sécurité, la disponibilité et l’interopérabilité du système. | **Validé** |
| **Autorités réglementaires** | Acteur | 02_acteurs_du_domaine.md | Organismes (HAS, ANSM, ARS, CNIL) qui vérifient la conformité du circuit avec les bonnes pratiques et les normes (ex. : ISO 15189, RGPD). Ils auditent les processus et peuvent sanctionner les non-conformités. | **Validé** |
| **Comité de pilotage du projet SIL** | Acteur organisationnel | 02_acteurs_du_domaine.md | Instance qui supervise l’évolution du SIL pour intégrer le circuit des demandes urgentes de dosage anti-Xa. Elle valide les priorités fonctionnelles et alloue les ressources nécessaires. | **Validé** |
| **Commission des Anti-infectieux et des Anticoagulants (CAI)** | Acteur organisationnel | 02_acteurs_du_domaine.md | Commission qui définit les protocoles locaux pour la prescription, l’analyse et l’interprétation des dosages anti-Xa. Elle met à jour les recommandations en fonction des données scientifiques et forme les équipes. | **Validé** |
| **Équipe de gestion des risques** | Acteur organisationnel | 02_acteurs_du_domaine.md | Équipe qui identifie et atténue les risques liés au circuit (ex. : erreurs de dosage, retards). Elle met en place des barrières de sécurité (ex. : alertes automatiques) et audite les processus. | **Validé** |

---

### **1.2. Acteurs techniques**

| **Terme** | **Type** | **Source principale** | **Définition** | **Statut** |
|-----------|----------|-----------------------|----------------|------------|
| **Système d'Information de Laboratoire (SIL)** | Acteur technique | 02_acteurs_du_domaine.md | Outil informatique centralisant la gestion des demandes de dosage, des résultats et des données contextuelles. Il automatise la priorisation, vérifie les conformités pré-analytiques, assure la traçabilité et la sécurité des données. | **Validé** |
| **Dossier Patient Informatisé (DPI)** | Acteur technique | 02_acteurs_du_domaine.md | Système informatisé stockant les données médicales du patient, incluant les traitements en cours, les résultats d’examens et la fonction rénale. Il fournit ces données au SIL pour l’interprétation des résultats. | **Validé** |
| **Analyseurs de laboratoire** | Acteur technique | 02_acteurs_du_domaine.md | Équipements automatisés (ex. : ACL TOP, STA R Max) qui réalisent le dosage anti-Xa sur les échantillons biologiques. Ils transmettent les résultats bruts au SIL. | **Validé** |
| **Middleware de laboratoire** | Acteur technique | 02_acteurs_du_domaine.md | Logiciel intermédiaire qui gère les flux d’échantillons entre les services, le laboratoire et les analyseurs. Il vérifie les conformités pré-analytiques, route les échantillons et transmet les résultats au SIL. | **Validé** |
| **Systèmes d'alerte et de priorisation** | Acteur technique | 02_acteurs_du_domaine.md | Modules du SIL qui classent automatiquement les demandes par niveau d’urgence et envoient des alertes aux acteurs concernés en cas de criticité (ex. : non-conformité des tubes, retard). | **Validé** |

---

### **1.3. Concepts métier centraux**

| **Terme** | **Type** | **Source principale** | **Définition** | **Statut** |
|-----------|----------|-----------------------|----------------|------------|
| **Anticoagulant Oral Direct (AOD)** | Concept | 03_concepts_metier_initiaux.md | Classe de médicaments anticoagulants administrés par voie orale, utilisés pour prévenir ou traiter les événements thromboemboliques. Les AOD concernés par le dosage anti-Xa incluent l’apixaban, le rivaroxaban et l’édoxaban (à confirmer). | **Validé** |
| **Dosage anti-Xa** | Concept | 03_concepts_metier_initiaux.md | Analyse biologique mesurant l’activité anticoagulante des AOD en évaluant l’inhibition du facteur Xa (enzyme clé de la coagulation). Il est utilisé pour évaluer l’efficacité et la sécurité du traitement anticoagulant, notamment en situation d’urgence. | **Validé** |
| **Demande urgente de dosage anti-Xa** | Concept | 03_concepts_metier_initiaux.md | Prescription médicale prioritaire de dosage anti-Xa pour un patient sous AOD, nécessitant une prise en charge immédiate en raison de la criticité clinique (ex. : hémorragie active, chirurgie en urgence). | **Validé** |
| **Prescription électronique** | Concept | 03_concepts_metier_initiaux.md | Acte médical formalisé via un système informatisé (ex. : SIL, DPI) pour demander un dosage anti-Xa. Elle inclut l’identité du patient, le service prescripteur, le type d’AOD, la posologie, l’heure de la dernière prise et le contexte clinique. | **Validé** |
| **Échantillon biologique (Tube)** | Concept | 03_concepts_metier_initiaux.md | Prélèvement sanguin destiné à l’analyse du dosage anti-Xa, soumis à des exigences pré-analytiques strictes (type de tube, volume, délai de transport, conditions de transport). | **Validé** |
| **Exigences pré-analytiques** | Concept | 03_concepts_metier_initiaux.md | Ensemble de conditions à respecter pour garantir la validité de l’échantillon avant analyse (ex. : type de tube citraté 3.2%, volume minimal, délai maximal entre prélèvement et analyse, température de transport). | **Validé** |
| **Priorisation des demandes** | Concept | 03_concepts_metier_initiaux.md | Classement automatique ou manuel des demandes de dosage anti-Xa en fonction de leur urgence clinique (ex. : hémorragie active = priorité absolue, chirurgie programmée = priorité haute). | **Validé** |
| **Contexte clinique** | Concept | 03_concepts_metier_initiaux.md | Ensemble des informations médicales et thérapeutiques nécessaires à l’interprétation du dosage anti-Xa (ex. : type d’AOD, posologie, heure de la dernière prise, fonction rénale, autres traitements anticoagulants, contexte clinique comme une hémorragie active). | **Validé** |
| **Fonction rénale** | Concept | 03_concepts_metier_initiaux.md | Capacité des reins à filtrer le sang, évaluée par la clairance de la créatinine (formule CKD-EPI ou MDRD). Elle impacte l’élimination des AOD et donc leur activité anticoagulante. Un seuil critique est souvent une clairance < 30 mL/min. | **Validé** |
| **Interprétation du dosage anti-Xa** | Concept | 03_concepts_metier_initiaux.md | Analyse des résultats du dosage en fonction du contexte clinique pour évaluer l’efficacité et la sécurité du traitement anticoagulant. Elle aboutit à un compte-rendu d’interprétation avec des recommandations thérapeutiques (ex. : adaptation de la posologie, arrêt temporaire du traitement). | **Validé** |
| **Traçabilité** | Concept | 03_concepts_metier_initiaux.md | Enregistrement systématique de toutes les étapes du circuit des demandes urgentes de dosage anti-Xa, depuis la prescription jusqu’à l’archivage. Elle permet les audits, l’amélioration des processus et garantit la sécurité. | **Validé** |
| **Sécurité des données** | Concept | 03_concepts_metier_initiaux.md | Ensemble des mesures techniques et organisationnelles pour protéger la confidentialité, l’intégrité et la disponibilité des données du circuit (ex. : authentification forte, droits d’accès différenciés, chiffrement, audit trail). | **Validé** |
| **Protocole local** | Concept | 03_concepts_metier_initiaux.md | Document définissant les bonnes pratiques pour la prescription, l’analyse et l’interprétation des dosages anti-Xa dans l’établissement. Il est mis à jour par la CAI en fonction des recommandations HAS/ANSM. | **Validé** |
| **Audit trail** | Concept | 03_concepts_metier_initiaux.md | Journal électronique enregistrant toutes les actions effectuées sur une demande de dosage, depuis la prescription jusqu’à l’archivage. Il inclut l’identifiant de l’utilisateur, l’horodatage et le type d’action. | **Validé** |
| **Non-conformité des tubes** | Concept | 03_concepts_metier_initiaux.md | Situation où un échantillon biologique ne respecte pas les exigences pré-analytiques requises pour le dosage anti-Xa (ex. : type de tube incorrect, volume insuffisant, délai de transport dépassé). | **Validé** |
| **Astreinte biologique** | Concept | 03_concepts_metier_initiaux.md | Organisation permettant la prise en charge des demandes urgentes en dehors des heures ouvrables (nuit, week-end, jours fériés). Un biologiste d’astreinte valide les résultats et émet des recommandations. | **Validé** |
| **Recommandations thérapeutiques** | Concept | 03_concepts_metier_initiaux.md | Conseils émis par le biologiste après interprétation du dosage anti-Xa, visant à adapter le traitement anticoagulant (ex. : adaptation de la posologie, arrêt temporaire du traitement, administration d’un antidote comme l’andexanet alfa). | **Validé** |
| **Collaboration pluridisciplinaire** | Concept | 03_concepts_metier_initiaux.md | Travail coordonné entre cliniciens, biologistes, pharmaciens et personnel administratif pour la prise en charge des patients sous AOD. Elle implique la transmission des informations et la prise de décision conjointe. | **Validé** |
| **Conformité réglementaire** | Concept | 03_concepts_metier_initiaux.md | Respect des normes et bonnes pratiques en vigueur pour la réalisation et l’interprétation des dosages anti-Xa (ex. : ISO 15189, RGPD, recommandations HAS/ANSM). | **Validé** |
| **Délai critique** | Concept | 03_concepts_metier_initiaux.md | Fenêtre de temps maximale acceptable entre la prescription et la transmission des résultats pour une prise en charge thérapeutique optimale. Exemples : 1 heure pour une hémorragie active, 4 heures pour une chirurgie programmée. | **Validé** |
| **Portail patient** | Concept | 03_concepts_metier_initiaux.md | Interface permettant aux patients d’accéder à leurs résultats d’examens et aux informations associées (ex. : recommandations thérapeutiques). Elle respecte le RGPD (authentification forte, consentement éclairé). | **Validé** |

---

### **1.4. Informations manipulées**

| **Terme** | **Type** | **Source principale** | **Définition** | **Statut** |
|-----------|----------|-----------------------|----------------|------------|
| **Identité du patient** | Information | 03_decisions_informations_manipulees.md | Données d’identification du patient (nom, prénom, numéro de dossier) utilisées pour la traçabilité et la communication entre acteurs. | **Validé** |
| **Service prescripteur** | Information | 03_decisions_informations_manipulees.md | Service médical (urgences, réanimation, bloc opératoire) ayant prescrit le dosage anti-Xa. | **Validé** |
| **Type d’AOD** | Information | 03_decisions_informations_manipulees.md | Type d’anticoagulant oral direct prescrit (apixaban, rivaroxaban, édoxaban). | **Validé** |
| **Posologie** | Information | 03_decisions_informations_manipulees.md | Dose et fréquence d’administration de l’AOD. | **Validé** |
| **Heure de la dernière prise** | Information | 03_decisions_informations_manipulees.md | Heure à laquelle le patient a pris son dernier comprimé d’AOD. La précision requise est à la minute près (ex. : "14h30"). | **Validé** |
| **Fonction rénale (clairance de la créatinine)** | Information | 03_decisions_informations_manipulees.md | Valeur de la clairance de la créatinine (formule CKD-EPI ou MDRD) utilisée pour évaluer l’élimination des AOD et adapter l’interprétation du dosage. | **Validé** |
| **Contexte clinique** | Information | 03_decisions_informations_manipulees.md | Contexte médical du patient justifiant le dosage (ex. : hémorragie active, chirurgie en urgence, suspicion de surdosage). | **Validé** |
| **Autres traitements** | Information | 03_decisions_informations_manipulees.md | Autres médicaments pris par le patient (ex. : antiagrégants plaquettaires, autres anticoagulants) pouvant interagir avec les AOD. | **Validé** |
| **Résultat brut du dosage anti-Xa** | Information | 03_decisions_informations_manipulees.md | Valeur numérique brute obtenue après analyse de l’échantillon (ex. : 0.8 UI/mL). | **Validé** |
| **Seuil d’alerte** | Information | 03_decisions_informations_manipulees.md | Valeur seuil du dosage anti-Xa au-delà de laquelle une alerte est déclenchée (ex. : > 1.5 UI/mL pour l’apixaban en cas d’insuffisance rénale). | **Validé** |
| **Compte-rendu d’interprétation** | Information | 03_decisions_informations_manipulees.md | Document rédigé par le biologiste après interprétation du résultat, incluant une analyse contextuelle et des recommandations thérapeutiques. | **Validé** |
| **Statut de la demande** | Information | 03_decisions_informations_manipulees.md | État de la demande dans le SIL (ex. : "en attente", "validée", "rejetée", "en cours d’analyse", "terminée"). | **Validé** |
| **Niveau de priorité** | Information | 03_decisions_informations_manipulees.md | Niveau d’urgence attribué à une demande (ex. : "urgence absolue", "urgence haute", "urgence modérée", "routine"). | **Validé** |
| **Statut de conformité des tubes** | Information | 03_decisions_informations_manipulees.md | Résultat de la vérification des exigences pré-analytiques (ex. : "conforme", "non conforme : volume insuffisant", "non conforme : délai de transport dépassé"). | **Validé** |
| **Logs d’audit (audit trail)** | Information | 03_decisions_informations_manipulees.md | Enregistrement systématique de toutes les actions effectuées sur une demande (ex. : prescription, validation, analyse, interprétation, transmission), incluant l’identifiant de l’utilisateur et l’horodatage. | **Validé** |
| **Recommandations thérapeutiques** | Information | 03_decisions_informations_manipulees.md | Conseils émis par le biologiste pour adapter le traitement (ex. : "réduire la posologie de 50%", "arrêter temporairement l’AOD", "administrer 10 mg d’andexanet alfa"). | **Validé** |

---
### **1.5. Décisions métier**

| **Terme** | **Type** | **Source principale** | **Définition** | **Statut** |
|-----------|----------|-----------------------|----------------|------------|
| **Prescrire un dosage anti-Xa en urgence** | Décision | 03_decisions_informations_manipulees.md | Décision du clinicien de prescrire un dosage anti-Xa pour un patient sous AOD, basée sur l’évaluation du contexte clinique et le respect des protocoles locaux. | **Validé** |
| **Classer manuellement une demande par niveau d’urgence** | Décision | 03_decisions_informations_manipulees.md | Décision du clinicien d’attribuer un niveau de priorité à une demande si le SIL ne le fait pas automatiquement (ex. : "urgence absolue" pour une hémorragie active). | **Validé** |
| **Valider ou rejeter une demande de dosage** | Décision | 03_decisions_informations_manipulees.md | Décision du biologiste de valider une demande (si conforme aux protocoles) ou de la rejeter (si non conforme ou inappropriée), avec justification. | **Validé** |
| **Prioriser une analyse** | Décision | 03_decisions_informations_manipulees.md | Décision du biologiste de classer les demandes par ordre d’urgence en fonction des critères cliniques et des délais critiques. | **Validé** |
| **Interpréter un résultat de dosage anti-Xa** | Décision | 03_decisions_informations_manipulees.md | Décision du biologiste d’analyser le résultat du dosage en fonction du contexte clinique (type d’AOD, fonction rénale, heure de la dernière prise) et d’émettre un compte-rendu d’interprétation avec des recommandations thérapeutiques. | **Validé** |
| **Valider la conformité d’un tube** | Décision | 03_decisions_informations_manipulees.md | Décision du technicien de laboratoire (ou du système automatisé) de valider ou rejeter un tube en fonction des exigences pré-analytiques (type, volume, délai de transport). | **Validé** |
| **Signaler une non-conformité ou un résultat aberrant** | Décision | 03_decisions_informations_manipulees.md | Décision du technicien de laboratoire d’alerter le biologiste en cas de non-conformité des tubes ou de résultat aberrant, avec demande de complément si nécessaire. | **Validé** |
| **Proposer l’administration d’un antidote** | Décision | 03_decisions_informations_manipulees.md | Décision du pharmacien (en collaboration avec le biologiste) de proposer l’administration d’un antidote (ex. : andexanet alfa) en cas de surdosage ou d’hémorragie active. | **Validé** |
| **Adapter le traitement anticoagulant** | Décision | 03_decisions_informations_manipulees.md | Décision du clinicien (en collaboration avec le pharmacien et le biologiste) d’adapter la posologie de l’AOD ou d’arrêter temporairement le traitement en fonction des résultats et des recommandations. | **Validé** |
| **Relancer un service en cas de retard ou non-conformité** | Décision | 03_decisions_informations_manipulees.md | Décision du personnel administratif de relancer un service prescripteur en cas de retard dans le prélèvement ou de non-conformité des tubes. | **Validé** |

---
### **1.6. Règles métier**

| **Terme** | **Type** | **Source principale** | **Définition** | **Statut** |
|-----------|----------|-----------------------|----------------|------------|
| **Prescription électronique obligatoire** | Règle | 04_regles_metier.md | Toute demande de dosage anti-Xa doit être formalisée via une prescription électronique dans le SIL. | **Validé** |
| **Respect des protocoles locaux** | Règle | 04_regles_metier.md | La prescription doit respecter les indications définies par les protocoles de la CAI et les recommandations HAS/ANSM. | **Validé** |
| **Validation biologique obligatoire** | Règle | 04_regles_metier.md | Toute demande de dosage anti-Xa doit être validée par un biologiste avant analyse. | **Validé** |
| **Rejet des demandes non conformes** | Règle | 04_regles_metier.md | Les demandes ne respectant pas les protocoles ou les critères cliniques doivent être rejetées avec justification. | **Validé** |
| **Priorisation automatique des demandes** | Règle | 04_regles_metier.md | Le SIL doit classer automatiquement les demandes par niveau d’urgence en fonction de règles métiers prédéfinies (ex. : hémorragie active = priorité absolue). | **Validé** |
| **Vérification automatique des conformités pré-analytiques** | Règle | 04_regles_metier.md | Le SIL ou le middleware doit alerter en temps réel si un tube est non conforme (type incorrect, volume insuffisant, délai de transport dépassé). | **Validé** |
| **Intégration automatique des résultats des analyseurs** | Règle | 04_regles_metier.md | Les résultats bruts des analyseurs doivent être transmis automatiquement au SIL pour éviter les erreurs de saisie. | **Validé** |
| **Traçabilité complète obligatoire** | Règle | 04_regles_metier.md | Toutes les actions (prescription, validation, analyse, interprétation, transmission) doivent être enregistrées dans un audit trail avec horodatage et identifiant de l’utilisateur. | **Validé** |
| **Signature électronique pour les résultats validés** | Règle | 04_regles_metier.md | Les résultats validés par le biologiste doivent être signés électroniquement pour garantir la non-répudiation. | **Validé** |
| **Accès sécurisé aux données** | Règle | 04_regles_metier.md | Les données du circuit doivent être protégées par une authentification forte et des droits d’accès différenciés. | **Validé** |
| **Conservation des logs pendant 10 ans** | Règle | 04_regles_metier.md | Les logs d’audit doivent être conservés pendant au moins 10 ans pour répondre aux exigences réglementaires (ISO 15189, RGPD). | **Validé** |
| **Disponibilité 24/7 du SIL** | Règle | 04_contraintes_et_risques.md | Le SIL doit être opérationnel en permanence pour gérer les demandes urgentes, y compris en dehors des heures ouvrables. | **Validé** |
| **Respect des délais critiques** | Règle | 04_contraintes_et_risques.md | Les délais entre la prescription et la transmission des résultats doivent être respectés (ex. : ≤ 1 heure pour une hémorragie active). | **Validé** |

---
### **1.7. Événements et processus**

| **Terme** | **Type** | **Source principale** | **Définition** | **Statut** |
|-----------|----------|-----------------------|----------------|------------|
| **Prescription d’un dosage anti-Xa** | Événement | 05_vision_globale_du_domaine.md | Acte médical déclenchant le circuit des demandes urgentes de dosage anti-Xa. | **Validé** |
| **Validation de la demande** | Événement | 05_vision_globale_du_domaine.md | Validation par le biologiste de la pertinence clinique de la demande. | **Validé** |
| **Prélèvement sanguin** | Événement | 05_vision_globale_du_domaine.md | Réalisation du prélèvement dans un tube citraté 3.2% par le personnel soignant. | **Validé** |
| **Transport de l’échantillon** | Événement | 05_vision_globale_du_domaine.md | Acheminement rapide de l’échantillon vers le laboratoire, dans des conditions de température contrôlées. | **Validé** |
| **Vérification de la conformité des tubes** | Événement | 05_vision_globale_du_domaine.md | Contrôle par le technicien de laboratoire du type de tube, du volume et du délai de transport. | **Validé** |
| **Réalisation du dosage anti-Xa** | Événement | 05_vision_globale_du_domaine.md | Analyse de l’échantillon sur un analyseur automatisé. | **Validé** |
| **Transmission des résultats bruts** | Événement | 05_vision_globale_du_domaine.md | Envoi automatique ou manuel des résultats bruts au SIL. | **Validé** |
| **Interprétation des résultats** | Événement | 05_vision_globale_du_domaine.md | Analyse des résultats par le biologiste en contexte clinique, avec émission d’un compte-rendu d’interprétation. | **Validé** |
| **Transmission des recommandations** | Événement | 05_vision_globale_du_domaine.md | Communication des recommandations thérapeutiques au clinicien. | **Validé** |
| **Adaptation du traitement** | Événement | 05_vision_globale_du_domaine.md | Modification de la posologie de l’AOD ou administration d’un antidote par le clinicien. | **Validé** |
| **Archivage des données** | Événement | 05_vision_globale_du_domaine.md | Conservation des logs et des résultats pendant 10 ans pour les audits. | **Validé** |

---
### **1.8. Contraintes**

| **Terme** | **Type** | **Source principale** | **Définition** | **Statut** |
|-----------|----------|-----------------------|----------------|------------|
| **Délais critiques** | Contrainte | 04_contraintes_et_risques.md | Fenêtres de temps maximales acceptables entre la prescription et la transmission des résultats pour éviter les complications cliniques (ex. : ≤ 1 heure pour une hémorragie active). | **Validé** |
| **Disponibilité 24/7 du SIL** | Contrainte | 04_contraintes_et_risques.md | Le SIL doit être opérationnel en permanence pour gérer les demandes urgentes, y compris en dehors des heures ouvrables. | **Validé** |
| **Exigences pré-analytiques strictes** | Contrainte | 04_contraintes_et_risques.md | Les tubes doivent respecter des critères précis (type citraté 3.2%, volume minimal, délai maximal entre prélèvement et analyse) pour garantir la validité du dosage. | **Validé** |
| **Traçabilité complète** | Contrainte | 04_contraintes_et_risques.md | Toutes les actions doivent être enregistrées dans un audit trail avec horodatage et identifiant de l’utilisateur. | **Validé** |
| **Sécurité des données** | Contrainte | 04_contraintes_et_risques.md | Les données doivent être protégées par une authentification forte, des droits d’accès différenciés et un chiffrement. | **Validé** |
| **Respect des normes réglementaires** | Contrainte | 04_contraintes_et_risques.md | Le circuit doit respecter les normes ISO 15189, RGPD et les recommandations HAS/ANSM. | **Validé** |
| **Gestion des astreintes** | Contrainte | 04_contraintes_et_risques.md | Organisation permettant la prise en charge des demandes urgentes en dehors des heures ouvrables (nuit, week-end, jours fériés). | **Validé** |
| **Collaboration pluridisciplinaire** | Contrainte | 02_acteurs_du_domaine.md | Travail coordonné entre cliniciens, biologistes, pharmaciens et personnel administratif pour une prise en charge optimale. | **Validé** |

---
## **2. Termes importants mais insuffisamment définis**

Les termes suivants sont **critiques pour le domaine**, mais leur définition ou leur portée nécessite une **clarification avec les experts métier** :

| **Terme** | **Type** | **Source principale** | **Problème identifié** | **Questions à poser** |
|-----------|----------|-----------------------|-------------------------|-----------------------|
| **Critères de priorisation** | Règle | 04_regles_metier.md, 05_priorites_exceptions_contraintes.md | Les critères exacts pour classer une demande en "urgence absolue", "urgence haute", ou "routine" ne sont pas détaillés. Exemples : quels seuils cliniques déclenchent une priorité absolue ? | - Quels sont les **critères exacts** pour classer une demande en "urgence absolue" ? <br> - Quels sont les **délais maximaux** acceptables pour chaque niveau de priorité ? <br> - Comment gérer les **conflits de priorité** (ex. : deux urgences absolues simultanées) ? |
| **Grille d’interprétation** | Règle | 04_regles_metier.md | Les seuils d’interprétation pour chaque AOD (apixaban, rivaroxaban, édoxaban) en fonction du contexte clinique ne sont pas précisés. | - Quels sont les **seuils exacts** pour chaque AOD ? <br> - Comment interpréter un résultat en fonction de la **fonction rénale** ? <br> - Quels sont les **recommandations thérapeutiques** associées à chaque seuil ? |
| **Critères de conformité des tubes** | Règle | 04_regles_metier.md | Les exigences précises pour les tubes (type, volume, délai de transport) ne sont pas détaillées. | - Quel est le **type de tube exact** requis (ex. : citraté 3.2%) ? <br> - Quel est le **volume minimal** requis ? <br> - Quel est le **délai maximal** entre prélèvement et analyse ? <br> - Quelles sont les **conditions de transport** (température, protection de la lumière) ? |
| **Procédure de gestion des non-conformités** | Règle | 04_regles_metier.md | La procédure à suivre en cas de non-conformité des tubes (refus, demande de complément, escalade) n’est pas formalisée. | - Que faire en cas de **non-conformité des tubes** ? <br> - Qui valide définitivement la conformité : clinicien, technicien, biologiste ou système automatisé ? <br> - Comment gérer les **échantillons non conformes en dehors des heures ouvrables** ? |
| **Données contextuelles à collecter** | Information | 03_decisions_informations_manipulees.md | La liste exhaustive des données contextuelles nécessaires à l’interprétation n’est pas clairement définie. | - Quelles sont les **données contextuelles obligatoires** ? <br> - Comment sont-elles **saisies** (manuellement ou automatiquement depuis le DPI) ? <br> - Quels **champs sont obligatoires** dans la prescription ? |
| **Intégration avec le DPI** | Contrainte | 05_vision_globale_du_domaine.md | La méthode d’intégration entre le SIL et le DPI (format des données, API) n’est pas précisée. | - Quelles **données du DPI** sont nécessaires au SIL ? <br> - Quel est le **format des données** échangées ? <br> - Existe-t-il une **API ou un connecteur** pour l’intégration ? |
| **Portail patient** | Concept | 03_concepts_metier_initiaux.md | Les fonctionnalités exactes du portail patient (données accessibles, processus de consentement) ne sont pas détaillées. | - Quelles **données** seront accessibles aux patients ? <br> - Comment sera géré le **consentement éclairé** ? <br> - Qui valide le **contenu du portail** ? |
| **Astreinte biologique** | Concept | 03_concepts_metier_initiaux.md | Les services couverts par l’astreinte et la procédure de déclenchement ne sont pas formalisés. | - Quels sont les **services couverts** par l’astreinte ? <br> - Quelle est la **procédure de déclenchement** de l’astreinte ? <br> - Qui valide les résultats **en dehors des heures ouvrables** ? |
| **Recommandations thérapeutiques** | Information | 03_decisions_informations_manipulees.md | Les recommandations exactes à émettre par le biologiste en fonction des résultats ne sont pas précisées. | - Quelles sont les **recommandations thérapeutiques** pour chaque AOD et chaque contexte clinique ? <br> - Qui valide les recommandations : pharmacien, clinicien ou système automatisé ? |
| **Normes réglementaires** | Contrainte | 04_contraintes_et_risques.md | Les normes exactes à respecter (ISO 15189, RGPD) et leur interprétation pour le circuit ne sont pas détaillées. | - Quelles sont les **normes exactes** à respecter ? <br> - Quelle est la **durée de conservation** des logs d’audit ? <br> - Faut-il prévoir une **signature électronique** pour les résultats ? |
| **Budget et planning** | Contrainte | 05_vision_globale_du_domaine.md | Le budget alloué et les délais impartis pour le projet ne sont pas précisés. | - Quel est le **budget disponible** pour le projet ? <br> - Quels sont les **délais impartis** pour la mise en place du nouveau circuit ? |
| **Compatibilité du SIL actuel** | Contrainte | 01_reformulation_du_besoin.md | La capacité du SIL actuel à intégrer les nouvelles fonctionnalités n’est pas confirmée. | - Le SIL actuel permet-il une telle évolution ? <br> - Quelles sont les **exigences techniques** pour le nouveau circuit ? |

---
## **3. Termes à éviter ou à clarifier**

| **Terme** | **Type** | **Problème identifié** | **Recommandation** |
|-----------|----------|-------------------------|--------------------|
| **"Système informatisé"** | Acteur technique | Trop générique et ambigu. Peut désigner le SIL, le DPI, le middleware ou les analyseurs. | Remplacer par **"Système d'Information de Laboratoire (SIL)"** ou préciser le système concerné. |
| **"Logiciel de gestion des prélèvements"** | Acteur technique | Peut désigner le middleware ou un autre outil. | Préciser **"Middleware de laboratoire"** ou **"Système de gestion des flux d'échantillons"**. |
| **"Bonnes pratiques de laboratoire (BPL)"** | Règle | Terme générique non formalisé dans le corpus. | Remplacer par **"Normes ISO 15189"** ou **"Recommandations HAS/ANSM"**, selon le contexte. |
| **"Urgence"** | Concept | Trop vague. Peut désigner un niveau de priorité, un contexte clinique ou un délai critique. | Préciser **"Niveau de priorité"** ou **"Contexte clinique urgent"**. |
| **"Données contextuelles"** | Information | Trop générique. Doit être détaillé (ex. : type d’AOD, posologie, heure de la dernière prise). | Remplacer par la liste des **données contextuelles spécifiques**. |

---
## **4. Synthèse des termes validés pour la modélisation**

### **Termes validés et prêts à l’emploi**
Les termes suivants sont **clairs, uniques et suffisamment définis** pour être utilisés dans les ateliers, la documentation, les user stories et le code :

#### **Acteurs**
- Cliniciens prescripteurs
- Biologistes médicaux
- Techniciens de laboratoire
- Pharmaciens hospitaliers
- Personnel administratif / Coordinateurs de soins
- Patients
- Équipe informatique (DSI)
- Autorités réglementaires
- Comité de pilotage du projet SIL
- Commission des Anti-infectieux et des Anticoagulants (CAI)
- Équipe de gestion des risques

#### **Acteurs techniques**
- Système d'Information de Laboratoire (SIL)
- Dossier Patient Informatisé (DPI)
- Analyseurs de laboratoire
- Middleware de laboratoire
- Systèmes d'alerte et de priorisation

#### **Concepts centraux**
- Anticoagulant Oral Direct (AOD)
- Dosage anti-Xa
- Demande urgente de dosage anti-Xa
- Prescription électronique
- Échantillon biologique (Tube)
- Exigences pré-analytiques
- Priorisation des demandes
- Contexte clinique
- Fonction rénale
- Interprétation du dosage anti-Xa
- Traçabilité
- Sécurité des données
- Protocole local
- Audit trail
- Non-conformité des tubes
- Astreinte biologique
- Recommandations thérapeutiques
- Collaboration pluridisciplinaire
- Conformité réglementaire
- Délai critique
- Portail patient

#### **Informations manipulées**
- Identité du patient
- Service prescripteur
- Type d’AOD
- Posologie
- Heure de la dernière prise
- Fonction rénale (clairance de la créatinine)
- Contexte clinique
- Autres traitements
- Résultat brut du dosage anti-Xa
- Seuil d’alerte
- Compte-rendu d’interprétation
- Statut de la demande
- Niveau de priorité
- Statut de conformité des tubes
- Logs d’audit (audit trail)
- Recommandations thérapeutiques

#### **Décisions métier**
- Prescrire un dosage anti-Xa en urgence
- Classer manuellement une demande par niveau d’urgence
- Valider ou rejeter une demande de dosage
- Prioriser une analyse
- Interpréter un résultat de dosage anti-Xa
- Valider la conformité d’un tube
- Signaler une non-conformité ou un résultat aberrant
- Proposer l’administration d’un antidote
- Adapter le traitement anticoagulant
- Relancer un service en cas de retard ou non-conformité

#### **Règles métier**
- Prescription électronique obligatoire
- Respect des protocoles locaux
- Validation biologique obligatoire
- Rejet des demandes non conformes
- Priorisation automatique des demandes
- Vérification automatique des conformités pré-analytiques
- Intégration automatique des résultats des analyseurs
- Traçabilité complète obligatoire
- Signature électronique pour les résultats validés
- Accès sécurisé aux données
- Conservation des logs pendant 10 ans
- Disponibilité 24/7 du SIL
- Respect des délais critiques

#### **Événements et processus**
- Prescription d’un dosage anti-Xa
- Validation de la demande
- Prélèvement sanguin
- Transport de l’échantillon
- Vérification de la conformité des tubes
- Réalisation du dosage anti-Xa
- Transmission des résultats bruts
- Interprétation des résultats
- Transmission des recommandations
- Adaptation du traitement
- Archivage des données

#### **Contraintes**
- Délais critiques
- Disponibilité 24/7 du SIL
- Exigences pré-analytiques strictes
- Traçabilité complète
- Sécurité des données
- Respect des normes réglementaires
- Gestion des astreintes
- Collaboration pluridisciplinaire

---
## **5. Recommandations pour la suite**

1. **Valider les termes à clarifier** avec les experts métier avant de passer à l’étape 3 (modélisation comportementale).
2. **Utiliser ce vocabulaire** dans les ateliers, les user stories et la documentation pour éviter les ambiguïtés.
3. **Éviter les synonymes** et privilégier les termes validés pour garantir une communication unifiée.
4. **Documenter les hypothèses** (ex. : seuils d’interprétation, critères de conformité) pour les affiner lors des ateliers.
5. **Intégrer ce vocabulaire** dans les tests fonctionnels et les critères d’acceptation des user stories.

---
**Fin du document**