# **Bounded Contexts candidats pour le domaine des demandes urgentes de dosage anti-Xa**
**Domaine métier** : Gestion des demandes urgentes de dosage anti-Xa dans le SIL
**Date** : [À compléter]
**Version** : 1.0
**Auteurs** : Analyste DDD
**Sources principales** :
- Livrables étape 1 :
  - `01_reformulation_du_besoin.md`
  - `02_acteurs_du_domaine.md`
  - `03_concepts_metier_initiaux.md`
  - `04_contraintes_et_risques.md`
  - `05_vision_globale_du_domaine.md`
- Livrables étape 2 :
  - `01_cartographie_acteurs_responsabilites.md`
  - `02_attentes_objectifs_acteurs.md`
  - `03_decisions_informations_manipulees.md`
  - `04_regles_metier.md`
  - `05_priorites_exceptions_contraintes.md`
  - `06_conflits_objectifs_arbitrages.md`
  - `07_base_modelisation_comportementale.md`
  - `08_glossaire_metier.md`
- Livrables étape 4 :
  - `01_zones_fonctionnelles_domaine.md`
  - `02_proposition_sous_domaines.md`
  - `03_classification_sous_domaines.md`
  - `04_interactions_sous_domaines.md`
  - `05_priorites_conception_sous_domaines.md`
  - `06_synthese_decoupage_sous_domaines.md`

---

---

## **1. Introduction**
Ce document identifie les **Bounded Contexts candidats** pour le domaine des **demandes urgentes de dosage anti-Xa** dans le SIL, en s’appuyant sur :
- Les **zones fonctionnelles** et **sous-domaines** proposés dans les étapes précédentes.
- Les **acteurs, responsabilités, décisions et règles métier** identifiés.
- Les **contraintes réglementaires, temporelles et pré-analytiques**.
- Les **interactions critiques** entre acteurs et systèmes.

L’objectif est de :
- **Délimiter des espaces cohérents** où le vocabulaire, les règles et les modèles gardent un sens stable.
- **Éviter les ambiguïtés** entre parties prenantes (ex. : qui valide une demande ? qui interprète un résultat ?).
- **Maîtriser les dépendances** entre contextes (ex. : contrat d’échange entre la prescription et la priorisation).
- **Préparer les étapes suivantes** de la démarche DDD (modélisation comportementale, conception des agrégats, etc.).

**Méthodologie** :
- Chaque **Bounded Context candidat** est défini par :
  - Une **responsabilité principale** claire et distincte.
  - Les **sous-domaines ou zones fonctionnelles** qu’il couvre.
  - Les **acteurs principalement concernés**.
  - Les **concepts métier centraux** manipulés.
  - Les **hypothèses de découpage** à valider avec les experts métier.
  - Les **dépendances et contrats d’échange** avec les autres contextes.
- Les **frontières** sont tracées en fonction :
  - Des **règles métier** (ex. : validation biologique obligatoire).
  - Des **décisions clés** (ex. : priorisation des demandes).
  - Des **informations structurantes** (ex. : contexte clinique pour l’interprétation).
- Les **ambiguïtés et points à clarifier** sont explicitement signalés.

---

---

## **2. Liste des Bounded Contexts candidats**

