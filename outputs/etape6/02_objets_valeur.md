# **Objets Valeur du Domaine**
**Domaine métier** : Gestion des demandes urgentes de dosage anti-Xa dans le SIL
**Date** : 2024-06-15
**Version** : 1.0
**Auteurs** : Architecte DDD
**Sources** : Livrables étape 5 (`01_contextes_candidats.md`, `02_frontieres_responsabilites_contextes.md`, `03_vocabulaire_modeles_par_contexte.md`, `04_dependances_contrats_contextes.md`, `05_risques_arbitrages_contextes.md`, `06_cartographie_bounded_contexts.md`, `07_synthese_bounded_contexts.md`)

---

---

## **1. Introduction**
Ce document identifie et formalise les **objets valeur** du domaine pour chaque **Bounded Context (BC)** du système de gestion des demandes urgentes de dosage anti-Xa. Les objets valeur sont des **concepts immuables**, définis uniquement par leurs attributs, et utilisés pour encapsuler des propriétés métier essentielles (résultats de mesure, plages de valeurs, contexte clinique, périodes temporelles, etc.).

**Objectifs** :
- Clarifier les **concepts immuables** du domaine.
- Définir les **règles d'égalité/comparaison** métier.
- Identifier les **contraintes de validité** et les **règles de construction**.
- Mettre en évidence les **objets valeur partagés** entre contextes et les **risques d'ambiguïté**.
- Fournir une base pour la **modélisation comportementale** et la **conception des services de domaine**.

**Méthodologie** :
- Pour chaque BC, identifier les objets valeur en analysant les **concepts métier centraux** et les **règles de gestion**.
- Définir les **attributs** et leur **type métier**.
- Spécifier les **règles d'égalité** (quand deux objets valeur sont considérés comme égaux ?).
- Documenter les **contraintes de validité** (ex: plage de valeurs, format).
- Identifier les **objets valeur partagés** entre BCs et les **risques d'ambiguïté sémantique**.

---

---

## **2. BC-AXA-01 : Prescription Clinique**
**Type** : Cœur stratégique
**Responsabilité principale** :
Gérer la **prescription électronique** des dosages anti-Xa en urgence et valider leur **pertinence clinique** selon les protocoles locaux (CAI) et les recommandations HAS/ANSM.

---

### **2.1. Objets Valeur Identifiés**

| **Objet Valeur** | **Description** | **Attributs** | **Type** | **Règle d'égalité** | **Contraintes de validité** | **Règles de construction** | **Porté par** |
|------------------|-----------------|---------------|----------|---------------------|-----------------------------|-----------------------------|----------------|
| **PrescriptionStatus** | Statut d'une prescription. | `status` | Enum | Deux objets sont égaux si leur `status` est identique. | `status` ∈ {`pending`, `validated`, `rejected`, `incomplete`} | Généré automatiquement par le SIL lors de la création ou de la validation. | `Prescription` (agrégat) |
| **AODType** | Type d'anticoagulant oral direct prescrit. | `type` | Enum | Deux objets sont égaux si leur `type` est identique. | `type` ∈ {`Apixaban`, `Rivaroxaban`, `Edoxaban`} | Saisi par le clinicien ou récupéré automatiquement depuis le DPI. | `AODDetails` (entité) |
| **ClinicalContextType** | Type de contexte clinique justifiant la prescription. | `type` | Enum | Deux objets sont égaux si leur `type` est identique. | `type` ∈ {`ActiveHemorrhage`, `PreSurgery`, `PostSurgery`, `RoutineMonitoring`, `Other`} | Déduit du motif de la prescription ou saisi par le clinicien. | `ClinicalContext` (entité) |
| **ProtocolCompliance** | Conformité de la prescription aux protocoles CAI. | `isCompliant` | Boolean | Deux objets sont égaux si leur `isCompliant` est identique. | `isCompliant` ∈ {`true`, `false`} | Calculé automatiquement par le SIL en comparant la prescription aux protocoles CAI. | `PrescriptionProtocol` (entité) |
| **DosageUnit** | Unité de mesure de la posologie (mg ou UI). | `unit` | Enum | Deux objets sont égaux si leur `unit` est identique. | `unit` ∈ {`mg`, `UI`} | Déduit du type d'AOD (ex: apixaban en mg, héparine en UI). | `AODDetails` (entité) |
| **TimeWindow** | Fenêtre temporelle critique pour la prescription. | `startTime`, `endTime` | DateTime | Deux objets sont égaux si leurs `startTime` et `endTime` sont identiques. | `startTime` < `endTime` | Calculé en fonction du `clinicalContextType` (ex: 1h pour `ActiveHemorrhage`). | `Prescription` (agrégat) |

---

### **2.2. Contraintes et Règles Métier Associées**
1. **PrescriptionStatus** :
   - Une prescription ne peut être transmise à BC-AXA-02 ou BC-AXA-03 que si son `status` est `validated`.
   - **Règle de construction** : Le statut passe à `validated` uniquement après validation biologique (`RBC-01-03`).

2. **AODType** :
   - Le type d'AOD doit être **cohérent** avec le contexte clinique (ex: apixaban pour une hémorragie active).
   - **Règle de construction** : Le SIL vérifie la cohérence entre `AODType` et `ClinicalContextType` (`RBC-01-02`).

3. **ClinicalContextType** :
   - Le contexte clinique doit être **exhaustif** et **justifié** (ex: `ActiveHemorrhage` nécessite une description détaillée).
   - **Règle de construction** : Le clinicien doit saisir une `description` si `type` est `Other`.

