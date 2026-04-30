# **Services et Événements de Domaine**
**Domaine métier** : Gestion des demandes urgentes de dosage anti-Xa dans le SIL
**Date** : 2024-06-15
**Version** : 1.0
**Auteurs** : Architecte DDD
**Sources** : Livrables étape 5 (`01_contextes_candidats.md`, `02_frontieres_responsabilites_contextes.md`, `03_vocabulaire_modeles_par_contexte.md`, `04_dependances_contrats_contextes.md`, `05_risques_arbitrages_contextes.md`, `06_cartographie_bounded_contexts.md`, `07_synthese_bounded_contexts.md`)

---

---

## **1. Introduction**
Ce document formalise les **services de domaine** et les **événements de domaine** pour chaque **Bounded Context (BC)** du système de gestion des demandes urgentes de dosage anti-Xa. Les services de domaine encapsulent des **opérations métier significatives** qui ne peuvent être naturellement attribuées ni à une entité ni à un agrégat. Les événements de domaine représentent des **faits métier passés**, immuables et significatifs, qui indiquent qu'un changement d'état important s'est produit dans le domaine.

**Objectifs** :
- Identifier les **services de domaine** et leurs **responsabilités métier**.
- Définir les **entrées/sorties** et les **règles métier** portées par chaque service.
- Lister les **événements de domaine** avec leur **nom au passé**, leur **contenu**, et leurs **consommateurs**.
- Clarifier les **liens entre services et événements** (qui publie/consomme).
- Mettre en évidence les **événements dont la définition reste à stabiliser** avec les experts métier.

**Méthodologie** :
- Pour chaque BC, analyser les **règles métier critiques** et les **décisions clés** pour identifier les services de domaine.
- Définir les **opérations** portées par chaque service, leurs **paramètres d'entrée**, et leurs **résultats**.
- Identifier les **événements de domaine** générés par ces services, en utilisant un **nom au passé** (ex: `PrescriptionValidated`).
- Documenter les **données portées par chaque événement** et les **contextes consommateurs**.
- Distinguer les **faits stabilisés** des **hypothèses à valider** avec les experts.

---

---

## **2. BC-AXA-01 : Prescription Clinique**
**Type** : Cœur stratégique
**Responsabilité principale** :
Gérer la **prescription électronique** des dosages anti-Xa en urgence et valider leur **pertinence clinique** selon les protocoles locaux (CAI) et les recommandations HAS/ANSM.

---

### **2.1. Services de Domaine**

