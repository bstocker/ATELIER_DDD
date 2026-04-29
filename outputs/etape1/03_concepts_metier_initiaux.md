```markdown
# Concepts métier initiaux

## Liste des concepts identifiés

---

### 1. **Anticoagulant Oral Direct (AOD)**
- **Définition** :
  Classe de médicaments anticoagulants administrés par voie orale, utilisés pour prévenir ou traiter les événements thromboemboliques.
- **Informations associées** :
  - Types mentionnés : apixaban, rivaroxaban, édoxaban (à confirmer).
  - Indications : prévention des AVC chez les patients en fibrillation atriale, traitement des thromboses veineuses profondes, etc.
- **Termes nécessitant validation** :
  - Liste exhaustive des AOD concernés par le dosage anti-Xa.
  - Posologies standard et seuils thérapeutiques associés.

---

### 2. **Dosage anti-Xa**
- **Définition** :
  Analyse biologique mesurant l'activité anticoagulante des AOD en évaluant l'inhibition du facteur Xa (enzyme clé de la coagulation).
- **Informations associées** :
  - Utilité : évaluer l'efficacité et la sécurité du traitement anticoagulant.
  - Contexte : demandes urgentes pour adapter rapidement le traitement (ex. : hémorragie, chirurgie).
- **Termes nécessitant validation** :
  - Méthode analytique utilisée (ex. : chromogénique, immunologique).
  - Seuil de normalité et intervalles thérapeutiques pour chaque AOD.

---
### 3. **Demande urgente de dosage anti-Xa**
- **Définition** :
  Prescription médicale prioritaire de dosage anti-Xa pour un patient sous AOD, nécessitant une prise en charge immédiate en raison de la criticité clinique.
- **Informations associées** :
  - Origine : services d'urgence, réanimation, bloc opératoire, services extérieurs.
  - Critères d'urgence : hémorragie active, chirurgie en urgence, suspicion de surdosage.
  - Circuit : prescription → prélèvement → analyse → interprétation → transmission des résultats.
- **Termes nécessitant validation** :
  - Liste exhaustive des critères d'urgence clinique.
  - Délais maximaux acceptables pour chaque niveau de priorité.

---
### 4. **Prescription électronique**
- **Définition** :
  Acte médical formalisé via un système informatisé (ex. : SIL, DPI) pour demander un dosage anti-Xa.
- **Informations associées** :
  - Données saisies : identité du patient, service prescripteur, type d'AOD, posologie, heure de la dernière prise, contexte clinique.
  - Intégration : lien avec le dossier patient et les protocoles locaux.
- **Termes nécessitant validation** :
  - Champ obligatoires dans la prescription.
  - Intégration avec les systèmes existants (DPI, SIL).

---
### 5. **Échantillon biologique (Tube)**
- **Définition** :
  Prélèvement sanguin destiné à l'analyse du dosage anti-Xa, soumis à des exigences pré-analytiques strictes.
- **Informations associées** :
  - Type de tube : généralement tube citraté 3.2% (à confirmer).
  - Volume minimal requis.
  - Délai maximal entre prélèvement et analyse.
  - Conditions de transport (température, délai).
- **Termes nécessitant validation** :
  - Critères exacts de conformité des tubes.
  - Procédure en cas de non-conformité.

---
### 6. **Exigences pré-analytiques**
- **Définition** :
  Ensemble de conditions à respecter pour garantir la validité de l'échantillon avant analyse.
- **Informations associées** :
  - Critères : type de tube, volume, délai de transport, conditions de centrifugation.
  - Conséquences de la non-conformité : rejet de l'échantillon, demande de complément, alerte au prescripteur.
- **Termes nécessitant validation** :
  - Liste détaillée des exigences pour chaque AOD.
  - Procédure de gestion des non-conformités.

---
### 7. **Priorisation des demandes**
- **Définition** :
  Classement automatique ou manuel des demandes de dosage anti-Xa en fonction de leur urgence clinique.
- **Informations associées** :
  - Critères : hémorragie active (priorité absolue), chirurgie programmée (priorité haute), contrôle systématique (priorité basse).
  - Mécanisme : règles métiers prédéfinies dans le SIL.
- **Termes nécessitant validation** :
  - Grille de priorisation complète avec seuils cliniques.
  - Règles d'escalade en cas de conflit de priorités.

---
### 8. **Contexte clinique**
- **Définition** :
  Ensemble des informations médicales et thérapeutiques nécessaires à l'interprétation du dosage anti-Xa.
- **Informations associées** :
  - Données : type d'AOD, posologie, heure de la dernière prise, fonction rénale (clairance de la créatinine), autres traitements anticoagulants.
  - Objectif : adapter l'interprétation du résultat au profil du patient.
- **Termes nécessitant validation** :
  - Liste exhaustive des données contextuelles à collecter.
  - Méthode de saisie (manuelle, intégration automatique depuis le DPI).

---
### 9. **Fonction rénale**
- **Définition** :
  Capacité des reins à filtrer le sang, évaluée par la clairance de la créatinine (formule CKD-EPI ou MDRD).
- **Informations associées** :
  - Impact sur le dosage anti-Xa : les AOD sont éliminés en partie par les reins, donc leur activité est prolongée en cas d'insuffisance rénale.
  - Seuil critique : clairance < 30 mL/min (à confirmer).
- **Termes nécessitant validation** :
  - Formule utilisée pour calculer la clairance.
  - Seuil d'insuffisance rénale impactant la posologie.

---
### 10. **Interprétation du dosage anti-Xa**
- **Définition** :
  Analyse des résultats du dosage en fonction du contexte clinique pour évaluer l'efficacité et la sécurité du traitement anticoagulant.
- **Informations associées** :
  - Données d'entrée : résultat du dosage, type d'AOD, posologie, heure de la dernière prise, fonction rénale, contexte clinique.
  - Sortie : compte-rendu d'interprétation avec recommandations thérapeutiques (ex. : adaptation de la posologie, arrêt temporaire du traitement).
- **Termes nécessitant validation** :
  - Grille d'interprétation pour chaque AOD.
  - Seuil d'alerte pour les surdosages/sous-dosages.

---
### 11. **Traçabilité**
- **Définition** :
  Enregistrement systématique de toutes les étapes du circuit des demandes urgentes de dosage anti-Xa, depuis la prescription jusqu'à l'interprétation.
- **Informations associées** :
  - Données tracées : identité du prescripteur, heure de la prescription, conformité des tubes, heure de l'analyse, résultat, biologiste ayant validé, heure de transmission des résultats.
  - Objectif : permettre les audits, améliorer les processus, garantir la sécurité.
- **Termes nécessitant validation** :
  - Liste des événements à tracer.
  - Durée de conservation des données.

---
### 12. **Sécurité des données**
- **Définition** :
  Ensemble des mesures techniques et organisationnelles pour protéger la confidentialité, l'intégrité et la disponibilité des données du circuit.
- **Informations associées** :
  - Mesures : authentification forte, droits d'accès différenciés, chiffrement des données, audit trail.
  - Conformité : respect du RGPD et des normes d'accréditation (ex. : ISO 15189).
- **Termes nécessitant validation** :
  - Politique de sécurité détaillée.
  - Procédure en cas de violation de données.

---
### 13. **Système informatisé (SIL)**
- **Définition** :
  Outil informatique centralisant la gestion des demandes de dosage, des résultats et des données contextuelles.
- **Informations associées** :
  - Fonctionnalités : prescription électronique, priorisation automatique, traçabilité, aide à l'interprétation.
  - Intégrations : DPI, analyseurs de laboratoire, systèmes d'alerte.
- **Termes nécessitant validation** :
  - Compatibilité avec les systèmes existants.
  - Exigences techniques (disponibilité, interopérabilité).

---
### 14. **Dossier Patient Informatisé (DPI)**
- **Définition** :
  Système informatisé stockant les données médicales du patient, incluant les traitements en cours et les résultats d'examens.
- **Informations associées** :
  - Données utiles : fonction rénale, traitements anticoagulants, antécédents médicaux.
  - Intégration : transmission automatique au SIL pour l'interprétation des résultats.
- **Termes nécessitant validation** :
  - Champs pertinents à partager avec le SIL.
  - Format des données échangées.

---
### 15. **Protocole local**
- **Définition** :
  Document définissant les bonnes pratiques pour la prescription, l'analyse et l'interprétation des dosages anti-Xa dans l'établissement.
- **Informations associées** :
  - Contenu : indications de dosage, seuils d'urgence, grilles d'interprétation, recommandations thérapeutiques.
  - Responsables : Commission des Anti-infectieux et des Anticoagulants (CAI).
- **Termes nécessitant validation** :
  - Version actuelle du protocole.
  - Fréquence de mise à jour.

---
### 16. **Audit trail**
- **Définition** :
  Journal électronique enregistrant toutes les actions effectuées sur une demande de dosage, depuis la prescription jusqu'à l'archivage.
- **Informations associées** :
  - Données enregistrées : utilisateur ayant effectué l'action, horodatage, type d'action (création, modification, validation).
  - Objectif : traçabilité pour les audits internes/externes.
- **Termes nécessitant validation** :
  - Liste des actions à tracer.
  - Format et durée de conservation des logs.

---
### 17. **Non-conformité des tubes**
- **Définition** :
  Situation où un échantillon biologique ne respecte pas les exigences pré-analytiques requises pour le dosage anti-Xa.
- **Informations associées** :
  - Causes : type de tube incorrect, volume insuffisant, délai de transport dépassé, mauvaise centrifugation.
  - Conséquences : rejet de l'échantillon, demande de complément, alerte au prescripteur.
- **Termes nécessitant validation** :
  - Liste exhaustive des critères de non-conformité.
  - Procédure de gestion (refus, demande de complément, escalade).

---
### 18. **Astreinte biologique**
- **Définition** :
  Organisation permettant la prise en charge des demandes urgentes en dehors des heures ouvrables (nuit, week-end, jours fériés).
- **Informations associées** :
  - Acteurs : biologiste d'astreinte.
  - Processus : transmission des demandes, validation des résultats, communication aux cliniciens.
- **Termes nécessitant validation** :
  - Liste des services couverts par l'astreinte.
  - Procédure de déclenchement de l'astreinte.

---
### 19. **Recommandations thérapeutiques**
- **Définition** :
  Conseils émis par le biologiste après interprétation du dosage anti-Xa, visant à adapter le traitement anticoagulant.
- **Informations associées** :
  - Contenu : adaptation de la posologie, arrêt temporaire du traitement, administration d'un antidote (ex. : andexanet alfa pour les anti-Xa).
  - Destinataires : cliniciens prescripteurs.
- **Termes nécessitant validation** :
  - Grille de recommandations pour chaque AOD et chaque contexte clinique.
  - Format de transmission (compte-rendu structuré, messagerie sécurisée).

---
### 20. **Collaboration pluridisciplinaire**
- **Définition** :
  Travail coordonné entre cliniciens, biologistes, pharmaciens et personnel administratif pour la prise en charge des patients sous AOD.
- **Informations associées** :
  - Acteurs : urgentistes, réanimateurs, biologistes, pharmaciens, coordinateurs de soins.
  - Processus : transmission des informations, prise de décision conjointe.
- **Termes nécessitant validation** :
  - Rôles et responsabilités de chaque acteur.
  - Canaux de communication (messagerie, réunions, SIL).

---
### 21. **Conformité réglementaire**
- **Définition** :
  Respect des normes et bonnes pratiques en vigueur pour la réalisation et l'interprétation des dosages anti-Xa.
- **Informations associées** :
  - Normes : ISO 15189 (laboratoires de biologie médicale), RGPD (protection des données), recommandations HAS/ANSM.
  - Objectif : éviter les sanctions et garantir la qualité des soins.
- **Termes nécessitant validation** :
  - Liste des normes applicables.
  - Procédure de vérification de la conformité.

---
### 22. **Délai critique**
- **Définition** :
  Fenêtre de temps maximale acceptable entre la prescription et la transmission des résultats pour une prise en charge thérapeutique optimale.
- **Informations associées** :
  - Exemples : 1 heure pour une hémorragie active, 4 heures pour une chirurgie programmée.
  - Mesure : suivi en temps réel des délais dans le SIL.
- **Termes nécessitant validation** :
  - Délais maximaux pour chaque niveau de priorité.
  - Procédure en cas de dépassement de délai.

---
### 23. **Analyseur de laboratoire**
- **Définition** :
  Équipement automatisé réalisant le dosage anti-Xa sur les échantillons biologiques.
- **Informations associées** :
  - Modèles : ACL TOP, STA R Max (exemples).
  - Intégration : transmission automatique des résultats au SIL.
- **Termes nécessitant validation** :
  - Compatibilité avec le SIL.
  - Procédure de maintenance et de contrôle qualité.

---
### 24. **Middleware de laboratoire**
- **Définition** :
  Logiciel intermédiaire gérant les flux d'échantillons et les échanges de données entre les services de soins, le laboratoire et les analyseurs.
- **Informations associées** :
  - Fonctionnalités : vérification des conformités pré-analytiques, routage des échantillons, transmission des résultats.
  - Intégration : lien avec le SIL et les analyseurs.
- **Termes nécessitant validation** :
  - Compatibilité avec les systèmes existants.
  - Exigences fonctionnelles.

---
### 25. **Portail patient**
- **Définition** :
  Interface permettant aux patients d'accéder à leurs résultats d'examens et aux informations associées.
- **Informations associées** :
  - Fonctionnalités : consultation des résultats, alertes en cas d'anomalie, messagerie sécurisée avec les cliniciens.
  - Sécurité : authentification forte, respect du RGPD.
- **Termes nécessitant validation** :
  - Liste des informations accessibles au patient.
  - Procédure de consentement.

---
```