4. **ProtocolCompliance** :
   - Une prescription est considérée comme `nonCompliant` si elle ne respecte pas les protocoles CAI (`RBC-01-02`).
   - **Règle de construction** : Le SIL compare automatiquement la prescription aux protocoles CAI.

5. **DosageUnit** :
   - L'unité doit être **cohérente** avec le type d'AOD (ex: apixaban en mg, héparine en UI).
   - **Règle de construction** : Le SIL déduit l'unité depuis une table de correspondance (ex: `AODType → DosageUnit`).

6. **TimeWindow** :
   - La fenêtre temporelle doit être **calculée** en fonction du contexte clinique (ex: 1h pour `ActiveHemorrhage`).
   - **Règle de construction** : Le SIL utilise une **grille de priorisation** définie par la CAI.

---

### **2.3. Objets Valeur Partagés ou Ambiguës**
| **Objet Valeur** | **BCs Partagés** | **Ambiguïté** | **Solution Proposée** |
|------------------|------------------|---------------|-----------------------|
| **AODType** | BC-AXA-01, BC-AXA-05 | Dans BC-AXA-01 = type de l'AOD prescrit. Dans BC-AXA-05 = type de l'AOD pour l'interprétation. | Utiliser un **identifiant unique** pour chaque AOD (ex: `AODTypeId`) et une **table de correspondance** partagée. |
| **ClinicalContextType** | BC-AXA-01, BC-AXA-05 | Dans BC-AXA-01 = contexte clinique justifiant la prescription. Dans BC-AXA-05 = contexte clinique pour l'interprétation. | Centraliser la définition des contextes cliniques dans un **glossaire métier partagé**. |
| **TimeWindow** | BC-AXA-01, BC-AXA-03 | Dans BC-AXA-01 = fenêtre temporelle critique pour la prescription. Dans BC-AXA-03 = délai maximal pour l'ordonnancement. | Renommer en **CriticalTimeWindow** dans BC-AXA-01 et **MaxDeadline** dans BC-AXA-03 pour éviter les ambiguïtés. |

---

---

## **3. BC-AXA-02 : Gestion Pré-Analytique**
**Type** : Support
**Responsabilité principale** :
Vérifier la **conformité des échantillons biologiques** (tubes) avant analyse et gérer les **non-conformités** selon les exigences réglementaires (ISO 15189, RGPD).

---

### **3.1. Objets Valeur Identifiés**

| **Objet Valeur** | **Description** | **Attributs** | **Type** | **Règle d'égalité** | **Contraintes de validité** | **Règles de construction** | **Porté par** |
|------------------|-----------------|---------------|----------|---------------------|-----------------------------|-----------------------------|----------------|
| **SampleStatus** | Statut de conformité d'un échantillon. | `status` | Enum | Deux objets sont égaux si leur `status` est identique. | `status` ∈ {`pending`, `conforme`, `nonConforme`, `invalid`} | Généré automatiquement par le SIL après vérification pré-analytique. | `Sample` (agrégat) |
| **TubeType** | Type de tube de prélèvement sanguin. | `type`, `minimalVolume`, `description` | Enum + Double + String | Deux objets sont égaux si leur `type` est identique. | `type` ∈ {`Citrate3.2%`, `EDTA`, `Heparin`}, `minimalVolume` > 0 | Déduit du type de tube utilisé pour le prélèvement. | `TubeType` (entité) |
| **TransportConditions** | Conditions de transport de l'échantillon. | `transportTimeHours`, `temperatureMin`, `temperatureMax` | Double + Double + Double | Deux objets sont égaux si tous leurs attributs sont identiques. | `transportTimeHours` ≤ 4, `15` ≤ `temperatureMin` ≤ `temperatureMax` ≤ `25` | Mesuré par le SIL ou saisi par le technicien. | `TransportConditions` (entité) |
| **NonConformityReason** | Motif de non-conformité d'un échantillon. | `reason` | Enum | Deux objets sont égaux si leur `reason` est identique. | `reason` ∈ {`incorrectTubeType`, `insufficientVolume`, `transportTimeExceeded`, `temperatureOutOfRange`, `other`} | Généré automatiquement par le SIL ou saisi par le technicien. | `Sample` (agrégat) |
| **PreAnalyticalWindow** | Fenêtre temporelle critique pour la conformité pré-analytique. | `maxTransportTime`, `maxTemperatureDeviation` | Double + Double | Deux objets sont égaux si leurs attributs sont identiques. | `maxTransportTime` = 4, `maxTemperatureDeviation` = 2°C | Déduit des protocoles CAI (`RBC-02-03`, `RBC-02-04`). | `Sample` (agrégat) |

---

### **3.2. Contraintes et Règles Métier Associées**
1. **SampleStatus** :
   - Un échantillon ne peut être transmis à BC-AXA-04 que si son `status` est `conforme`.
   - **Règle de construction** : Le statut passe à `conforme` uniquement si tous les critères de conformité sont respectés (`RBC-02-01` à `RBC-02-04`).

2. **TubeType** :
   - Le type de tube doit être **exactement** `Citrate3.2%` pour les dosages anti-Xa (`RBC-02-01`).
   - **Règle de construction** : Le SIL vérifie automatiquement le type de tube via un **scanner de codes-barres**.

