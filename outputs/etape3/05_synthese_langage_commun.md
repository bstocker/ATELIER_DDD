Voici une **synthèse structurée et actionnable** pour finaliser le langage commun partagé dans le cadre de la gestion des demandes urgentes de dosage anti-Xa dans le SIL. Ce livrable est conçu pour être **utilisé directement** dans les ateliers, la documentation, les user stories, les tests et le code, tout en préservant le contexte métier validé.

---

---

# **📌 Livrable Final : Glossaire du Langage Commun Partagé**
**Domaine** : Gestion des demandes urgentes de dosage anti-Xa dans le SIL
**Version** : 1.0
**Date** : [À compléter]
**Auteurs** : Analyste DDD
**Sources** : Livrables des étapes 1 et 2 (14 documents)

---

## **📋 Table des Matières**
1. [Introduction](#introduction)
2. [Règles Générales d'Usage](#règles-générales-dusage)
3. [Glossaire par Catégorie](#glossaire-par-catégorie)
   - [3.1. Acteurs](#31-acteurs)
   - [3.2. Concepts Métier Centraux](#32-concepts-métier-centraux)
   - [3.3. Informations Manipulées](#33-informations-manipulées)
   - [3.4. Décisions Métier](#34-décisions-métier)
   - [3.5. Règles Métier](#35-règles-métier)
   - [3.6. Événements et Processus](#36-événements-et-processus)
   - [3.7. Contraintes](#37-contraintes)
4. [Termes à Clarifier avec les Experts](#4-termes-à-clarifier-avec-les-experts)
5. [Exemples d'Utilisation](#5-exemples-dutilisation)
6. [Références et Normes](#6-références-et-normes)
7. [Annexes](#7-annexes)

---

---

## **1. Introduction**
### **Objectif**
Ce glossaire établit un **langage commun partagé** pour le domaine des **demandes urgentes de dosage anti-Xa** dans le SIL. Il vise à :
- **Éviter les ambiguïtés** entre les acteurs (cliniciens, biologistes, techniciens, pharmaciens, patients, équipe IT, autorités réglementaires).
- **Stabiliser les termes** pour une utilisation cohérente dans :
  - Les ateliers métiers et techniques.
  - La documentation (exigences, spécifications).
  - Les user stories et cas de test.
  - Le code (noms de variables, méthodes, classes).
- **Servir de référence** pour les étapes ultérieures du DDD (modélisation comportementale, conception stratégique).

### **Portée**
Ce glossaire couvre :
- Les **acteurs** (humains, organisationnels, techniques).
- Les **concepts métier** (AOD, dosage anti-Xa, priorisation, etc.).
- Les **informations manipulées** (données patients, résultats, contexte clinique).
- Les **décisions** (prescrire, valider, interpréter).
- Les **règles métier** (obligations réglementaires, processus).
- Les **événements** (prescription, prélèvement, analyse).
- Les **contraintes** (délais critiques, conformité).

### **Public Cible**
- **Experts métiers** : Cliniciens prescripteurs, biologistes, techniciens de laboratoire, pharmaciens, coordinateurs de soins.
- **Analystes et concepteurs** : Pour la modélisation et la rédaction des user stories.
- **Développeurs** : Pour l'implémentation (noms de variables, méthodes, interfaces).
- **Testeurs** : Pour la rédaction des cas de test.
- **Équipe IT (DSI)** : Pour l'intégration technique (SIL, DPI, middleware).
- **Autorités réglementaires** : Pour la conformité (ISO 15189, RGPD).

---

---

## **2. Règles Générales d'Usage**
### **2.1. Conventions de Nomination**
| **Règle** | **Exemple** | **À Éviter** |
|-----------|------------|--------------|
| **Utiliser des termes validés** | "Clinicien prescripteur" | "Médecin prescripteur" |
| **Sigles standardisés** | "SIL", "DPI", "AOD", "CAI" | "Système informatisé", "Dossier médical", "Anticoagulant oral" |
| **Éviter le jargon technique non validé** | "Prescription électronique" | "API", "Middleware", "Backend" |
| **Casse** | "Dosage anti-Xa" (majuscule initiale) | "dosage Anti-Xa" |
| **Singulier** | "Une Demande urgente" | "Des Demandes urgentes" |
| **Pas d'anglicismes** | "Heure de la dernière prise" | "Last intake time" |
| **Formulation active** | "Le Biologiste valide la demande" | "La demande est validée par le biologiste" |

### **2.2. Règles Spécifiques par Catégorie**
| **Catégorie** | **Règle** | **Exemple** |
|---------------|-----------|-------------|
| **Acteurs** | Utiliser le terme validé + rôle précis. | "Clinicien prescripteur (urgentiste)" |
| **Concepts** | Définir clairement et éviter les synonymes. | "Anticoagulant Oral Direct (AOD)" |
| **Informations** | Préciser le format et l'unité. | "Résultat brut du dosage anti-Xa (UI/mL)" |
| **Décisions** | Formuler comme une action métier. | "Valider ou rejeter une demande de dosage" |
| **Règles** | Utiliser des formulations impératives. | "La prescription électronique est obligatoire." |
| **Événements** | Décrire le déclencheur et le résultat. | "Prescription d'un dosage anti-Xa → Validation par le biologiste" |
| **Contraintes** | Quantifier les exigences. | "Délai critique : ≤1 heure pour une hémorragie active." |

### **2.3. Utilisation dans les Échanges Projet**
- **Ateliers métiers** : Utiliser **uniquement** les termes validés.
- **Documentation** : Inclure le glossaire en annexe et référencer les termes.
- **User Stories** : Formuler les histoires avec le vocabulaire métier.
- **Tests** : Rédiger les cas de test en utilisant les termes du glossaire.
- **Code** : Utiliser les termes pour les noms de variables, méthodes et classes (ex: `patientRenalFunction`, `validateTubeCompliance()`).

---

---

## **3. Glossaire par Catégorie**
*(Les termes marqués d'un 🔴 nécessitent une validation par les experts.)*

---

### **3.1. Acteurs**
| **Terme** | **Définition Métier** | **Termes à Éviter** | **Exemple d'Utilisation** | **🔴 Questions Restantes** |
|-----------|-----------------------|---------------------|---------------------------|----------------------------|
| **Clinicien prescripteur** | Professionnel de santé (médecin, interne sous supervision) qui prescrit un dosage anti-Xa en urgence pour un patient sous AOD. Évalue le contexte clinique et saisit les données contextuelles. | Médecin prescripteur, prescripteur | *"Le Clinicien prescripteur saisit l'Heure de la dernière prise d'apixaban dans le SIL."* | - Les internes peuvent-ils prescrire sans supervision ? <br> - Les prescripteurs externes (libéraux) sont-ils inclus ? |
| **Biologiste médical** | Professionnel responsable de la validation des demandes, de la priorisation des analyses, de l'interprétation des résultats et de la rédaction de recommandations thérapeutiques. Garantit la qualité et la fiabilité des résultats. | Biologiste | *"Le Biologiste médical valide la demande et interprète le résultat en tenant compte de la Fonction rénale."* | - Qui valide les résultats en astreinte ? |
| **Technicien de laboratoire** | Professionnel qui prépare les échantillons, vérifie la conformité des tubes, réalise le dosage anti-Xa et saisit les résultats dans le SIL. Signale les non-conformités ou résultats aberrants. | Manipulateur, technicien de biochimie | *"Le Technicien de laboratoire vérifie que le tube est conforme (citraté 3.2%, volume ≥1.8 mL)."* | - Peut-il valider définitivement la conformité des tubes ? |
| **Pharmacien hospitalier** | Professionnel qui conseille les cliniciens sur le choix et l'adaptation des anticoagulants, analyse les interactions médicamenteuses et participe à la gestion des urgences hémorragiques (ex: administration d'antidotes). | Pharmacien | *"Le Pharmacien hospitalier valide les recommandations thérapeutiques du Biologiste."* | - Peut-il contester les recommandations du Biologiste ? |
| **Coordinateur de soins** | Professionnel qui gère les flux de demandes entre les services et le laboratoire, coordonne les prélèvements et le transport des échantillons, et suit les délais de traitement. | Gestionnaire de flux, secrétaire médical | *"Le Coordinateur de soins relance le service des urgences pour un prélèvement en retard."* | - Peut-il prescrire ou valider des demandes ? |
| **Patient** | Personne sous AOD pour laquelle un dosage anti-Xa est prescrit. Doit être informée des résultats et signaler les effets indésirables. | Usager, bénéficiaire | *"Le Patient consulte ses résultats via le Portail patient."* | - Le consentement est-il toujours requis ? <br> - Un Portail patient sera-t-il mis en place ? |
| **Équipe informatique (DSI)** | Équipe responsable de la maintenance et de l'évolution du SIL pour répondre aux besoins du circuit des demandes urgentes. Garantit la sécurité, la disponibilité et l'interopérabilité du système. | Service informatique, éditeur du SIL | *"La DSI intègre le module de priorisation automatique dans le SIL."* | - Qui compose exactement cette équipe ? |
| **Autorités réglementaires** | Organismes (HAS, ANSM, ARS, CNIL) qui vérifient la conformité du circuit avec les bonnes pratiques et les normes (ISO 15189, RGPD). Peuvent sanctionner en cas de non-conformité. | - | *"L'ARS audite le laboratoire pour vérifier le respect de la norme ISO 15189."* | - Quelles normes exactes doivent être respectées ? |
| **Comité de pilotage du projet SIL** | Instance qui supervise l'évolution du SIL pour intégrer le circuit des demandes urgentes. Valide les priorités fonctionnelles et alloue les ressources. | COPIL | *"Le Comité de pilotage valide l'ajout du module de traçabilité dans le SIL."* | - Qui compose ce comité ? <br> - Quels sont ses pouvoirs décisionnels ? |
| **Commission des Anti-infectieux et des Anticoagulants (CAI)** | Commission qui définit les protocoles locaux pour la prescription, l'analyse et l'interprétation des dosages anti-Xa. Met à jour les recommandations en fonction des données scientifiques. | Commission des anticoagulants | *"La CAI met à jour le protocole local pour inclure les seuils d'interprétation de l'apixaban."* | - Qui compose cette commission ? <br> - Quelle est sa fréquence de mise à jour ? |
| **Équipe de gestion des risques** | Équipe qui identifie et atténue les risques liés au circuit (ex: erreurs de dosage, retards). Met en place des barrières de sécurité (ex: alertes automatiques). | Cellule qualité | *"L'Équipe de gestion des risques identifie un risque de retard dans les urgences absolues."* | - Qui compose cette équipe ? |

---

### **3.2. Concepts Métier Centraux**
| **Terme** | **Définition Métier** | **Termes à Éviter** | **Exemple d'Utilisation** | **🔴 Questions Restantes** |
|-----------|-----------------------|---------------------|---------------------------|----------------------------|
| **Anticoagulant Oral Direct (AOD)** | Classe de médicaments anticoagulants administrés par voie orale, utilisés pour prévenir ou traiter les événements thromboemboliques. Les AOD concernés par le dosage anti-Xa incluent l'apixaban, le rivaroxaban et l'édoxaban. | Anticoagulants oraux directs, NACO | *"Le Clinicien prescrit un dosage anti-Xa pour un patient sous apixaban (5 mg 2x/jour)."* | - Faut-il inclure le dabigatran ? |
| **Dosage anti-Xa** | Analyse biologique mesurant l'activité anticoagulante des AOD en évaluant l'inhibition du facteur Xa. Utilisée pour évaluer l'efficacité et la sécurité du traitement anticoagulant, notamment en situation d'urgence. | Test anti-Xa, mesure de l'activité anti-Xa | *"Le Dosage anti-Xa est réalisé sur un échantillon sanguin prélevé dans un tube citraté 3.2%."* | - Quelle méthode analytique est utilisée ? <br> - Quels sont les seuils thérapeutiques ? |
| **Demande urgente de dosage anti-Xa** | Prescription médicale prioritaire de dosage anti-Xa pour un patient sous AOD, nécessitant une prise en charge immédiate en raison de la criticité clinique (ex: hémorragie active, chirurgie en urgence). | Prescription urgente, analyse en urgence | *"La Demande est classée en 'urgence absolue' en raison d'une hémorragie active non contrôlée."* | - Quels critères cliniques définissent une urgence absolue ? |
| **Prescription électronique** | Acte médical formalisé via un système informatisé (SIL, DPI) pour demander un dosage anti-Xa. Inclut l'identité du patient, le service prescripteur, le type d'AOD, la posologie, l'heure de la dernière prise et le contexte clinique. | Ordonnance électronique, demande informatisée | *"Le Clinicien prescrit une Prescription électronique dans le SIL avec les données contextuelles complètes."* | - La prescription doit-elle être obligatoirement électronique ? <br> - Existe-t-il une procédure de secours en cas de panne du SIL ? |
| **Échantillon biologique (Tube)** | Prélèvement sanguin destiné à l'analyse du dosage anti-Xa, soumis à des exigences pré-analytiques strictes (type de tube, volume, délai de transport, conditions de transport). | Prélèvement sanguin, tube de prélèvement | *"Le Technicien vérifie que l'échantillon est prélevé dans un tube citraté 3.2% avec un volume ≥1.8 mL et un délai de transport ≤4h."* | - Quel est le type de tube exact requis ? <br> - Quel est le volume minimal requis ? |
| **Exigences pré-analytiques** | Ensemble de conditions à respecter pour garantir la validité de l'échantillon avant analyse (ex: type de tube citraté 3.2%, volume minimal, délai maximal entre prélèvement et analyse, température de transport). | Conditions pré-analytiques, critères de qualité | *"Le Middleware vérifie automatiquement que l'échantillon respecte les Exigences pré-analytiques avant analyse."* | - Qui valide définitivement la conformité des tubes ? |
| **Priorisation des demandes** | Classement automatique ou manuel des demandes de dosage anti-Xa en fonction de leur urgence clinique (ex: hémorragie active = priorité absolue, chirurgie programmée = priorité haute). | Tri des demandes, classement par urgence | *"Le SIL classe automatiquement la Demande en 'urgence absolue' en fonction des critères cliniques saisis par le Clinicien."* | - La priorisation est-elle automatique ou manuelle ? <br> - Qui valide les règles de priorisation ? |
| **Contexte clinique** | Ensemble des informations médicales et thérapeutiques nécessaires à l'interprétation du dosage anti-Xa (ex: type d'AOD, posologie, heure de la dernière prise, fonction rénale, autres traitements, contexte clinique comme une hémorragie active). | Situation clinique, motif de la prescription | *"Le Biologiste interprète le résultat en tenant compte du Contexte clinique : apixaban 5 mg 2x/jour, Heure de la dernière prise à 14h30, Clairance de la créatinine à 25 mL/min, hémorragie active."* | - Quelles données contextuelles sont obligatoires ? <br> - Comment sont-elles saisies ? |
| **Fonction rénale** | Capacité des reins à filtrer le sang, évaluée par la clairance de la créatinine (formule CKD-EPI ou MDRD). Impacte l'élimination des AOD et donc leur activité anticoagulante. Un seuil critique est souvent une clairance < 30 mL/min. | Clairance de la créatinine, DFG, insuffisance rénale | *"La Clairance de la créatinine est calculée à 25 mL/min (formule CKD-EPI), ce qui nécessite une adaptation posologique de l'apixaban."* | - Quelle formule est utilisée ? <br> - Quel est le seuil critique ? |
| **Interprétation du dosage anti-Xa** | Analyse des résultats du dosage en fonction du contexte clinique pour évaluer l'efficacité et la sécurité du traitement anticoagulant. Aboutit à un compte-rendu d'interprétation avec des recommandations thérapeutiques (ex: adaptation de la posologie, arrêt temporaire du traitement). | Analyse des résultats, compte-rendu d'interprétation | *"Le Biologiste interprète le résultat de 0.8 UI/mL pour l'apixaban comme un surdosage en cas d'insuffisance rénale et recommande une réduction de 50% de la posologie."* | - Qui émet les recommandations ? <br> - Quels seuils d'alerte sont utilisés ? |
| **Traçabilité** | Enregistrement systématique de toutes les étapes du circuit des demandes urgentes de dosage anti-Xa, depuis la prescription jusqu'à l'archivage. Permet les audits, l'amélioration des processus et garantit la sécurité. | Historique des actions, journal des événements | *"Le SIL enregistre toutes les actions (prescription, validation, analyse, interprétation) dans un Audit trail avec horodatage et identifiant utilisateur."* | - Quelles actions doivent être tracées ? <br> - Quelle est la durée de conservation des logs ? |
| **Sécurité des données** | Ensemble des mesures techniques et organisationnelles pour protéger la confidentialité, l'intégrité et la disponibilité des données du circuit (ex: authentification forte, droits d'accès différenciés, chiffrement, audit trail). | Protection des données, confidentialité | *"Le SIL met en place une authentification forte (carte CPS) et des droits d'accès différenciés pour garantir la sécurité des données."* | - Quels mécanismes d'authentification sont utilisés ? |
| **Protocole local** | Document définissant les bonnes pratiques pour la prescription, l'analyse et l'interprétation des dosages anti-Xa dans l'établissement. Mis à jour par la CAI en fonction des recommandations HAS/ANSM. | Procédure locale, recommandations internes | *"Le Protocole local de la CAI définit les seuils d'interprétation pour chaque AOD et les critères de priorisation des Demandes."* | - Qui met à jour le protocole ? <br> - Quelle est la fréquence de mise à jour ? |
| **Audit trail** | Journal électronique enregistrant toutes les actions effectuées sur une demande de dosage, depuis la prescription jusqu'à l'archivage. Inclut l'identifiant de l'utilisateur, l'horodatage et le type d'action. | Journal d'audit, logs d'activité | *"L'Audit trail permet de retracer : '14h30 - Dr Martin - Prescription électronique', '14h45 - Dr Dubois - Validation biologique'."* | - Quel est le format des logs ? |
| **Non-conformité des tubes** | Situation où un échantillon biologique ne respecte pas les exigences pré-analytiques requises pour le dosage anti-Xa (ex: type de tube incorrect, volume insuffisant, délai de transport dépassé). | Échantillon non conforme, tube rejeté | *"Le Technicien signale une Non-conformité : tube EDTA au lieu de citraté 3.2% → rejet de l'échantillon et demande de nouveau prélèvement."* | - Que faire en cas de Non-conformité ? |
| **Astreinte biologique** | Organisation permettant la prise en charge des demandes urgentes en dehors des heures ouvrables (nuit, week-end, jours fériés). Un Biologiste d'astreinte valide les résultats et émet des recommandations. | Garde biologique | *"Le Biologiste d'astreinte valide le résultat d'une Demande classée en 'urgence absolue' à 3h du matin."* | - Quels services sont couverts par l'astreinte ? |
| **Recommandations thérapeutiques** | Conseils émis par le Biologiste après interprétation du dosage anti-Xa, visant à adapter le traitement anticoagulant (ex: adaptation de la posologie, arrêt temporaire du traitement, administration d'un antidote comme l'andexanet alfa). | Conseils thérapeutiques, prescriptions adaptées | *"Le Biologiste recommande d'arrêter temporairement l'apixaban et d'administrer 10 mg d'andexanet alfa en cas de surdosage avéré."* | - Quelles recommandations sont émises pour chaque AOD ? |
| **Collaboration pluridisciplinaire** | Travail coordonné entre Cliniciens, Biologistes, Pharmaciens et personnel administratif pour la prise en charge des patients sous AOD. Implique la transmission des informations et la prise de décision conjointe. | Travail d'équipe, coordination entre services | *"La Collaboration pluridisciplinaire permet une prise en charge optimale : le Clinicien prescrit, le Biologiste interprète, le Pharmacien valide les recommandations."* | - Quels canaux de communication sont utilisés ? |
| **Conformité réglementaire** | Respect des normes et bonnes pratiques en vigueur pour la réalisation et l'interprétation des dosages anti-Xa (ex: ISO 15189, RGPD, recommandations HAS/ANSM). | Respect des normes, accréditation | *"Le laboratoire respecte la norme ISO 15189 pour la traçabilité et le RGPD pour la protection des données."* | - Quelles normes exactes doivent être respectées ? |
| **Délai critique** | Fenêtre de temps maximale acceptable entre la prescription et la transmission des résultats pour une prise en charge thérapeutique optimale (ex: ≤1 heure pour une hémorragie active). | Fenêtre de temps, délai maximal | *"Le Délai critique pour une hémorragie active est de 1 heure : le SIL alerte si le résultat n'est pas transmis dans ce délai."* | - Quels sont les délais maximaux pour chaque niveau de priorité ? |
| **Portail patient** | Interface permettant aux patients d'accéder à leurs résultats d'examens et aux informations associées (ex: recommandations thérapeutiques). Respecte le RGPD (authentification forte, consentement éclairé). | Interface patient, accès aux résultats | *"Le Patient consulte ses résultats (Dosage anti-Xa à 0.8 UI/mL) via le Portail patient sécurisé."* | - Quelles données seront accessibles ? <br> - Comment sera géré le consentement ? |

---

### **3.3. Informations Manipulées**
| **Terme** | **Définition Métier** | **Format/Unité** | **Exemple d'Utilisation** | **🔴 Questions Restantes** |
|-----------|-----------------------|------------------|---------------------------|----------------------------|
| **Identité du patient** | Données d'identification du patient (nom, prénom, numéro de dossier) utilisées pour la traçabilité et la communication entre acteurs. | Nom, prénom, dossier n° | *"Le SIL utilise l'Identité du patient (Dupont Jean, dossier n°12345) pour tracer toutes les actions."* | - Quelles données d'identité sont utilisées ? |
| **Service prescripteur** | Service médical (urgences, réanimation, bloc opératoire) ayant prescrit le dosage anti-Xa. | Nom du service | *"Le Service prescripteur est les urgences, où le Dr Martin a prescrit le dosage à 14h30."* | - Quels services sont inclus ? |
| **Type d’AOD** | Type d'anticoagulant oral direct prescrit (apixaban, rivaroxaban, édoxaban). | Liste prédéfinie | *"Le Type d'AOD est l'apixaban, prescrit à une posologie de 5 mg 2x/jour."* | - Faut-il inclure le dabigatran ? |
| **Posologie** | Dose et fréquence d'administration de l'AOD. | Ex: "5 mg 2x/jour" | *"La Posologie de l'apixaban est de 5 mg 2x/jour."* | - Quelle précision est requise ? |
| **Heure de la dernière prise** | Heure à laquelle le patient a pris son dernier comprimé d'AOD. Précision à la minute près. | HH:MM | *"L'Heure de la dernière prise est 14h30, ce qui influence l'interprétation du Dosage anti-Xa."* | - Quelle précision est requise ? |
| **Fonction rénale (clairance de la créatinine)** | Valeur de la clairance de la créatinine (formule CKD-EPI ou MDRD) utilisée pour évaluer l'élimination des AOD. | mL/min | *"La Clairance de la créatinine est de 25 mL/min (formule CKD-EPI), ce qui nécessite une adaptation posologique."* | - Quelle formule est utilisée ? |
| **Contexte clinique** | Contexte médical du patient justifiant le dosage (ex: hémorragie active, chirurgie en urgence, suspicion de surdosage). | Texte libre ou liste prédéfinie | *"Le Contexte clinique est une hémorragie active non contrôlée, justifiant une priorité absolue."* | - Quelles données contextuelles sont obligatoires ? |
| **Autres traitements** | Autres médicaments pris par le patient (ex: antiagrégants, autres anticoagulants) pouvant interagir avec les AOD. | Liste de médicaments | *"Le patient prend de l'aspirine (antiagrégant) en plus de l'apixaban, ce qui augmente le risque hémorragique."* | - Quels traitements doivent être déclarés ? |
| **Résultat brut du dosage anti-Xa** | Valeur numérique brute obtenue après analyse de l'échantillon. | UI/mL | *"Le Résultat brut du Dosage anti-Xa est de 0.8 UI/mL."* | - Quelle unité est utilisée ? |
| **Seuil d’alerte** | Valeur seuil du dosage anti-Xa au-delà de laquelle une alerte est déclenchée. | UI/mL | *"Un Seuil d'alerte est déclenché si le résultat dépasse 1.5 UI/mL pour l'apixaban en cas d'insuffisance rénale."* | - Quels seuils sont utilisés pour chaque AOD ? |
| **Compte-rendu d’interprétation** | Document rédigé par le Biologiste après interprétation du résultat, incluant une analyse contextuelle et des recommandations thérapeutiques. | Texte structuré | *"Le Compte-rendu d'interprétation inclut le résultat (0.8 UI/mL), l'analyse contextuelle et les recommandations (réduire la posologie de 50%)."* | - Quel format est utilisé ? |
| **Statut de la demande** | État de la demande dans le SIL (ex: "en attente", "validée", "rejetée", "en cours d'analyse", "terminée"). | Liste prédéfinie | *"Le Statut de la demande est 'validée' par le Biologiste à 14h45."* | - Quels statuts sont utilisés ? |
| **Niveau de priorité** | Niveau d'urgence attribué à une demande (ex: "urgence absolue", "urgence haute", "urgence modérée", "routine"). | Liste prédéfinie | *"Le Niveau de priorité est 'urgence absolue' en raison d'une hémorragie active."* | - Quels niveaux sont utilisés ? |
| **Statut de conformité des tubes** | Résultat de la vérification des exigences pré-analytiques (ex: "conforme", "non conforme : volume insuffisant"). | Liste prédéfinie | *"Le Statut de conformité est 'non conforme : volume insuffisant (1.5 mL au lieu de 1.8 mL)'."* | - Quels critères de conformité sont utilisés ? |
| **Logs d’audit (Audit trail)** | Enregistrement systématique de toutes les actions effectuées sur une demande (ex: prescription, validation, analyse, interprétation, transmission), incluant l'identifiant de l'utilisateur et l'horodatage. | Horodatage, ID utilisateur, type d'action | *"L'Audit trail enregistre : '14h30 - Dr Martin - Prescription électronique', '14h45 - Dr Dubois - Validation biologique'."* | - Quel est le format des logs ? |
| **Recommandations thérapeutiques** | Conseils émis par le Biologiste pour adapter le traitement (ex: "réduire la posologie de 50%", "arrêter temporairement l'AOD"). | Texte structuré | *"Les Recommandations thérapeutiques sont : arrêter temporairement l'apixaban et administrer 10 mg d'andexanet alfa."* | - Quelles recommandations sont émises pour chaque AOD ? |

---

### **3.4. Décisions Métier**
| **Terme** | **Définition Métier** | **Acteurs Impliqués** | **Exemple d'Utilisation** | **🔴 Questions Restantes** |
|-----------|-----------------------|-----------------------|---------------------------|----------------------------|
| **Prescrire un dosage anti-Xa en urgence** | Décision du Clinicien de prescrire un dosage anti-Xa pour un patient sous AOD, basée sur l'évaluation du contexte clinique et le respect des protocoles locaux. | Clinicien prescripteur | *"Le Clinicien prescrit un dosage anti-Xa en urgence pour un patient présentant une hémorragie active sous apixaban."* | - Quels critères cliniques justifient la prescription ? |
| **Classer manuellement une demande par niveau d’urgence** | Décision du Clinicien d'attribuer un niveau de priorité à une demande si le SIL ne le fait pas automatiquement (ex: "urgence absolue" pour une hémorragie active). | Clinicien prescripteur | *"Le Clinicien classe manuellement la Demande en 'urgence absolue' en raison d'une hémorragie active."* | - La priorisation est-elle automatique ou manuelle ? |
| **Valider ou rejeter une demande de dosage** | Décision du Biologiste de valider une demande (si conforme aux protocoles) ou de la rejeter (si non conforme ou inappropriée), avec justification. | Biologiste médical | *"Le Biologiste valide la Demande car elle respecte les protocoles locaux, mais rejette une autre Demande en raison d'un manque de données contextuelles."* | - Quels critères de rejet sont utilisés ? |
| **Prioriser une analyse** | Décision du Biologiste de classer les demandes par ordre d'urgence en fonction des critères cliniques et des délais critiques. | Biologiste médical | *"Le Biologiste priorise les analyses en 'urgence absolue' pour les hémorragies actives et en 'urgence haute' pour les chirurgies programmées."* | - Quelles règles de priorisation sont appliquées ? |
| **Interpréter un résultat de dosage anti-Xa** | Décision du Biologiste d'analyser le résultat du dosage en fonction du contexte clinique et d'émettre un compte-rendu d'interprétation avec des recommandations thérapeutiques. | Biologiste médical | *"Le Biologiste interprète le résultat de 0.8 UI/mL pour l'apixaban comme un surdosage en cas d'insuffisance rénale et recommande une réduction de 50% de la posologie."* | - Quels seuils d'interprétation sont utilisés ? |
| **Valider la conformité d’un tube** | Décision du Technicien de laboratoire (ou du système automatisé) de valider ou rejeter un tube en fonction des exigences pré-analytiques. | Technicien de laboratoire | *"Le Technicien valide le tube car il est conforme (citraté 3.2%, volume ≥1.8 mL, délai ≤4h)."* | - Qui valide définitivement la conformité ? |
| **Signaler une non-conformité ou un résultat aberrant** | Décision du Technicien de laboratoire d'alerter le Biologiste en cas de non-conformité des tubes ou de résultat aberrant, avec demande de complément si nécessaire. | Technicien de laboratoire, Biologiste médical | *"Le Technicien signale une Non-conformité : tube EDTA au lieu de citraté 3.2% → demande de nouveau prélèvement."* | - Que faire en cas de Non-conformité ? |
| **Proposer l’administration d’un antidote** | Décision du Pharmacien (en collaboration avec le Biologiste) de proposer l'administration d'un antidote (ex: andexanet alfa) en cas de surdosage ou d'hémorragie active. | Pharmacien hospitalier, Biologiste médical | *"Le Pharmacien propose l'administration de 10 mg d'andexanet alfa en cas de surdosage avéré d'apixaban."* | - Qui valide l'administration de l'antidote ? |
| **Adapter le traitement anticoagulant** | Décision du Clinicien (en collaboration avec le Pharmacien et le Biologiste) d'adapter la posologie de l'AOD ou d'arrêter temporairement le traitement en fonction des résultats et des recommandations. | Clinicien prescripteur, Pharmacien hospitalier, Biologiste médical | *"Le Clinicien adapte la posologie de l'apixaban de 5 mg 2x/jour à 2.5 mg 2x/jour en fonction des Recommandations thérapeutiques du Biologiste."* | - Qui prend la décision finale ? |
| **Relancer un service en cas de retard ou non-conformité** | Décision du Coordinateur de soins de relancer un service prescripteur en cas de retard dans le prélèvement ou de non-conformité des tubes. | Coordinateur de soins | *"Le Coordinateur de soins relance le service des urgences pour un prélèvement en retard et met à jour le Statut de la demande dans le SIL."* | - Qui est responsable de la relance ? |

---

### **3.5. Règles Métier**
| **Terme** | **Définition Métier** | **Exemple d'Utilisation** | **🔴 Questions Restantes** |
|-----------|-----------------------|---------------------------|----------------------------|
| **Prescription électronique obligatoire** | Toute demande de dosage anti-Xa doit être formalisée via une Prescription électronique dans le SIL. | *"La Prescription électronique est obligatoire pour toutes les Demandes de dosage anti-Xa."* | - Existe-t-il une procédure de secours en cas de panne du SIL ? |
| **Respect des protocoles locaux** | La prescription doit respecter les indications définies par les protocoles de la CAI et les recommandations HAS/ANSM. | *"La prescription respecte le Protocole local de la CAI pour l'apixaban."* | - Quels sont les protocoles locaux exacts ? |
| **Validation biologique obligatoire** | Toute demande de dosage anti-Xa doit être validée par un Biologiste avant analyse. | *"Toute Demande de dosage anti-Xa est validée par un Biologiste avant analyse."* | - Qui valide les Demandes en astreinte ? |
| **Rejet des demandes non conformes** | Les demandes ne respectant pas les protocoles ou les critères cliniques doivent être rejetées avec justification. | *"La Demande est rejetée car elle ne respecte pas les critères cliniques (pas d'indication de dosage anti-Xa pour ce patient)."* | - Quels critères de rejet sont utilisés ? |
| **Priorisation automatique des demandes** | Le SIL doit classer automatiquement les demandes par niveau d'urgence en fonction de règles métiers prédéfinies. | *"Le SIL classe automatiquement la Demande en 'urgence absolue' en fonction des critères cliniques saisis par le Clinicien."* | - Quelles sont les règles de priorisation exactes ? |
| **Vérification automatique des conformités pré-analytiques** | Le SIL ou le Middleware doit alerter en temps réel si un tube est non conforme (type incorrect, volume insuffisant, délai de transport dépassé). | *"Le Middle