| **Service de Domaine** | **Responsabilité Métier** | **Entrées** | **Sorties** | **Règles Métier Portées** | **Exemple d'Appel** |
|------------------------|----------------------------|-------------|-------------|----------------------------|----------------------|
| **`PrescriptionValidationService`** | Valider une prescription selon les protocoles CAI et les données cliniques. | - `prescriptionId` (UUID) <br> - `clinicalContext` (ClinicalContextType) <br> - `aodDetails` (AODDetails) <br> - `prescriptionProtocol` (PrescriptionProtocol) | - `validationStatus` (PrescriptionStatus) <br> - `validationTimestamp` (DateTime) <br> - `validationReason` (String, si rejet) | - Vérifier l'exhaustivité des données (`RBC-01-04`) <br> - Valider la conformité aux protocoles CAI (`RBC-01-02`) <br> - Bloquer les prescriptions non conformes (`RBC-01-01`) | ```java
validatePrescription(
    prescriptionId: UUID,
    clinicalContext: ClinicalContext,
    aodDetails: AODDetails,
    prescriptionProtocol: PrescriptionProtocol
) -> ValidationResult
``` |
| **`PrescriptionCompletionService`** | Compléter une prescription incomplète avec des données manquantes. | - `prescriptionId` (UUID) <br> - `missingDataType` (String: "lastDoseTime", "creatinineClearance", etc.) | - `updatedPrescription` (Prescription) <br> - `completionTimestamp` (DateTime) | - Notifier le clinicien des données manquantes (`RBC-01-04`) <br> - Mettre à jour le statut de la prescription | ```java
completePrescription(
    prescriptionId: UUID,
    missingDataType: String
) -> Prescription
``` |
| **`PrescriptionRejectionService`** | Rejeter une prescription non conforme et notifier les acteurs concernés. | - `prescriptionId` (UUID) <br> - `rejectionReason` (NonConformityReason) <br> - `clinicianId` (String) | - `rejectionStatus` (PrescriptionStatus) <br> - `notificationSent` (Boolean) | - Générer un motif de rejet justifié (`RBC-01-03`) <br> - Envoyer une notification au clinicien (`RBC-01-06`) | ```java
rejectPrescription(
    prescriptionId: UUID,
    rejectionReason: String,
    clinicianId: String
) -> RejectionResult
``` |

---

### **2.2. Événements de Domaine**

| **Événement** | **Données Portées** | **Publié par** | **Consommateurs** | **Description** |
|---------------|---------------------|-----------------|-------------------|-----------------|
| `PrescriptionCreated` | `{ "prescriptionId": UUID, "patientId": String, "aodType": AODType, "clinicalContext": ClinicalContextType }` | `Prescription` (agrégat) | - `PrescriptionValidationService` (BC-AXA-01) <br> - `DataIntegration` (BC-AXA-08) | Une nouvelle prescription a été créée dans le SIL. |
| `PrescriptionValidated` | `{ "prescriptionId": UUID, "validatedBy": String (BiologisteId), "validationTimestamp": DateTime, "urgencyLevel": UrgencyLevel }` | `PrescriptionValidationService` | - `Sample` (BC-AXA-02) <br> - `Request` (BC-AXA-03) <br> - `AuditLog` (BC-AXA-10) | Une prescription a été validée biologiquement et est prête pour la priorisation. |
| `PrescriptionRejected` | `{ "prescriptionId": UUID, "rejectionReason": String, "rejectedBy": String (BiologisteId), "rejectionTimestamp": DateTime }` | `PrescriptionRejectionService` | - `Communication` (BC-AXA-06) <br> - `AuditLog` (BC-AXA-10) | Une prescription a été rejetée pour non-conformité ou données manquantes. |
| `PrescriptionCompleted` | `{ "prescriptionId": UUID, "completedFields": String[], "completionTimestamp": DateTime }` | `PrescriptionCompletionService` | - `PrescriptionValidationService` (BC-AXA-01) <br> - `AuditLog` (BC-AXA-10) | Une prescription incomplète a été complétée par le clinicien. |

---
### **2.3. Points à Clarifier avec les Experts Métier**
| **Événement** | **Question** | **Impact Potentiel** |
|---------------|--------------|----------------------|
| `PrescriptionValidated` | Quel niveau de détail doit être inclus dans l'événement pour BC-AXA-03 (Ordonnancement) ? | Mauvaise priorisation des demandes. |
| `PrescriptionRejected` | Faut-il inclure le motif de rejet dans l'événement ou le gérer via un service dédié ? | Perte de traçabilité ou retard dans la correction. |

---

---

## **3. BC-AXA-02 : Gestion Pré-Analytique**
**Type** : Support
**Responsabilité principale** :
Vérifier la **conformité des échantillons biologiques** (tubes) avant analyse et gérer les **non-conformités** selon les exigences réglementaires (ISO 15189, RGPD).

---

### **3.1. Services de Domaine**

| **Service de Domaine** | **Responsabilité Métier** | **Entrées** | **Sorties** | **Règles Métier Portées** | **Exemple d'Appel** |
|------------------------|----------------------------|-------------|-------------|----------------------------|----------------------|
| **`SampleConformityVerificationService`** | Vérifier la conformité d'un échantillon selon les critères pré-analytiques. | - `sampleId` (UUID) <br> - `tubeType` (TubeType) <br> - `volume` (Double) <br> - `transportConditions` (TransportConditions) | - `conformityStatus` (SampleStatus) <br> - `nonConformityReasons` (NonConformityReason[]) | - Vérifier le type de tube (`RBC-02-01`) <br> - Vérifier le volume minimal (`RBC-02-02`) <br> - Vérifier le délai de transport (`RBC-02-03`) <br> - Vérifier les conditions de transport (`RBC-02-04`) | ```java
verifySampleConformity(
    sampleId: UUID,
    tubeType: TubeType,
    volume: Double,
    transportConditions: TransportConditions
) -> ConformityResult
``` |
| **`NonConformityManagementService`** | Gérer les non-conformités détectées et notifier les acteurs concernés. | - `sampleId` (UUID) <br> - `nonConformityReason` (NonConformityReason) <br> - `technicianId` (String) | - `nonConformityStatus` (SampleStatus) <br> - `notificationSent` (Boolean) <br> - `newSampleRequested` (Boolean) | - Générer un motif de non-conformité justifié (`RBC-02-05`) <br> - Notifier le clinicien (`RBC-02-06`) <br> - Demander un nouveau prélèvement si nécessaire | ```java
manageNonConformity(
    sampleId: UUID,
    nonConformityReason: NonConformityReason,
    technicianId: String
) -> NonConformityResult
``` |

---
### **3.2. Événements de Domaine**

| **Événement** | **Données Portées** | **Publié par** | **Consommateurs** | **Description** |
|---------------|---------------------|-----------------|-------------------|-----------------|
| `SampleReceived` | `{ "sampleId": UUID, "prescriptionId": UUID, "patientId": String }` | `Sample` (agrégat) | - `SampleConformityVerificationService` (BC-AXA-02) <br> - `DataIntegration` (BC-AXA-08) | Un échantillon a été reçu au laboratoire. |
| `SampleConformityVerified` | `{ "sampleId": UUID, "status": SampleStatus, "verificationTimestamp": DateTime }` | `SampleConformityVerificationService` | - `Analysis` (BC-AXA-04) <br> - `OnCallSchedule` (BC-AXA-07) <br> - `AuditLog` (BC-AXA-10) | Un échantillon a été vérifié conforme et est prêt pour l'analyse. |
| `SampleNonConformityDetected` | `{ "sampleId": UUID, "reasons": NonConformityReason[], "detectedBy": String (TechnicianId), "detectionTimestamp": DateTime }` | `NonConformityManagementService` | - `Communication` (BC-AXA-06) <br> - `OnCallSchedule` (BC-AXA-07) <br> - `AuditLog` (BC-AXA-10) | Une non-conformité a été détectée sur un échantillon. |

---
### **3.3. Points à Clarifier avec les Experts Métier**
| **Événement** | **Question** | **Impact Potentiel** |
|---------------|--------------|----------------------|
| `SampleConformityVerified` | Faut-il inclure les détails de la conformité (ex: volume exact, température) dans l'événement ? | Perte d'information pour l'analyse ou l'interprétation. |
| `SampleNonConformityDetected` | Faut-il inclure une recommandation automatique pour le nouveau prélèvement (ex: type de tube à utiliser) ? | Erreur dans le nouveau prélèvement ou retard. |

---

---

## **4. BC-AXA-03 : Ordonnancement et Priorisation**
**Type** : Cœur stratégique
**Responsabilité principale** :
Classer les **demandes de dosage anti-Xa** par **niveau d'urgence clinique** et ordonnancer les analyses en fonction des **ressources disponibles** (techniciens, analyseurs) et des **délais critiques**.

---

### **4.1. Services de Domaine**

| **Service de Domaine** | **Responsabilité Métier** | **Entrées** | **Sorties** | **Règles Métier Portées** | **Exemple d'Appel** |
|------------------------|----------------------------|-------------|-------------|----------------------------|----------------------|
| **`PrioritizationService`** | Classer une demande par niveau d'urgence clinique. | - `requestId` (UUID) <br> - `prescription` (Prescription) <br> - `resourcesAvailability` (ResourceAvailability[]) | - `urgencyLevel` (UrgencyLevel) <br> - `maxDeadline` (DateTime) <br> - `priorityScore` (Integer) | - Appliquer la grille de priorisation CAI (`RBC-03-01`) <br> - Calculer le délai maximal (`RBC-03-02`) <br> - Détecter les conflits de priorité | ```java
prioritizeRequest(
    requestId: UUID,
    prescription: Prescription,
    resourcesAvailability: ResourceAvailability[]
) -> PrioritizationResult
``` |
| **`SchedulingService`** | Ordonnancer une demande priorisée en fonction des ressources disponibles. | - `requestId` (UUID) <br> - `urgencyLevel` (UrgencyLevel) <br> - `resourcesAvailability` (ResourceAvailability[]) | - `scheduledStartTime` (DateTime) <br> - `scheduledEndTime` (DateTime) <br> - `allocatedResources` (ResourceAllocation[]) | - Allouer les ressources disponibles (`RBC-03-03`) <br> - Gérer les pics d'activité (`RBC-09-01`) | ```java
scheduleRequest(
    requestId: UUID,
    urgencyLevel: UrgencyLevel,
    resourcesAvailability: ResourceAvailability[]
) -> SchedulingResult
``` |
| **`UrgencyAlertService`** | Déclencher des alertes en cas de dépassement de délai critique. | - `requestId` (UUID) <br> - `maxDeadline` (DateTime) <br> - `currentTime` (DateTime) | - `alertTriggered` (Boolean) <br> - `alertRecipients` (String[]) | - Détecter les dépassements de délai (`RBC-03-02`) <br> - Notifier les acteurs concernés (`RBC-03-06`) | ```java
triggerUrgencyAlert(
    requestId: UUID,
    maxDeadline: DateTime,
    currentTime: DateTime
) -> AlertResult
``` |

---
### **4.2. Événements de Domaine**

| **Événement** | **Données Portées** | **Publié par** | **Consommateurs** | **Description** |
|---------------|---------------------|-----------------|-------------------|-----------------|
| `RequestReceived` | `{ "requestId": UUID, "prescriptionId": UUID, "urgencyLevel": UrgencyLevel }` | `Request` (agrégat) | - `PrioritizationService` (BC-AXA-03) <br> - `AuditLog` (BC-AXA-10) | Une nouvelle demande priorisée a été reçue. |
| `RequestPrioritized` | `{ "requestId": UUID, "urgencyLevel": UrgencyLevel, "maxDeadline": DateTime, "priorityScore": Integer }` | `PrioritizationService` | - `SchedulingService` (BC-AXA-03) <br> - `UrgencyAlertService` (BC-AXA-03) <br> - `AuditLog` (BC-AXA-10) | Une demande a été classée par niveau d'urgence. |
| `RequestScheduled` | `{ "requestId": UUID, "scheduledStartTime": DateTime, "scheduledEndTime": DateTime, "allocatedResources": ResourceAllocation[] }` | `SchedulingService` | - `Analysis` (BC-AXA-04) <br> - `AuditLog` (BC-AXA-10) | Une demande a été ordonnancée et est prête pour l'analyse. |
| `UrgencyAlertTriggered` | `{ "requestId": UUID, "alertLevel": UrgencyLevel, "triggeredAt": DateTime }` | `UrgencyAlertService` | - `Communication` (BC-AXA-06) <br> - `OnCallSchedule` (BC