3. **TransportConditions** :
   - Les conditions de transport doivent respecter les **exigences réglementaires** (ISO 15189).
   - **Règle de construction** : Le SIL enregistre automatiquement la température et l'heure de transport via des capteurs connectés.

4. **NonConformityReason** :
   - Le motif de non-conformité doit être **justifié** et **documenté** pour les audits.
   - **Règle de construction** : Le SIL génère automatiquement le motif si un critère est violé (ex: `insufficientVolume`).

5. **PreAnalyticalWindow** :
   - La fenêtre temporelle critique doit être **calculée** en fonction des protocoles CAI.
   - **Règle de construction** : Le SIL utilise une **grille de conformité pré-analytique** définie par la CAI.

---

### **3.3. Objets Valeur Partagés ou Ambiguës**
| **Objet Valeur** | **BCs Partagés** | **Ambiguïté** | **Solution Proposée** |
|------------------|------------------|---------------|-----------------------|
| **TubeType** | BC-AXA-02, BC-AXA-08 | Dans BC-AXA-02 = type de tube pour la conformité. Dans BC-AXA-08 = type de tube pour l'intégration des données. | Utiliser un **identifiant unique** pour chaque type de tube (ex: `TubeTypeId`) et une **table de correspondance** partagée. |
| **NonConformityReason** | BC-AXA-02, BC-AXA-07 | Dans BC-AXA-02 = motif de rejet d'un échantillon. Dans BC-AXA-07 = motif d'alerte sur un résultat aberrant. | Renommer en **SampleNonConformityReason** dans BC-AXA-02 et **ResultAlertReason** dans BC-AXA-07 pour éviter les ambiguïtés. |

---

---

## **4. BC-AXA-03 : Ordonnancement et Priorisation**
**Type** : Cœur stratégique
**Responsabilité principale** :
Classer les **demandes de dosage anti-Xa** par **niveau d'urgence clinique** et ordonnancer les analyses en fonction des **ressources disponibles** (techniciens, analyseurs) et des **délais critiques**.

---

### **4.1. Objets Valeur Identifiés**

| **Objet Valeur** | **Description** | **Attributs** | **Type** | **Règle d'égalité** | **Contraintes de validité** | **Règles de construction** | **Porté par** |
|------------------|-----------------|---------------|----------|---------------------|-----------------------------|-----------------------------|----------------|
| **UrgencyLevel** | Niveau d'urgence clinique d'une demande. | `level` | Enum | Deux objets sont égaux si leur `level` est identique. | `level` ∈ {`ABSOLUTE`, `HIGH`, `MODERATE`, `ROUTINE`} | Calculé automatiquement par le SIL en fonction du `clinicalContextType` et des protocoles CAI. | `Request` (agrégat) |
| **MaxDeadline** | Délai maximal acceptable pour traiter une demande. | `deadline` | DateTime | Deux objets sont égaux si leur `deadline` est identique. | `deadline` > `currentTime` | Calculé en fonction du `UrgencyLevel` (ex: 1h pour `ABSOLUTE`). | `Request` (agrégat) |
| **PriorityScore** | Score de priorité calculé pour arbitrer les conflits. | `score` | Integer | Deux objets sont égaux si leur `score` est identique. | `score` ∈ [0, 100] | Calculé par le SIL en fonction de l'`UrgencyLevel`, du `MaxDeadline`, et des ressources disponibles. | `Request` (agrégat) |
| **ResourceType** | Type de ressource critique (technicien ou analyseur). | `type` | Enum | Deux objets sont égaux si leur `type` est identique. | `type` ∈ {`TECHNICIAN`, `ANALYZER`} | Déduit du type de demande (ex: analyseur pour BC-AXA-04). | `ResourceAllocation` (entité) |
| **SchedulingWindow** | Fenêtre temporelle disponible pour l'ordonnancement. | `startTime`, `endTime` | DateTime | Deux objets sont égaux si leurs attributs sont identiques. | `startTime` < `endTime` | Calculé en fonction des plannings de ressources (BC-AXA-09). | `Request` (agrégat) |

---
### **4.2. Contraintes et Règles Métier Associées**
1. **UrgencyLevel** :
   - Le niveau d'urgence doit être **calculé automatiquement** en fonction du contexte clinique (`RBC-03-01`).
   - **Règle de construction** : Le SIL utilise une **grille de priorisation** définie par la CAI.

2. **MaxDeadline** :
   - Le délai maximal doit être **respecté** pour éviter les retards critiques.
   - **Règle de construction** : Le SIL déclenche une **alerte** si le délai est dépassé (`RBC-03-02`).

3. **PriorityScore** :
   - Le score de priorité doit être **recalculé** en cas de conflit (ex: deux demandes `ABSOLUTE` simultanées).
   - **Règle de construction** : Le SIL utilise un **algorithme de priorisation** (ex: score = `UrgencyLevel.weight + MaxDeadline.urgency`).

4. **ResourceType** :
   - Le type de ressource doit être **cohérent** avec la demande (ex: analyseur pour BC-AXA-04).
   - **Règle de construction** : Le SIL vérifie la disponibilité des ressources avant ordonnancement.

5. **SchedulingWindow** :
   - La fenêtre temporelle doit être **disponible** pour l'ordonnancement.
   - **Règle de construction** : Le SIL consulte le planning des ressources (BC-AXA-09) pour déterminer la fenêtre.