| **ID** | **Nom du Bounded Context** | **Type** | **Responsabilité principale** | **Sous-domaines couverts** | **Acteurs principaux** | **Concepts métier centraux** | **Contexte stable** |
|--------|----------------------------|----------|-------------------------------|-----------------------------|------------------------|-------------------------------|---------------------|
| **BC-AXA-01** | **Prescription Clinique** | Cœur stratégique | Gérer la prescription électronique des dosages anti-Xa en urgence et valider leur pertinence clinique selon les protocoles locaux. | SD-AXA-01 (Prescription et Validation Clinique) | Cliniciens prescripteurs, Biologistes médicaux, CAI | Prescription électronique, Protocoles locaux, Contexte clinique, Validation biologique | Les prescriptions sont validées selon des règles cliniques strictes (CAI) et des données contextuelles exhaustives. |
| **BC-AXA-02** | **Gestion Pré-Analytique** | Support | Vérifier la conformité des échantillons biologiques (tubes) avant analyse et gérer les non-conformités selon les exigences réglementaires. | SD-AXA-02 (Gestion Pré-Analytique des Échantillons) | Techniciens de laboratoire, Biologistes médicaux, SIL | Tube citraté 3.2%, Volume minimal, Délai de transport, Non-conformité | Les exigences pré-analytiques (type de tube, volume, temps) sont strictes et réglementées. |
| **BC-AXA-03** | **Ordonnancement et Priorisation** | Cœur stratégique | Classer les demandes par niveau d’urgence clinique et ordonnancer les analyses en fonction des ressources disponibles et des délais critiques. | SD-AXA-03 (Ordonnancement et Priorisation) | Biologistes médicaux, SIL, Systèmes d’alerte | Niveaux d’urgence (Absolue, Haute, Modérée, Routine), Délais critiques, Conflits de priorité | Les demandes sont classées et ordonnancées selon des critères cliniques objectifs et des ressources limitées. |
| **BC-AXA-04** | **Analyse Laboratoire** | Support | Réaliser les dosages anti-Xa sur les échantillons conformes et transmettre les résultats bruts de manière fiable et traçable au SIL. | SD-AXA-04 (Analyse Laboratoire et Transmission des Résultats) | Techniciens de laboratoire, Analyseurs, SIL | Résultat brut, Intégration automatique, Résultats aberrants | Les résultats sont générés par des équipements automatisés et transmis sans erreur de saisie. |
| **BC-AXA-05** | **Interprétation Clinique** | Cœur stratégique | Interpréter les résultats du dosage anti-Xa en contexte clinique et thérapeutique, et émettre des recommandations thérapeutiques validées. | SD-AXA-05 (Interprétation Clinique et Aide à la Décision) | Biologistes médicaux, Pharmaciens hospitaliers, Cliniciens | Résultat interprété, Grilles d’interprétation, Recommandations thérapeutiques, Seuil d’alerte | Les résultats sont interprétés en fonction de données contextuelles (type d’AOD, fonction rénale, etc.). |
| **BC-AXA-06** | **Collaboration et Communication** | Support | Faciliter la communication sécurisée et structurée entre les acteurs (cliniciens, biologistes, pharmaciens) pour une prise en charge coordonnée. | SD-AXA-07 (Collaboration Multidisciplinaire et Communication Sécurisée) | Cliniciens, Biologistes, Pharmaciens, SIL, Systèmes d’alerte | Messagerie sécurisée, Alertes critiques, Archivage des communications | Les communications sont tracées, horodatées et sécurisées pour éviter les pertes d’information. |
| **BC-AXA-07** | **Gestion des Exceptions** | Support | Gérer les cas particuliers (non-conformités, urgences hors heures ouvrables) et organiser les astreintes pour assurer la continuité du service 24/7. | SD-AXA-08 (Gestion des Exceptions et Astreintes) | Biologistes d’astreinte, Personnel administratif, SIL | Astreinte biologique, Non-conformité en astreinte, Escalade | Les exceptions sont gérées selon des procédures claires pour garantir la continuité du service. |
| **BC-AXA-08** | **Intégration des Données** | Générique/Technique | Assurer l’intégration fluide des données patients (DPI) et des résultats (analyseurs) avec le SIL pour éviter les erreurs de saisie et garantir la cohérence. | SD-AXA-09 (Intégration des Données Patients et Interopérabilité) | DSI, Fournisseurs de middleware, SIL, DPI | Intégration automatique, Formats de données (HL7 FHIR, API), Compatibilité technique | Les données sont échangées entre systèmes sans perte ni corruption. |
| **BC-AXA-09** | **Gestion des Ressources** | Support | Optimiser l’utilisation des ressources critiques (techniciens, analyseurs) pour garantir la réactivité du laboratoire. | SD-AXA-10 (Gestion des Ressources et Planification) | Responsables de laboratoire, SIL | Planification des ressources, Réaffectation en cas de pic d’activité, Optimisation | Les ressources sont allouées de manière optimale pour respecter les délais critiques. |
| **BC-AXA-10** | **Traçabilité et Conformité** | Générique/Technique | Enregistrer systématiquement toutes les actions du circuit et garantir la sécurité des données, la traçabilité complète et la conformité réglementaire. | SD-AXA-06 (Traçabilité, Sécurité et Conformité) | SIL, Biologistes, Techniciens de laboratoire, Autorités réglementaires | Audit trail, Chiffrement des données, Logs d’audit, Conservation des données (10 ans) | Toutes les actions sont tracées, sécurisées et conformes aux normes (ISO 15189, RGPD). |

