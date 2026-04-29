```markdown
# **Risques de découpage en Bounded Contexts et arbitrages à traiter**
**Domaine métier** : Gestion des demandes urgentes de dosage anti-Xa dans le SIL
**Date** : 2024-06-10
**Version** : 1.0
**Auteurs** : Analyste DDD
**Sources** : Livrables étapes 1, 2 et 4

---

---

## **1. Introduction**
Ce document identifie et analyse les **risques majeurs** liés à un **mauvais découpage en Bounded Contexts** pour le domaine des **demandes urgentes de dosage anti-Xa dans le SIL**. Il met en lumière :
- Les **risques de duplication incohérente des règles métier**.
- Les **ambiguïtés de vocabulaire** entre contextes.
- Les **dépendances trop fortes** entre Bounded Contexts.
- Les **responsabilités floues** ou mal réparties.
- Les **contrats d'échange insuffisants** ou mal définis.

Pour chaque risque identifié, nous proposons :
- Les **contextes concernés**.
- Les **impacts métier possibles** (clinique, réglementaire, opérationnel).
- Les **arbitrages à décider** avec les experts métier.
- Les **questions clés** à poser aux parties prenantes.
- Des **recommandations de prudence** avant toute décision d'architecture.

L'objectif est d'éviter les **couplages indésirables**, les **incohérences sémantiques**, et les **dysfonctionnements critiques** dans le futur système.

---

---

## **2. Risques identifiés et arbitrages à traiter**

---

### **Risque 1 : Duplication incohérente des règles métier entre Bounded Contexts**
**Contexte concerné** :
- **BC-AXA-01 (Prescription Clinique)** et **BC-AXA-03 (Ordonnancement et Priorisation)**.
- **BC-AXA-02 (Gestion Pré-Analytique)** et **BC-AXA-07 (Gestion des Exceptions)**.

**Description du risque** :
Les règles métier critiques (ex. : validation des prescriptions, gestion des non-conformités) pourraient être **dupliquées ou interprétées différemment** entre les Bounded Contexts, entraînant :
- Des **incohérences** dans la validation des demandes.
- Des **décisions contradictoires** (ex. : une prescription validée dans BC-AXA-01 rejetée dans BC-AXA-03).
- Une **perte de traçabilité** et de responsabilité claire.

**Exemples concrets** :
- **Règle RBC-01-02** : "Respect des protocoles locaux (CAI)" pourrait être appliquée différemment :
  - Dans **BC-AXA-01** : Validation par le biologiste.
  - Dans **BC-AXA-03** : Priorisation automatique basée sur des critères cliniques, sans vérification des protocoles.
- **Règle RBC-02-05** : "Validation partagée des tubes" pourrait être interprétée comme :
  - Dans **BC-AXA-02** : Le technicien valide la conformité.
  - Dans **BC-AXA-07** : Le biologiste d'astreinte tranche en cas de non-conformité en dehors des heures ouvrables.

**Impacts métier possibles** :
| **Impact** | **Description** | **Gravité** |
|------------|-----------------|-------------|
| **Clinique** | Prescription inappropriée → risque de surdosage ou de sous-dosage. | ⭐⭐⭐⭐⭐ |
| **Réglementaire** | Non-respect des protocoles CAI → perte d'accréditation ISO 15189. | ⭐⭐⭐⭐⭐ |
| **Opérationnel** | Retards dans le traitement des demandes urgentes. | ⭐⭐⭐⭐ |
| **Financier** | Coûts liés aux complications évitables (ex. : transfusion, hospitalisation prolongée). | ⭐⭐⭐ |

**Arbitrages à décider** :
1. **Centraliser la validation des règles métier critiques** (ex. : respect des protocoles CAI) dans un seul Bounded Context.
   - **Option 1** : BC-AXA-01 (Prescription Clinique) devient le **gardien unique** des règles de validation clinique.
   - **Option 2** : Créer un **nouveau Bounded Context "Règles Métier"** pour centraliser toutes les règles critiques.
   - **Option 3** : **BC-AXA-10 (Traçabilité et Conformité)** intègre un module de validation des règles.

2. **Définir une autorité unique** pour les décisions critiques (ex. : rejet d'une prescription) :
   - **Autorité finale** : Le biologiste en chef ou un comité dédié (CAI + DSI).

**Questions clés à poser aux experts métier** :
- Qui doit avoir l'**autorité finale** pour valider ou rejeter une prescription ?
- Les **protocoles CAI** doivent-ils être **strictement appliqués** ou **flexibles** en cas d'urgence ?
- Comment **documenter les exceptions** aux protocoles pour éviter les incohérences ?

**Recommandations de prudence** :
- **Éviter la duplication** des règles métier : une règle critique (ex. : validation des prescriptions) doit être définie **une seule fois** et partagée via des contrats clairs.
- **Documenter les exceptions** : Prévoir un mécanisme pour gérer les cas particuliers (ex. : pédiatrie, insuffisance rénale aiguë) sans contourner les règles de base.
- **Valider les règles avec la CAI** : Toute règle métier doit être **validée et signée** par la Commission des Anti-infectieux et des Anticoagulants.

---

---

### **Risque 2 : Ambiguïtés de vocabulaire entre Bounded Contexts**
**Contexte concerné** :
- **BC-AXA-01 (Prescription Clinique)** vs. **BC-AXA-03 (Ordonnancement et Priorisation)**.
- **BC-AXA-02 (Gestion Pré-Analytique)** vs. **BC-AXA-07 (Gestion des Exceptions)**.
- **BC-AXA-04 (Analyse Laboratoire)** vs. **BC-AXA-05 (Interprétation Clinique)**.

**Description du risque** :
Les termes clés (ex. : "Prescription", "Non-conformité", "Résultat", "Urgence") ont des **sens différents** selon le contexte, ce qui peut entraîner :
- Des **malentendus** entre acteurs (ex. : un clinicien parle de "prescription urgente", un biologiste de "demande prioritaire").
- Des **erreurs de conception** dans les contrats d'échange (ex. : envoi d'une "prescription" non validée à BC-AXA-03).
- Une **perte de cohérence sémantique** dans le système.

**Exemples concrets** :
| **Terme ambigu** | **Sens dans BC-AXA-01** | **Sens dans BC-AXA-03** | **Risque** |
|------------------|-------------------------|--------------------------|------------|
| **Prescription** | Acte médical formalisé (avec données contextuelles). | Demande classée par urgence (ex. : "urgence absolue"). | Envoi d'une prescription non validée à BC-AXA-03 → erreur de priorisation. |
| **Non-conformité** | Rejet d'un échantillon (ex. : tube incorrect). | Alerte sur un résultat aberrant (ex. : dosage > seuil). | Confusion entre rejet d'échantillon et alerte sur résultat. |
| **Résultat** | Donnée brute de l'analyseur (ex. : "1.2 UI/mL"). | Interprétation clinique (ex. : "surdosage confirmé"). | Transmission d'un résultat brut à BC-AXA-05 → erreur d'interprétation. |
| **Urgence** | Contexte clinique (ex. : "hémorragie active"). | Niveau de priorité attribué (ex. : "urgence absolue"). | Utilisation du terme "urgence" dans BC-AXA-01 au lieu de "niveau de priorité". |

**Impacts métier possibles** :
| **Impact** | **Description** | **Gravité** |
|------------|-----------------|-------------|
| **Clinique** | Erreur d'interprétation → adaptation thérapeutique inadaptée. | ⭐⭐⭐⭐⭐ |
| **Réglementaire** | Non-respect des normes de traçabilité (ISO 15189). | ⭐⭐⭐⭐ |
| **Opérationnel** | Retards dans le traitement des demandes. | ⭐⭐⭐⭐ |
| **Financier** | Coûts liés aux erreurs de traitement. | ⭐⭐⭐ |

**Arbitrages à décider** :
1. **Créer un glossaire métier partagé** pour clarifier les termes ambigus :
   - Exemple :
     - **"Prescription"** → Toujours utiliser **"Demande validée"** dans les échanges entre BC-AXA-01 et BC-AXA-03.
     - **"Non-conformité"** → Dans BC-AXA-02 = "Échantillon non conforme". Dans BC-AXA-07 = "Résultat aberrant".
     - **"Résultat"** → Dans BC-AXA-04 = "Résultat brut". Dans BC-AXA-05 = "Résultat interprété".

2. **Définir des contrats d'échange explicites** avec des **noms de champs unifiés** :
   - Exemple :
     ```json
     {
       "context": "BC-AXA-01",
       "dataType": "PrescriptionValidated",
       "fields": {
         "prescriptionId": "string",
         "patientId": "string",
         "clinicalContext": "string",  // Remplacer "urgence" par "clinicalContext"
         "urgencyLevel": "string"      // Ajouté pour BC-AXA-03
       }
     }
     ```

3. **Éviter les termes génériques** comme "Urgence" ou "Résultat" dans les échanges inter-contextes. Préférer des termes précis :
   - **"Niveau de priorité"** au lieu de "Urgence".
   - **"Résultat brut"** ou **"Résultat interprété"** au lieu de "Résultat".

**Questions clés à poser aux experts métier** :
- Quels sont les **termes critiques** à clarifier pour éviter les malentendus ?
- Comment **nommer les champs** dans les contrats d'échange pour éviter les ambiguïtés ?
- Quels **exemples concrets** de malentendus ont déjà été observés dans le circuit actuel ?

**Recommandations de prudence** :
- **Documenter un glossaire métier** pour chaque Bounded Context et partager les termes ambigus avec toutes les équipes.
- **Valider les contrats d'échange** avec un atelier de simulation (ex. : jeu de rôle entre cliniciens, biologistes et techniciens).
- **Utiliser des noms de champs explicites** dans les APIs (ex. : `clinicalContext` au lieu de `urgency`).

---

---

### **Risque 3 : Dépendances trop fortes entre Bounded Contexts**
**Contexte concerné** :
- **BC-AXA-01 (Prescription Clinique)** → **BC-AXA-03 (Ordonnancement et Priorisation)**.
- **BC-AXA-02 (Gestion Pré-Analytique)** → **BC-AXA-04 (Analyse Laboratoire)**.
- **BC-AXA-04 (Analyse Laboratoire)** → **BC-AXA-05 (Interprétation Clinique)**.

**Description du risque** :
Des **dépendances directes et synchrones** entre Bounded Contexts peuvent entraîner :
- Un **couplage fort** entre les systèmes (ex. : BC-AXA-01 attend une réponse de BC-AXA-03 avant de continuer).
- Une **baisse de résilience** (ex. : si BC-AXA-03 est indisponible, BC-AXA-01 est bloqué).
- Une **difficulté à faire évoluer** les contextes indépendamment (ex. : changement des règles de priorisation dans BC-AXA-03 impacte BC-AXA-01).

**Exemples concrets** :
- **Couplage BC-AXA-01 → BC-AXA-03** :
  - BC-AXA-01 envoie une prescription à BC-AXA-03 et **attend une confirmation** avant de notifier le clinicien.
  - Si BC-AXA-03 est indisponible → blocage de BC-AXA-01.
- **Couplage BC-AXA-02 → BC-AXA-04** :
  - BC-AXA-02 envoie un échantillon conforme à BC-AXA-04 et **attend un accusé de réception** avant de mettre à jour le statut.
  - Si BC-AXA-04 est en maintenance → BC-AXA-02 ne peut pas traiter d'autres échantillons.

**Impacts métier possibles** :
| **Impact** | **Description** | **Gravité** |
|------------|-----------------|-------------|
| **Clinique** | Retard dans le traitement des demandes urgentes. | ⭐⭐⭐⭐⭐ |
| **Opérationnel** | Surcharge du système ou blocage des flux. | ⭐⭐⭐⭐ |
| **Technique** | Difficulté à faire évoluer les Bounded Contexts indépendamment. | ⭐⭐⭐⭐ |
| **Financier** | Coûts liés à la maintenance et aux évolutions. | ⭐⭐⭐ |

**Arbitrages à décider** :
1. **Remplacer les appels synchrones par des échanges asynchrones** (événements) :
   - Exemple :
     - BC-AXA-01 envoie un événement `PrescriptionValidated` à un bus d'événements (Kafka/RabbitMQ).
     - BC-AXA-03 s'abonne à cet événement et **traite la priorisation en arrière-plan**.
     - BC-AXA-01 n'attend pas de réponse de BC-AXA-03.

2. **Définir des contrats d'échange idempotents** :
   - Exemple :
     - BC-AXA-01 envoie une prescription à BC-AXA-03 **sans attendre de confirmation**.
     - BC-AXA-03 traite la demande **dans l'ordre de réception** et envoie un événement `PrioritizationCompleted` pour notifier BC-AXA-01.

3. **Introduire un middleware ou un orchestrateur** pour gérer les dépendances :
   - Exemple :
     - Un **service d'orchestration** (ex. : Apache Camel) gère les flux entre BC-AXA-01, BC-AXA-02 et BC-AXA-03.
     - Si un contexte est indisponible, le service **met en file d'attente** les demandes et les traite dès que possible.

**Questions clés à poser aux experts métier** :
- Quels sont les **flux critiques** qui ne doivent **jamais être bloqués** ?
- Comment **gérer les indisponibilités** des Bounded Contexts (ex. : maintenance, panne) ?
- Quels **mécanismes de reprise** sont nécessaires en cas d'échec (ex. : retry, compensation) ?

**Recommandations de prudence** :
- **Éviter les appels synchrones** entre Bounded Contexts : privilégier les **événements asynchrones** (ex. : Kafka, RabbitMQ).
- **Définir des contrats idempotents** pour éviter les doublons ou les pertes de données.
- **Documenter les dépendances** dans un **diagramme de contexte** (ex. : C4 Model) pour visualiser les couplages.
- **Tester la résilience** des Bounded Contexts avec des **scénarios de panne** (ex. : simulation d'indisponibilité de BC-AXA-03).

---

---

### **Risque 4 : Responsabilités floues ou mal réparties**
**Contexte concerné** :
- **BC-AXA-01 (Prescription Clinique)** et **BC-AXA-02 (Gestion Pré-Analytique)**.
- **BC-AXA-05 (Interprétation Clinique)** et **BC-AXA-06 (Collaboration et Communication)**.
- **BC-AXA-07 (Gestion des Exceptions)** et **BC-AXA-02 (Gestion Pré-Analytique)**.

**Description du risque** :
Les **responsabilités critiques** (ex. : validation des prescriptions, gestion des non-conformités, émission des recommandations) sont **partagées ou mal définies**, ce qui peut entraîner :
- Des **conflits d'autorité** (ex. : qui valide une prescription rejetée ?).
- Une **perte de traçabilité** (ex. : qui est responsable d'un échantillon non conforme ?).
- Une **surcharge de travail** pour certains acteurs (ex. : les biologistes valident tout, y compris les tâches des techniciens).

**Exemples concrets** :
| **Responsabilité floue** | **Contexte concerné** | **Risque** |
|--------------------------|-----------------------|------------|
| **Validation des prescriptions** | BC-AXA-01 (biologiste) vs. BC-AXA-03 (SIL automatique). | Double validation → retard ou conflit. |
| **Gestion des non-conformités** | BC-AXA-02 (technicien) vs. BC-AXA-07 (biologiste d'astreinte). | Rejet injustifié ou analyse d'un échantillon non conforme. |
| **Émission des recommandations** | BC-AXA-05 (biologiste) vs. BC-AXA-06 (pharmacien). | Recommandation non validée → erreur thérapeutique. |
| **Activation de l'astreinte** | BC-AXA-07 (personnel administratif) vs. BC-AXA-03 (SIL). | Astreinte non activée → retard critique. |

**Impacts métier possibles** :
| **Impact** | **Description** | **Gravité** |
|------------|-----------------|-------------|
| **Clinique** | Erreur de traitement → complication grave. | ⭐⭐⭐⭐⭐ |
| **Réglementaire** | Non-respect des normes de traçabilité. | ⭐⭐⭐⭐ |
| **Opérationnel** | Surcharge des équipes ou retards. | ⭐⭐⭐⭐ |
| **Financier** | Coûts liés aux erreurs ou aux audits. | ⭐⭐⭐ |

**Arbitrages à décider** :
1. **Définir une autorité unique** pour chaque responsabilité critique :
   - Exemple :
     - **Validation des prescriptions** → **Uniquement le biologiste** (BC-AXA-01).
     - **Gestion des non-conformités** → **Le technicien valide la conformité**, mais le **biologiste tranche en cas de désaccord** (BC-AXA-02).
     - **Émission des recommandations** → **Le biologiste propose**, mais le **pharmacien valide** (BC-AXA-05).
     - **Activation de l'astreinte** → **Automatique via le SIL** (BC-AXA-07).

2. **Documenter les responsabilités** dans un **RACI (Responsible, Accountable, Consulted, Informed)** :
   - Exemple pour la validation des prescriptions :
     | **Activité**               | **Responsible** | **Accountable** | **Consulted** | **Informed** |
     |----------------------------|-----------------|-----------------|---------------|--------------|
     | Valider une prescription   | Biologiste      | Biologiste en chef | Clinicien     | SIL, CAI     |

3. **Automatiser les décisions simples** pour réduire la charge des acteurs :
   - Exemple :
     - Le **SIL valide automatiquement** les prescriptions conformes aux protocoles (sans intervention humaine).
     - Le **SIL active l'astreinte** en cas de demande urgente en dehors des heures ouvrables.

**Questions clés à poser aux experts métier** :
- Qui doit avoir l'**autorité finale** pour valider une prescription ?
- Comment **documenter les décisions** pour les audits (ex. : logs, signatures électroniques) ?
- Quelles **décisions peuvent être automatisées** pour réduire la charge des équipes ?

**Recommandations de prudence** :
- **Éviter les responsabilités partagées** pour les décisions critiques : désigner un **unique "Accountable"** pour chaque responsabilité.
- **Automatiser les décisions simples** (ex. : validation des prescriptions conformes) pour réduire les erreurs humaines.
- **Former les équipes** aux nouvelles responsabilités pour éviter les malentendus.
- **Tester les processus** avec des **scénarios de crise** (ex. : panne du SIL, absence du biologiste).

---

---
### **Risque 5 : Contrats d'échange insuffisants ou mal définis**
**Contexte concerné** :
- **Tous les Bounded Contexts** (échanges entre BC-AXA-01 → BC-AXA-02, BC-AXA-02 → BC-AXA-04, etc.).

**Description du risque** :
Les **contrats d'échange** (données/événements) entre Bounded Contexts sont :
- **Incomplets** (ex. : données manquantes dans les échanges).
- **Ambiguës** (ex. : format des données non standardisé).
- **Non validés** (ex. : pas de test des contrats avec les utilisateurs).
- **Non sécurisés** (ex. : pas de chiffrement ou d'authentification).

Cela peut entraîner :
- Des **erreurs de données** (ex. : résultat aberrant non détecté).
- Des **pertes de données** (ex. : échantillon non conforme non signalé).
- Des **incohérences** entre systèmes (ex. : prescription validée dans BC-AXA-01 mais non reçue dans BC-AXA-03).

**Exemples concrets** :
| **Contrat d'échange** | **Problème identifié** | **Risque** |
|-----------------------|------------------------|------------|
| BC-AXA-01 → BC-AXA-02 | Données contextuelles manquantes (ex. : heure de la dernière prise). | Interprétation erronée du résultat. |
| BC-AXA-02 → BC-AXA-04 | Statut de l'échantillon non transmis (ex. : "conforme" vs. "non conforme"). | Analyse d'un échantillon non conforme → résultat invalide. |
| BC-AXA-04 → BC-AXA-05 | Résultat brut non standardisé (ex. : format différent selon l'analyseur). | Erreur d'interprétation par le biologiste. |
| BC-AXA-05 → BC-AXA-06 | Recommandation thérapeutique non structurée (ex. : texte libre au lieu de champs standardisés). | Recommandation mal comprise par le clinicien. |

**Impacts métier possibles** :
| **Impact** | **Description** | **Gravité** |
|------------|-----------------|-------------|
| **Clinique** | Erreur d'interprétation → adaptation thérapeutique inadaptée. | ⭐⭐⭐⭐⭐ |
| **Réglementaire** | Non-respect des normes de traçabilité (ISO 15189). | ⭐⭐⭐⭐⭐ |
| **Opérationnel** | Retards ou erreurs dans le traitement des demandes. | ⭐⭐⭐⭐ |
| **Financier** | Coûts liés aux erreurs ou aux audits. | ⭐