---
### **4.3. Objets Valeur Partagés ou Ambiguës**
| **Objet Valeur** | **BCs Partagés** | **Ambiguïté** | **Solution Proposée** |
|------------------|------------------|---------------|-----------------------|
| **UrgencyLevel** | BC-AXA-03, BC-AXA-06 | Dans BC-AXA-03 = niveau d'urgence pour l'ordonnancement. Dans BC-AXA-06 = niveau d'urgence pour les alertes. | Utiliser un **identifiant unique** pour chaque niveau d'urgence (ex: `UrgencyLevelId`) et une **table de correspondance** partagée. |
| **MaxDeadline** | BC-AXA-03, BC-AXA-05 | Dans BC-AXA-03 = délai maximal pour l'ordonnancement. Dans BC-AXA-05 = délai maximal pour l'interprétation. | Renommer en **SchedulingDeadline** dans BC-AXA-03 et **InterpretationDeadline** dans BC-AXA-05. |

---

---

## **5. BC-AXA-04 : Analyse Laboratoire**
**Type** : Support
**Responsabilité principale** :
Réaliser les **dosages anti-Xa** sur les échantillons conformes et transmettre les **résultats bruts** de manière fiable et traçable au SIL.

---
### **5.1. Objets Valeur Identifiés**

| **Objet Valeur** | **Description** | **Attributs** | **Type** | **Règle d'égalité** | **Contraintes de validité** | **Règles de construction** | **Porté par** |
|------------------|-----------------|---------------|----------|---------------------|-----------------------------|-----------------------------|----------------|
| **AnalysisStatus** | Statut d'une analyse. | `status` | Enum | Deux objets sont égaux si leur `status` est identique. | `status` ∈ {`PENDING`, `ANALYZED`, `ABNORMAL`, `VALIDATED`} | Généré automatiquement par l'analyseur ou le SIL. | `Analysis` (agrégat) |
| **AnalyzerId** | Identifiant unique de l'analyseur. | `id` | String | Deux objets sont égaux si leur `id` est identique. | `id` ∈ [format alphanumérique] | Saisi par le technicien ou récupéré automatiquement depuis l'analyseur. | `Analyzer` (entité) |
| **AntiXaUnit** | Unité de mesure du résultat anti-Xa. | `unit` | Enum | Deux objets sont égaux si leur `unit` est identique. | `unit` ∈ {`UI/mL`, `ng/mL`} | Déduit du type d'analyseur (ex: ACL TOP utilise `UI/mL`). | `Analysis` (agrégat) |
| **QualityControl** | Résultat du contrôle qualité de l'analyseur. | `isPassed`, `controlValue` | Boolean + Double | Deux objets sont égaux si leurs attributs sont identiques. | `isPassed` ∈ {`true`, `false`}, `controlValue` ∈ [plage de validité] | Généré automatiquement par l'analyseur après chaque série de tests. | `Analysis` (agrégat) |
| **ResultRange** | Plage de valeurs normales pour un résultat anti-Xa. | `minValue`, `maxValue`, `aodType` | Double + Double + AODType | Deux objets sont égaux si leurs attributs sont identiques. | `minValue` < `maxValue`, `aodType` ∈ {`Apixaban`, `Rivaroxaban`, `Edoxaban`} | Déduit des **grilles d'interprétation** (BC-AXA-05). | `Analysis` (agrégat) |

---
### **5.2. Contraintes et Règles Métier Associées**
1. **AnalysisStatus** :
   - Un résultat ne peut être transmis à BC-AXA-05 que si son `status` est `VALIDATED`.
   - **Règle de construction** : Le statut passe à `VALIDATED` uniquement après validation biologique (`RBC-04-03`).

2. **AnalyzerId** :
   - L'identifiant de l'analyseur doit être **unique** et **traçable**.
   - **Règle de construction** : Le SIL enregistre automatiquement l'`AnalyzerId` depuis l'analyseur.

3. **AntiXaUnit** :
   - L'unité doit être **cohérente** avec le type d'analyseur.
   - **Règle de construction** : Le SIL utilise une **table de correspondance** entre analyseurs et unités.

4. **QualityControl** :
   - Le contrôle qualité doit être **réussi** (`isPassed` = `true`) pour que l'analyse soit considérée comme valide.
   - **Règle de construction** : L'analyseur génère automatiquement le résultat du contrôle qualité.

5. **ResultRange** :
   - La plage de valeurs normales doit être **définie** pour chaque type d'AOD.
   - **Règle de construction** : Le SIL utilise les **grilles d'interprétation** de BC-AXA-05.

---
### **5.3. Objets Valeur Partagés ou Ambiguës**
| **Objet Valeur** | **BCs Partagés** | **Ambiguïté** | **Solution Proposée** |
|------------------|------------------|---------------|-----------------------|
| **ResultRange** | BC-AXA-04, BC-AXA-05 | Dans BC-AXA-04 = plage de valeurs normales pour l'analyse. Dans BC-AXA-05 = seuil d'alerte pour l'interprétation. | Renommer en **NormalResultRange** dans BC-AXA-04 et **AlertThreshold** dans BC-AXA-05. |
| **AntiXaUnit** | BC-AXA-04, BC-AXA-05 | Dans BC-AXA-04 = unité du résultat brut. Dans BC-AXA-05 = unité pour l'interprétation. | Utiliser un **identifiant unique** pour chaque unité (ex: `AntiXaUnitId`) et une **table de correspondance** partagée. |

---

---