---

---

## **3. Détail des Bounded Contexts candidats**

---

### **3.1. BC-AXA-01 : Prescription Clinique**
**Type** : Cœur stratégique
**Responsabilité principale** :
Gérer la **prescription électronique** des dosages anti-Xa en urgence et valider leur **pertinence clinique** selon les protocoles locaux (CAI) et les recommandations HAS/ANSM.

---

#### **Sous-domaines couverts**
- **SD-AXA-01** : Prescription et Validation Clinique

---

#### **Acteurs principaux**
| **Acteur** | **Rôle dans le contexte** | **Source** |
|------------|---------------------------|------------|
| **Cliniciens prescripteurs** | Prescrire un dosage anti-Xa en urgence via une prescription électronique dans le SIL. Saisir les **données contextuelles** (type d’AOD, posologie, heure de dernière prise, fonction rénale, contexte clinique). Respecter les **protocoles locaux** ou recommandations HAS/ANSM. | `02_acteurs_du_domaine.md`, `03_concepts_metier_initiaux.md`, `05_vision_globale_du_domaine.md` |
| **Biologistes médicaux** | Valider ou rejeter une demande de dosage selon des critères cliniques et réglementaires. Vérifier la **cohérence** de la prescription avec les protocoles locaux. Justifier un rejet si nécessaire. | `02_acteurs_du_domaine.md`, `04_regles_metier.md` |
| **Commission des Anti-infectieux et des Anticoagulants (CAI)** | Définir les **protocoles locaux** pour la prescription des dosages anti-Xa. Mettre à jour ces protocoles en fonction des dernières recommandations. | `02_acteurs_du_domaine.md` |

---

#### **Concepts métier centraux manipulés**
| **Concept** | **Définition** | **Exemples** | **Source** |
|-------------|----------------|--------------|------------|
| **Prescription électronique** | Demande formalisée dans le SIL, avec les informations nécessaires à la prise en charge du dosage. | - Identité du patient <br> - Service prescripteur <br> - Contexte clinique (ex. : hémorragie active) <br> - Type d’AOD (apixaban, rivaroxaban, édoxaban) <br> - Posologie et heure de la dernière prise <br> - Clairance de la créatinine | `03_concepts_metier_initiaux.md`, `04_regles_metier.md` |
| **Protocoles locaux (CAI)** | Ensemble de règles définies par la CAI pour encadrer la prescription des dosages anti-Xa. | - Indications de dosage (ex. : hémorragie active) <br> - Contre-indications <br> - Posologies recommandées | `02_acteurs_du_domaine.md` |
| **Validation biologique** | Contrôle réalisé par le biologiste pour confirmer qu’une demande peut être traitée. | - Statut : "validée" ou "rejetée" <br> - Motif de rejet (ex. : "hors protocole CAI") | `02_acteurs_du_domaine.md`, `04_regles_metier.md` |
| **Contexte clinique** | Informations médicales nécessaires pour comprendre et justifier la prescription. | - Motif de la demande (ex. : hémorragie active) <br> - Autres traitements (ex. : antiagrégants) <br> - Antécédents médicaux pertinents | `03_concepts_metier_initiaux.md` |

---