## **6. BC-AXA-05 : Interprétation Clinique**
**Type** : Cœur stratégique
**Responsabilité principale** :
Interpréter les **résultats du dosage anti-Xa** en contexte clinique et thérapeutique, et émettre des **recommandations thérapeutiques validées**.

---
### **6.1. Objets Valeur Identifiés**

| **Objet Valeur** | **Description** | **Attributs** | **Type** | **Règle d'égalité** | **Contraintes de validité** | **Règles de construction** | **Porté par** |
|------------------|-----------------|---------------|----------|---------------------|-----------------------------|-----------------------------|----------------|
| **InterpretationStatus** | Statut de l'interprétation. | `status` | Enum | Deux objets sont égaux si leur `status` est identique. | `status` ∈ {`PENDING`, `INTERPRETED`, `VALIDATED`} | Généré automatiquement par le SIL après interprétation. | `Interpretation` (agrégat) |
| **AlertThreshold** | Seuil d'alerte pour un résultat anti-Xa. | `threshold`, `aodType`, `clinicalContextType` | Double + AODType + ClinicalContextType | Deux objets sont égaux si leurs attributs sont identiques. | `threshold` > 0, `aodType` ∈ {`Apixaban`, `Rivaroxaban`, `Edoxaban`}, `clinicalContextType` ∈ {`ActiveHemorrhage`, `PreSurgery`, ...} | Déduit des **grilles d'interprétation** définies par la CAI. | `InterpretationGrid` (entité) |
| **TherapeuticRecommendation** | Recommandation thérapeutique structurée. | `recommendationType`, `dosage`, `duration`, `justification` | Enum + Double + String + String | Deux objets sont égaux si leurs attributs sont identiques. | `recommendationType` ∈ {`DOSE_ADJUSTMENT`, `SWITCH_TO_PARENTERAL`, `MONITORING_ONLY`, `NO_CHANGE`}, `dosage` ≥ 0, `duration` > 0 | Généré automatiquement par le SIL après application des grilles d'interprétation. | `Interpretation` (agrégat) |
| **RenalFunction** | Fonction rénale du patient (clairance de la créatinine). | `creatinineClearance`, `unit` | Double + String | Deux objets sont égaux si leurs attributs sont identiques. | `creatinineClearance` > 0, `unit` ∈ {`mL/min`, `mL/s`} | Récupéré automatiquement depuis le DPI (BC-AXA-08). | `ClinicalContext` (entité) |
| **LastDoseWindow** | Fenêtre temporelle depuis la dernière prise d'AOD. | `timeSinceLastDose`, `unit` | Double + String | Deux objets sont égaux si leurs attributs sont identiques. | `timeSinceLastDose` ≥ 0, `unit` ∈ {`hours`, `minutes`} | Calculé par le SIL à partir de `lastDoseTime` (BC-AXA-01). | `AODDetails` (entité) |

---
### **6.2. Contraintes et Règles Métier Associées**
1. **InterpretationStatus** :
   - Une recommandation ne peut être émise que si le `status` est `VALIDATED`.
   - **Règle de construction** : Le statut passe à `VALIDATED` uniquement après validation pharmaceutique (`RBC-05-02`).

2. **AlertThreshold** :
   - Le seuil d'alerte doit être **cohérent** avec le type d'AOD et le contexte clinique.
   - **Règle de construction** : Le SIL utilise les **grilles d'interprétation** définies par la CAI (`RBC-05-01`).

3. **TherapeuticRecommendation** :
   - La recommandation doit être **structurée** et **justifiée**.
   - **Règle de construction** : Le SIL génère automatiquement la recommandation en fonction du résultat et du contexte clinique.

4. **RenalFunction** :
   - La fonction rénale doit être **à jour** (<24h) pour une interprétation pertinente.
   - **Règle de construction** : Le SIL rafraîchit les données depuis le DPI (BC-AXA-08).

5. **LastDoseWindow** :
   - La fenêtre temporelle doit être **calculée** pour ajuster la posologie.
   - **Règle de construction** : Le SIL utilise `lastDoseTime` (BC-AXA-01) pour calculer `timeSinceLastDose`.

---
### **6.3. Objets Valeur Partagés ou Ambiguës**
| **Objet Valeur** | **BCs Partagés** | **Ambiguïté** | **Solution Proposée** |
|------------------|------------------|---------------|-----------------------|
| **AlertThreshold** | BC-AXA-05, BC-AXA-06 | Dans BC-AXA-05 = seuil d'alerte pour l'interprétation. Dans BC-AXA-06 = seuil d'alerte pour les notifications. | Utiliser un **identifiant unique** pour chaque seuil (ex: `AlertThresholdId`) et une **table de correspondance** partagée. |
| **TherapeuticRecommendation** | BC-AXA-05, BC-AXA-06 | Dans BC-AXA-05 = recommandation thérapeutique. Dans BC-AXA-06 = message structuré pour les cliniciens. | Renommer en **ClinicalRecommendation** dans BC-AXA-05 et **StructuredMessage** dans BC-AXA-06. |

---

---

## **7. BC-AXA-06 : Collaboration et Communication**
**Type** : Support
**Responsabilité principale** :
Faciliter la **communication sécurisée et structurée** entre les acteurs (cliniciens, biologistes, pharmaciens) pour une prise en charge coordonnée.

---
### **7.1. Objets Valeur Identifiés**

| **Objet Valeur** | **Description** | **Attributs** | **Type** | **Règle d'égalité** | **Contraintes de validité** | **Règles de construction** | **Porté par** |
|------------------|-----------------|---------------|----------|---------------------|-----------------------------|-----------------------------|----------------|
| **CommunicationType** | Type de communication (alerte, rejet, recommandation). | `type` | Enum | Deux objets sont égaux si leur `type` est identique. | `type` ∈ {`PRESCRIPTION_REJECTED`, `SAMPLE_NON_CONFORMITY`, `URGENCY_ALERT`, `RECOMMENDATION_VALIDATED`, `OTHER`} | Déduit du contexte (ex: `URGENCY_ALERT` pour une demande `ABSOLUTE`). | `Communication` (agrégat) |
| **MessagePriority** | Priorité du message (faible, moyenne, haute, critique). | `priority` | Enum | Deux objets sont égaux si leur `priority` est identique. | `priority` ∈ {`LOW`, `MEDIUM`, `HIGH`, `CRITICAL`} | Calculé automatiquement par le SIL en fonction du `CommunicationType` et du contexte. | `Communication` (agrégat) |
| **SecureMessage** | Message chiffré et horodaté. | `encryptedContent`, `timestamp`, `signature` | String + DateTime + String | Deux objets sont égaux si leurs attributs sont identiques. | `encryptedContent` ≠ `null`, `timestamp` ≤ `currentTime`, `signature` valide | Généré automatiquement par le SIL avant envoi. | `Communication` (agrégat) |
| **Acknowledgment** | Accusé de réception d'un message. | `acknowledgedBy`, `acknowledgmentTimestamp` | String + DateTime | Deux objets sont égaux si leurs attributs sont identiques. | `acknowledgedBy` ∈ [liste des acteurs], `acknowledgmentTimestamp` ≥ `message.timestamp` | Généré automatiquement par le destinataire après lecture. | `Communication` (agrégat) |

---
### **7.2. Contraintes et Règles Métier Associées**
1. **CommunicationType** :
   - Le type de communication doit être **cohérent** avec le contexte (ex: `URGENCY_ALERT` pour une demande `ABSOLUTE`).
   - **Règle de construction** : Le SIL déduit le type en fonction des événements (ex: `PrescriptionRejected` → `PRESCRIPTION_REJECTED`).

2. **MessagePriority** :
   - La priorité doit être **calculée** en fonction du type de communication et du contexte.
   - **Règle de construction** : Le SIL utilise une **grille de priorisation** (ex: `CRITICAL` pour `URGENCY_ALERT`).

3. **SecureMessage** :
   - Le message doit être **chiffré** et **horodaté** pour garantir la sécurité et la traçabilité.
   - **Règle de construction** : Le SIL utilise un **certificat de chiffrement** (ex: AES-256) et un **horodatage sécurisé**.

4. **Acknowledgment** :
   - L'accusé de réception doit être **obligatoire** pour les messages critiques.
   - **Règle de construction** : Le SIL attend un accusé de réception avant de marquer le message comme `RECEIVED`.

---
### **7.3. Objets Valeur Partagés ou Ambiguës**
| **Objet Valeur** | **BCs Partagés** | **Ambiguïté** | **Solution Proposée** |
|------------------|------------------|---------------|-----------------------|
| **MessagePriority** | BC-AXA-06, BC-AXA-03 | Dans BC-AXA-06 = priorité pour les notifications. Dans BC-AXA-03 = priorité pour l'ordonnancement. | Utiliser un **identifiant unique** pour chaque niveau de priorité (ex: `MessagePriorityId`) et une **table de correspondance** partagée. |

---

---

## **8. BC-AXA-07 : Gestion des Exceptions**
**Type** : Support
**Responsabilité principale** :
Gérer les **cas particuliers** (non-conformités, urgences hors heures ouvrables) et organiser les **astreintes** pour assurer la continuité du service 24/7.

---
### **8.1. Objets Valeur Identifiés**

| **Objet Valeur** | **Description** | **Attributs** | **Type** | **Règle d'égalité** | **Contraintes de validité** | **Règles de construction** | **Porté par** |
|------------------|-----------------|---------------|----------|---------------------|-----------------------------|-----------------------------|----------------|
| **OnCallStatus** | Statut du planning d'astreinte. | `status` | Enum | Deux objets sont égaux si leur `status` est identique. | `status` ∈ {`PLANNED`, `ACTIVE`, `COMPLETED`} | Généré automatiquement par le SIL en fonction des horaires. | `OnCallSchedule` (agrégat) |
| **ExceptionType** | Type d'exception à gérer en astreinte. | `type` | Enum | Deux objets sont égaux si leur `type` est identique. | `type` ∈ {`SAMPLE_NON_CONFORMITY`, `URGENT_REQUEST_OUT_OF_HOURS`, `EQUIPMENT_FAILURE`} | Déduit du contexte (ex: `URGENT_REQUEST_OUT_OF_HOURS` pour une demande `ABSOLUTE` en dehors des heures ouvrables). | `OnCallSchedule` (agrégat) |
| **EscalationLevel** | Niveau d'escalade pour une exception. | `level` | Enum | Deux objets sont égaux si leur `level` est identique. | `level` ∈ {`LEVEL_1`, `LEVEL_2`, `LEVEL_3`} | Calculé automatiquement par le SIL en fonction de la criticité de l'exception. | `OnCallSchedule` (agrégat) |
| **OnCallWindow** | Fenêtre temporelle de l'astreinte. | `startTime`, `endTime` | DateTime | Deux objets sont égaux si leurs attributs sont identiques. | `startTime` < `endTime` | Déduit des plannings d'astreinte (ex: 20h-8h en semaine). | `OnCallSchedule` (agrégat) |