#### **Règles métier spécifiques au contexte**
| **ID** | **Règle métier** | **Description** | **Acteurs concernés** | **Conditions d’application** | **Conséquences en cas de non-respect** | **Source** |
|--------|------------------|-----------------|-----------------------|-----------------------------|----------------------------------------|------------|
| **RBC-01-01** | **Prescription électronique obligatoire** | Toute demande de dosage anti-Xa doit être formalisée via une prescription électronique dans le SIL. Les prescriptions papier sont **interdites**. | Cliniciens prescripteurs, SIL | - Patient sous AOD <br> - Contexte clinique justifiant le dosage (ex. : hémorragie active) | - Risque de perte de traçabilité <br> - Erreur de transcription <br> - Non-respect des protocoles locaux | `02_acteurs_du_domaine.md`, `03_concepts_metier_initiaux.md`, `05_vision_globale_du_domaine.md` |
| **RBC-01-02** | **Respect des protocoles locaux (CAI)** | La prescription doit respecter les indications définies par les protocoles de la CAI. Toute demande en dehors de ces indications doit être **justifiée et validée par un biologiste**. | Cliniciens prescripteurs, Biologistes médicaux, CAI | - Protocoles locaux en vigueur <br> - Recommandations HAS/ANSM | - Prescription inappropriée → risque clinique <br> - Non-conformité réglementaire <br> - Surcharge du laboratoire | `02_acteurs_du_domaine.md`, `04_regles_metier.md` |
| **RBC-01-03** | **Validation biologique obligatoire** | Toute demande de dosage anti-Xa doit être validée par un biologiste avant analyse. Les demandes non validées sont **bloquées automatiquement** dans le SIL. | Biologistes médicaux, SIL | - Demande reçue dans le SIL <br> - Données contextuelles complètes | - Analyse non pertinente → résultat inutilisable <br> - Retard dans la prise en charge <br> - Perte de temps pour le laboratoire | `02_acteurs_du_domaine.md`, `04_regles_metier.md` |
| **RBC-01-04** | **Exhaustivité des données contextuelles** | Les données contextuelles (type d’AOD, posologie, heure de la dernière prise, fonction rénale, contexte clinique) doivent être **saisies ou récupérées automatiquement** à 100% pour permettre une validation pertinente. | Cliniciens prescripteurs, SIL, DPI | - Données disponibles dans le DPI (fonction rénale, traitements) <br> - Intégration automatique avec le SIL | - Données incomplètes → interprétation erronée <br> - Risque clinique pour le patient <br> - Non-conformité réglementaire | `03_concepts_metier_initiaux.md`, `04_contraintes_et_risques.md`, `05_vision_globale_du_domaine.md` |

---

#### **Décisions clés dans le contexte**
| **Décision** | **Acteur responsable** | **Informations nécessaires** | **Informations produites** | **Dépendances** |
|--------------|------------------------|-----------------------------|----------------------------|-----------------|
| Valider une prescription | Biologiste | Prescription électronique, contexte clinique, protocoles CAI | Statut : "validée" ou "rejetée" (avec motif) | - Données contextuelles complètes <br> - Respect des protocoles locaux |
| Demander un complément | Biologiste | Prescription incomplète ou non conforme | Demande de complément au clinicien | - Protocoles locaux <br> - Disponibilité des ressources |

---
#### **Contrat d’échange avec d’autres contextes**
| **Contexte source** | **Contexte cible** | **Données échangées** | **Format** | **Fréquence** | **Risque si non respecté** |
|---------------------|--------------------|-----------------------|-------------|----------------|----------------------------|
| **BC-AXA-01** | **BC-AXA-02** | Prescription validée (avec données contextuelles) | JSON/XML (SIL → SIL) | En temps réel | Échantillon non conforme → résultat invalide |
| **BC-AXA-01** | **BC-AXA-03** | Prescription validée (avec niveau d’urgence) | JSON/XML (SIL → SIL) | En temps réel | Priorisation erronée → retard critique |
| **BC-AXA-01** | **BC-AXA-06** | Motif de rejet ou demande de complément | Message structuré (SIL → Cliniciens) | Immédiat | Non-respect des protocoles → risque réglementaire |

---
#### **Hypothèses de découpage à valider**
| **Hypothèse** | **Description** | **Questions clés à poser aux experts métier** |
|---------------|-----------------|-----------------------------------------------|
| **Autorité finale en cas de désaccord** | En cas de désaccord entre clinicien et biologiste sur la pertinence d’une prescription, qui tranche ? | - Qui a l’autorité finale en cas de divergence ? <br> - Existe-t-il une procédure d’escalade formalisée ? |
| **Flexibilité des protocoles** | Les cliniciens peuvent-ils adapter les traitements en fonction de leur expertise, ou les protocoles sont-ils stricts ? | - Quels sont les **cas d’exception** autorisés par la CAI ? <br> - Comment documenter ces exceptions ? |
| **Gestion des données manquantes** | Que faire si une donnée contextuelle est manquante (ex. : heure de la dernière prise non saisie) ? | - Le SIL doit-il **bloquer automatiquement** la demande ? <br> - Comment **notifier le clinicien** en cas de donnée manquante ? |

---
---