---
### **8.2. Contraintes et Règles Métier Associées**
1. **OnCallStatus** :
   - Le statut doit être **mis à jour automatiquement** en fonction des horaires.
   - **Règle de construction** : Le SIL utilise un **calendrier d'astreinte** défini par l'administration.

2. **ExceptionType** :
   - Le type d'exception doit être **cohérent** avec le contexte (ex: `SAMPLE_NON_CONFORMITY` pour un échantillon non conforme en astreinte).
   - **Règle de construction** : Le SIL déduit le type en fonction des événements (ex: `SampleNonConformityDetected` → `SAMPLE_NON_CONFORMITY`).

3. **EscalationLevel** :
   - Le niveau d'escalade doit être **calculé** en fonction de la criticité de l'exception.
   - **Règle de construction** : Le SIL utilise une **grille d'escalade** définie par la CAI.

4. **OnCallWindow** :
   - La fenêtre temporelle doit être **disponible** pour l'astreinte.
   - **Règle de construction** : Le SIL consulte le calendrier d'astreinte pour déterminer la fenêtre.

---
### **8.3. Objets Valeur Partagés ou Ambiguës**
| **Objet Valeur** | **BCs Partagés** | **Ambiguïté** | **Solution Proposée** |
|------------------|------------------|---------------|-----------------------|
| **ExceptionType** | BC-AXA-07, BC-AXA-02 | Dans BC-AXA-07 = type d'exception en astreinte. Dans BC-AXA-02 = motif de non-conformité. | Utiliser un **identifiant unique** pour chaque type d'exception (ex: `ExceptionTypeId`) et une **table de correspondance** partagée. |

---

---

## **9. BC-AXA-08 : Intégration des Données**
**Type** : Générique/Technique
**Responsabilité principale** :
Assurer l'**intégration fluide** des données patients (DPI) et des résultats (analyseurs) avec le SIL pour éviter les **erreurs de saisie** et garantir la **cohérence**.

---
### **9.1. Objets Valeur Identifiés**

| **Objet Valeur** | **Description** | **Attributs** | **Type** | **Règle d'égalité** | **Contraintes de validité** | **Règles de construction** | **Porté par** |
|------------------|-----------------|---------------|----------|---------------------|-----------------------------|-----------------------------|----------------|
| **DataFormat** | Format des données échangées. | `format` | Enum | Deux objets sont égaux si leur `format` est identique. | `format` ∈ {`HL7_FHIR`, `JSON`, `XML`} | Déduit du système source (ex: DPI utilise HL7 FHIR). | `DataIntegration` (agrégat) |
| **IntegrationStatus** | Statut de l'intégration des données. | `status` | Enum | Deux objets sont égaux si leur `status` est identique. | `status` ∈ {`PENDING`, `VALIDATED`, `TRANSFORMED`, `FAILED`} | Généré automatiquement par le SIL après validation. | `DataIntegration` (agrégat) |
| **DataConsistency** | Cohérence des données intégrées. | `isConsistent`, `validationErrors` | Boolean + String[] | Deux objets sont égaux si leurs attributs sont identiques. | `isConsistent` ∈ {`true`, `false`}, `validationErrors` = [] si `isConsistent` = `true` | Calculé automatiquement par le SIL après validation des données. | `DataIntegration` (agrégat) |
| **PatientIdentifier** | Identifiant unique du patient. | `idType`, `idValue` | Enum + String | Deux objets sont égaux si leurs attributs sont identiques. | `idType` ∈ {`INS`, `NIR`, `LOCAL`}, `idValue` ≠ `null` | Récupéré depuis le DPI ou généré automatiquement par le SIL. | `DataIntegration` (agrégat) |

---
### **9.2. Contraintes et Règles Métier Associées**
1. **DataFormat** :
   - Le format doit être **compatible** avec le système cible (ex: HL7 FHIR pour le DPI).
   - **Règle de construction** : Le SIL utilise un **convertisseur de format** (ex: JSON → HL7 FHIR).

2. **IntegrationStatus** :
   - Les données ne peuvent être transmises que si leur `status` est `VALIDATED`.
   - **Règle de construction** : Le SIL valide les données avant transformation (`RBC-08-02`).

3. **DataConsistency** :
   - Les données doivent être **cohérentes** avec les règles métier (ex: `creatinineClearance` > 0).
   - **Règle de construction** : Le SIL utilise des **règles de validation** (ex: plage de valeurs pour `creatinineClearance`).

4. **PatientIdentifier** :
   - L'identifiant du patient doit être **unique** et **traçable**.
   - **Règle de construction** : Le SIL utilise un **identifiant national** (ex: NIR) ou un identifiant local.

---
### **9.3. Objets Valeur Partagés ou Ambiguës**
| **Objet Valeur** | **BCs Partagés** | **Ambiguïté** | **Solution Proposée** |
|------------------|------------------|---------------|-----------------------|
| **PatientIdentifier** | BC-AXA-08, BC-AXA-01 | Dans BC-AXA-08 = identifiant du patient pour l'intégration. Dans BC-AXA-01 = identifiant du patient pour la prescription. | Utiliser un **identifiant unique** pour chaque patient (ex: `PatientId`) et une **table de correspondance** partagée. |

---

---

## **10. BC-AXA-09 : Gestion des Ressources**
**Type** : Support
**Responsabilité principale** :
Optimiser l'**utilisation des ressources critiques** (techniciens, analyseurs) pour garantir la **réactivité** du laboratoire.

---
### **10.1. Objets Valeur Identifiés**

| **Objet Valeur** | **Description** | **Attributs** | **Type** | **Règle d'égalité** | **Contraintes de validité** | **Règles de construction** | **Porté par** |
|------------------|-----------------|---------------|----------|---------------------|-----------------------------|-----------------------------|----------------|
| **ResourceType** | Type de ressource critique. | `type` | Enum | Deux objets sont égaux si leur `type` est identique. | `type` ∈ {`TECHNICIAN`, `ANALYZER`} | Déduit du contexte (ex: `ANALYZER` pour BC-AXA-04). | `ResourceAllocation` (agrégat) |
| **AllocationStatus** | Statut de l'allocation d'une ressource. | `status` | Enum | Deux objets sont égaux si leur `status` est identique. | `status` ∈ {`PLANNED`, `ALLOCATED`, `RELEASED`} | Généré automatiquement par le SIL après allocation. | `ResourceAllocation` (agrégat) |
| **ResourceAvailability** | Disponibilité d'une ressource. | `isAvailable`, `nextAvailableTime` | Boolean + DateTime | Deux objets sont égaux si leurs attributs sont identiques. | `isAvailable` ∈ {`true`, `false`}, `nextAvailableTime` ≥ `currentTime` si `isAvailable` = `false` | Calculé automatiquement par le SIL en fonction des plannings. | `ResourceAllocation` (agrégat) |
| **PeakActivityWindow** | Fenêtre temporelle de pic d'activité. | `startTime`, `endTime`, `expectedVolume` | DateTime + DateTime + Integer | Deux objets sont égaux si leurs attributs sont identiques. | `startTime` < `endTime`, `expectedVolume` > 0 | Déduit des **statistiques historiques** (ex: épidémie). | `ResourceAllocation` (agrégat) |

---
### **10.2. Contraintes et Règles Métier Associées**
1. **ResourceType** :
   - Le type de ressource doit être **cohérent** avec la demande (ex: `ANALYZER` pour BC-AXA-04).
   - **Règle de construction** : Le SIL vérifie la disponibilité des ressources avant allocation.

2. **AllocationStatus** :
   - Une ressource ne peut être allouée que si son `status` est `PLANNED` ou `RELEASED`.
   - **Règle de construction** : Le SIL met à jour le statut après allocation (`allocate()`) ou libération (`release()`).

3. **ResourceAvailability** :
   - La disponibilité doit être **calculée** en fonction des plannings et des pics d'activité.
   - **Règle de construction** : Le SIL utilise un **algorithme de planification** (ex: algorithme de type "First-Fit Decreasing").

4. **PeakActivityWindow** :
   - La fenêtre de pic d'activité doit être **prédite** pour optimiser l'allocation des ressources.
   - **Règle de construction** : Le SIL utilise des **modèles prédictifs** (ex: machine learning basé sur les données historiques).

---
### **10.3. Objets Valeur Partagés ou Ambiguës**
| **Objet Valeur** | **BCs Partagés** | **Ambiguïté** | **Solution Proposée** |
|------------------|------------------|---------------|-----------------------|
| **ResourceType** | BC-AXA-09, BC-AXA-03 | Dans BC-AXA-09 = type de ressource pour l'allocation. Dans BC-AXA-03 = type de ressource pour l'ordonnancement. | Utiliser un **identifiant unique** pour chaque type de ressource (ex: `ResourceTypeId`) et une **table de correspondance** partagée. |

---

---

## **11. BC-AXA-10 : Traçabilité et Conformité**
**Type** : Générique/Technique
**Responsabilité principale** :
Enregistrer **systématiquement toutes les actions** du circuit et garantir la **sécurité des données**, la **traçabilité complète** et la **conformité réglementaire**.

---
### **11.1. Objets Valeur Identifiés**

| **Objet Valeur** | **Description** | **Attributs** | **Type** | **Règle d'égalité** | **Contraintes de validité** | **Règles de construction** | **Porté par** |
|------------------|-----------------|---------------|----------|---------------------|-----------------------------|-----------------------------|----------------|
| **LogStatus** | Statut d'un log d'audit. | `status` | Enum | Deux objets sont égaux si leur `status` est identique. | `status` ∈ {`PENDING`, `SIGNED`, `ARCHIVED`} | Généré automatiquement par le SIL après signature. | `AuditLog` (agrégat) |
| **RetentionPeriod** | Période de conservation d'un log. | `startDate`, `endDate`, `regulation` | DateTime + DateTime + Enum | Deux objets sont égaux si leurs attributs sont identiques. | `startDate` < `endDate`, `regulation` ∈ {`ISO_15189`, `RGPD`, `LOCAL`} | Déduit des **règlementations** (ex: 10 ans pour ISO 15189). | `AuditLog` (agrégat) |
| **DataSecurity** | Niveau de sécurité des données. | `encryptionLevel`, `accessControl` | Enum + Enum | Deux objets sont égaux si leurs attributs sont identiques. | `encryptionLevel` ∈ {`AES_128`, `AES_256`, `NONE`}, `accessControl` ∈ {`CPS`, `LOCAL`, `NONE`} | Déduit des **politiques de sécurité** de l'établissement. | `AuditLog` (