### **3.2. BC-AXA-02 : Gestion Pré-Analytique**
**Type** : Support
**Responsabilité principale** :
Vérifier la **conformité des échantillons biologiques** (tubes) avant analyse et gérer les **non-conformités** selon les exigences réglementaires (ISO 15189, RGPD).

---

#### **Sous-domaines couverts**
- **SD-AXA-02** : Gestion Pré-Analytique des Échantillons

---
#### **Acteurs principaux**
| **Acteur** | **Rôle dans le contexte** | **Source** |
|------------|---------------------------|------------|
| **Techniciens de laboratoire** | Vérifier la conformité des tubes (type, volume, conditions de transport) à réception dans le SIL. Signaler les non-conformités (ex. : délai de transport dépassé) aux biologistes et au SIL. Archiver les échantillons non conformes avec motif. | `02_acteurs_du_domaine.md`, `04_regles_metier.md` |
| **Biologistes médicaux** | Valider définitivement la conformité d’un tube ou rejeter un échantillon non conforme. | `02_acteurs_du_domaine.md` |
| **Système d’Information de Laboratoire (SIL)** | Intégrer un **module de vérification automatique** des conformités pré-analytiques (ex. : alerte si type de tube incorrect). Bloquer l’analyse si un tube est non conforme. Notifier les acteurs concernés (prescripteur, biologiste). | `02_acteurs_du_domaine.md`, `03_concepts_metier_initiaux.md`, `07_base_modelisation_comportementale.md` |
| **Commission des Anti-infectieux et des Anticoagulants (CAI)** | Définir les **critères exacts de conformité** des tubes (ex. : tube citraté 3.2%, volume minimal 1.8 mL). | `04_contraintes_et_risques.md` |

---
#### **Concepts métier centraux manipulés**
| **Concept** | **Définition** | **Exemples** | **Source** |
|-------------|----------------|--------------|------------|
| **Tube citraté 3.2%** | Type de tube de prélèvement sanguin requis pour le dosage anti-Xa. | - BD Vacutainer 9NC 3.2% <br> - Volume minimal : 1.8 mL | `04_contraintes_et_risques.md` |
| **Volume minimal** | Volume sanguin minimal requis dans le tube pour une analyse valide. | - 1.8 mL (pour l’analyseur ACL TOP) <br> - 2.7 mL (pour l’analyseur STA R Max) | Hypothèse basée sur les bonnes pratiques de laboratoire |
| **Délai maximal entre prélèvement et analyse** | Temps maximal autorisé entre le prélèvement et l’analyse pour garantir la validité de l’échantillon. | - < 4 heures <br> - Température entre 15°C et 25°C <br> - Protection de la lumière | `04_contraintes_et_risques.md` |
| **Non-conformité** | Situation où un échantillon ne respecte pas les exigences pré-analytiques. | - Type de tube incorrect (ex. : EDTA au lieu de citraté) <br> - Volume insuffisant <br> - Délai de transport dépassé | `04_contraintes_et_risques.md` |

---
#### **Règles métier spécifiques au contexte**
| **ID** | **Règle métier** | **Description** | **Acteurs concernés** | **Conditions d’application** | **Conséquences en cas de non-respect** | **Source** |
|--------|------------------|-----------------|-----------------------|-----------------------------|----------------------------------------|------------|
| **RBC-02-01** | **Type de tube exact requis** | Le tube de prélèvement doit être de type **citraté 3.2%** (ex. : BD Vacutainer 9NC 3.2%). Tout autre type de tube (ex. : EDTA, héparine) est **interdit** et entraîne un rejet systématique. | Cliniciens prescripteurs, Techniciens de laboratoire, SIL, CAI | - Patient sous AOD nécessitant un dosage anti-Xa <br> - Protocoles locaux de la CAI définissant le type de tube | - Analyse d’un échantillon non conforme → résultat invalide <br> - Risque clinique pour le patient (ex. : surdosage non détecté) <br> - Non-conformité réglementaire (ISO 15189) | `04_contraintes_et_risques.md`, `03_concepts_metier_initiaux.md` |
| **RBC-02-02** | **Volume minimal requis** | Le volume sanguin minimal requis dans le tube est de **1.8 mL** (ex. : pour l’analyseur ACL TOP). Tout volume inférieur est **interdit** et entraîne un rejet systématique. | Cliniciens prescripteurs, Techniciens de laboratoire, SIL | - Type de tube correct (citraté 3.2%) <br> - Protocoles locaux de la CAI définissant le volume minimal | - Analyse d’un échantillon non conforme → résultat invalide <br> - Perte de temps pour le laboratoire <br> - Frustration des cliniciens | Hypothèse basée sur `04_contraintes_et_risques.md` et bonnes pratiques de laboratoire |
| **RBC-02-03** | **Délai maximal entre prélèvement et analyse** | Le délai maximal entre le prélèvement sanguin et l’analyse du dosage anti-Xa est de **< 4 heures**. Tout délai dépassé est **interdit** et entraîne un rejet systématique. | Techniciens de laboratoire, SIL, Personnel administratif | - Type de tube correct <br> - Volume minimal respecté <br> - Protocoles locaux de la CAI définissant le délai maximal | - Analyse d’un échantillon dégradé → résultat invalide <br> - Risque clinique pour le patient (ex. : hémorragie non contrôlée) <br> - Non-conformité réglementaire | `04_contraintes_et_risques.md`, `03_concepts_metier_initiaux.md` |
| **RBC-02-04** | **Conditions de transport strictes** | Les tubes de prélèvement doivent être transportés dans des conditions strictes : **température entre 15°C et 25°C**, **protection de la lumière**, et **délai maximal de 4 heures**. Tout écart est **interdit** et entraîne un rejet systématique. | Personnel administratif, Techniciens de laboratoire, SIL | - Type de tube correct <br> - Volume minimal respecté <br> - Protocoles locaux de la CAI définissant les conditions de transport | - Analyse d’un échantillon dégradé → résultat invalide <br> - Risque clinique pour le patient <br> - Non-conformité réglementaire | Hypothèse basée sur `04_contraintes_et_risques.md` et bonnes pratiques pré-analytiques |
| **RBC-02-05** | **Validation partagée des tubes** | La conformité d’un tube est **validée en deux étapes** : <br> 1. Par le **clinicien prescripteur** avant envoi (contrôle visuel et vérification du volume). <br> 2. Par le **technicien de laboratoire** à réception (contrôle du type de tube, du volume, et du délai de transport). <br> En cas de désaccord, le **biologiste** tranche définitivement. | Cliniciens prescripteurs, Techniciens de laboratoire, Biologistes médicaux | - Tube reçu au laboratoire <br> - Données de transport disponibles (ex. : horodatage) | - Perte de temps pour le laboratoire <br> - Risque de rejet d’un échantillon conforme <br> - Frustration des acteurs | `02_acteurs_du_domaine.md`, `04_regles_metier.md` |

---
#### **Décisions clés dans le contexte**
| **Décision** | **Acteur responsable** | **Informations nécessaires** | **Informations produites** | **Dépendances** |
|--------------|------------------------|-----------------------------|----------------------------|-----------------|
| Vérifier la conformité d’un tube | Technicien/Biologiste | Type de tube, volume, conditions de transport, temps écoulé | Statut : "conforme" ou "non conforme" | - Critères de conformité validés par la CAI |
| Rejeter un échantillon non conforme | Biologiste | Non-conformité détectée, protocole de gestion | Motif du rejet, demande de nouveau prélèvement | - Procédure de rejet claire et validée |

---
#### **Contrat d’échange avec d’autres contextes**
| **Contexte source** | **Contexte cible** | **Données échangées** | **Format** | **Fréquence** | **Risque si non respecté** |
|---------------------|--------------------|-----------------------|-------------|----------------|----------------------------|
| **BC-AXA-01** | **BC-AXA-02** | Prescription validée (avec données contextuelles) | JSON/XML (SIL → SIL) | En temps réel | Échantillon non conforme → résultat invalide |
| **BC-AXA-02** | **BC-AXA-04** | Échantillon conforme (avec statut) | JSON/XML (SIL → SIL) | En temps réel | Analyse non réalisée → retard critique |
| **BC-AXA-02** | **BC-AXA-06** | Motif de rejet ou demande de complément | Message structuré (SIL → Cliniciens) | Immédiat | Non-respect des protocoles → risque réglementaire |

---
#### **Hypothèses de découpage à valider**
| **Hypothèse** | **Description** | **Questions clés à poser aux experts métier** |
|---------------|-----------------|-----------------------------------------------|
| **Critères de conformité par AOD** | Les exigences pré-analytiques (type de tube, volume, délai) peuvent varier selon le type d’AOD (apixaban vs. rivaroxaban). | - Quels sont les **critères exacts** pour chaque AOD ? <br> - Comment **afficher ces critères** dans le SIL pour guider les techniciens ? |
| **Responsabilité en cas de non-conformité** | Qui est responsable de la relance ou de la demande de complément en cas de tube non conforme ? | - Quel est le **délai maximal** pour notifier une non-conformité au clinicien ? <br> - Comment **archiver les non-conformités** pour les audits ? |
| **Gestion des exceptions pré-analytiques** | Comment gérer les cas particuliers (ex. : patient en pédiatrie, volume minimal < 1 mL) ? | - Quels sont les **cas d’exception** autorisés ? <br> - Comment **former les techniciens** aux exigences spécifiques ? |

---
---

### **3.3. BC-AXA-03 : Ordonnancement et Priorisation**
**Type** : Cœur stratégique
**Responsabilité principale** :
Classer les **demandes de dosage anti-Xa** par **niveau d’urgence clinique** et ordonnancer les analyses en fonction des **ressources disponibles** (techniciens, analyseurs) et des **délais critiques**.

---
#### **Sous-domaines couverts**
- **SD-AXA-03** : Ordonnancement et Priorisation

---
#### **Acteurs principaux**
| **Acteur** | **Rôle dans le contexte** | **Source** |
|------------|---------------------------|------------|
| **Biologistes médicaux** | Valider ou ajuster manuellement la priorisation des demandes. Ordonnancer les analyses en fonction des ressources disponibles et des **délais critiques**. Superviser le traitement des demandes urgentes. | `02_acteurs_du_domaine.md`, `04_regles_metier.md` |
| **Système d’Information de Laboratoire (SIL)** | Classer automatiquement les demandes par niveau d’urgence en fonction de **règles métiers prédéfinies** (ex. : hémorragie active = urgence absolue). Ordonnancer les analyses en fonction des ressources disponibles. Notifier les acteurs concernés (biologistes, techniciens) en cas de criticité. | `02_acteurs_du_domaine.md`, `03_concepts_metier_initiaux.md`, `05_vision_globale_du_domaine.md`, `07_base_modelisation_comportementale.md` |
| **Systèmes d’alerte et de priorisation** | Appliquer les règles de priorisation et envoyer des alertes aux acteurs concernés. | Hypothèse basée sur `02_acteurs_du_domaine.md` et `05_vision_globale_du_domaine.md` |
| **Commission des Anti-infectieux et des Anticoagulants (CAI)** | Définir les **critères exacts de priorisation** (ex. : hémorragie active = urgence absolue) et les **délais maximaux acceptables** pour chaque niveau de priorité. | `04_regles_metier.md`, `05_priorites_exceptions_contraintes.md` |

---
#### **Concepts métier centraux manipulés**
| **Concept** | **Définition** | **Exemples** | **Source** |
|-------------|----------------|--------------|------------|
| **Niveau d’urgence** | Classement des demandes selon leur degré d’urgence clinique. | - Urgence Absolue (≤1 heure) <br> - Urgence Haute (≤4 heures) <br> - Urgence Modérée (≤24 heures) <br> - Routine (≤48 heures) | `05_priorites_exceptions_contraintes.md` |
| **Délai critique** | Fenêtre de temps maximale acceptable entre la prescription et la transmission des résultats. | - Hémorragie active : ≤1 heure <br> - Chirurgie en urgence : ≤4 heures | `01_reformulation_du_besoin.md`, `04_contraintes_et_risques.md` |
| **Ordonnancement** | Planification des analyses en fonction des ressources disponibles et des priorités. | - Planning des analyses <br> - Statut des demandes : "en attente", "en cours", "terminée" | Hypothèse basée sur `02_acteurs_du_domaine.md` |
| **Conflit de priorité** | Situation où plusieurs demandes ont le même niveau de priorité (ex. : deux urgences absolues simultanées). | - Autorité finale en cas de conflit <br> - Règles d’escalade | `06_conflits_objectifs_arbitrages.md` |

---
#### **Règles métier spécifiques au contexte**
| **ID**