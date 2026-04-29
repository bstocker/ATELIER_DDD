```markdown
# Proposition de sous-domaines métier
**Gestion des demandes urgentes de dosage anti-Xa dans le SIL**
**Date** : [À compléter]
**Version** : 1.0
**Auteurs** : Analyste DDD
**Sources** : Livrables étape 1 et 2 (01_reformulation_du_besoin.md, 02_acteurs_du_domaine.md, 03_concepts_metier_initiaux.md, 04_contraintes_et_risques.md, 05_vision_globale_du_domaine.md, 01_cartographie_acteurs_responsabilites.md, 02_attentes_objectifs_acteurs.md, 03_decisions_informations_manipulees.md, 04_regles_metier.md, 05_priorites_exceptions_contraintes.md, 06_conflits_objectifs_arbitrages.md, 07_base_modelisation_comportementale.md)

---

## 1. Introduction
Ce document propose une **réorganisation du domaine des demandes urgentes de dosage anti-Xa** en **sous-domaines métier cohérents**, en s’appuyant sur les livrables des étapes 1 et 2. L’objectif est de :
- **Réduire la complexité** du domaine global en identifiant des périmètres homogènes de responsabilités métier.
- **Définir clairement** la finalité, les acteurs, les décisions, les informations et les règles de chaque sous-domaine.
- **Distinguer** les sous-domaines de cœur stratégique, de support et génériques pour préparer l’étape suivante de modélisation comportementale (étape 3).
- **Identifier les frontières potentielles** entre sous-domaines sans figer prématurément les bounded contexts.

Ce découpage repose sur une analyse approfondie des **problèmes métier**, des **règles implicites**, des **décisions clés** et des **contraintes réglementaires**, tout en signalant les **hypothèses à valider** avec les experts.

---

## 2. Liste des sous-domaines proposés

### 2.1. Sous-domaine 1 : Gestion des prescriptions et priorisation
**Finalité métier** :
Garantir que **toute demande de dosage anti-Xa** est **prescrite de manière conforme aux protocoles**, **validée cliniquement** et **priorisée automatiquement** avant toute analyse, afin d’éviter les prescriptions inappropriées, les erreurs de tri et les retards critiques.

**Responsabilité métier principale** :
- **Centraliser et valider** les prescriptions électroniques.
- **Appliquer une grille de priorisation automatique** basée sur des critères cliniques objectifs.
- **Rejeter les demandes non conformes** aux protocoles locaux ou aux recommandations HAS/ANSM.
- **Assurer la traçabilité** des prescriptions depuis leur création jusqu’à leur validation.

**Problèmes métier traités** :
- Prescriptions papier → erreurs de transcription.
- Absence de priorisation automatique → retards pour les cas urgents.
- Non-respect des protocoles locaux → analyses inutiles ou inappropriées.
- Traçabilité insuffisante → impossibilité de retracer les actions en cas d’audit.

**Acteurs principalement concernés** :
- **Cliniciens prescripteurs** (urgentistes, réanimateurs, chirurgiens, services extérieurs).
- **Biologistes médicaux** (validation biologique).
- **Commission des Anti-infectieux et des Anticoagulants (CAI)** (définition des protocoles).
- **Système d’Information de Laboratoire (SIL)** (enregistrement, priorisation, traçabilité).

**Décisions clés** :
| **Décision** | **Acteur responsable** | **Informations nécessaires** | **Informations produites** | **Règles métier associées** |
|--------------|------------------------|------------------------------|---------------------------|-----------------------------|
| Prescrire un dosage anti-Xa en urgence | Clinicien prescripteur | - Identité du patient <br> - Service prescripteur <br> - Contexte clinique (ex. : hémorragie active) <br> - Protocoles locaux ou recommandations HAS/ANSM <br> - Historique des traitements en cours | - Prescription électronique (obligatoire) <br> - Statut de la demande : "en attente" <br> - Données contextuelles saisies (type d’AOD, posologie, heure de dernière prise, clairance de la créatinine) | **RME-01** : Prescription électronique obligatoire <br> **RME-02** : Respect des protocoles locaux <br> **RM-01** : Grille de priorisation automatique basée sur le contexte clinique |
| Valider ou rejeter une demande de dosage | Biologiste médical | - Demande reçue dans le SIL <br> - Données contextuelles complètes <br> - Protocoles locaux | - Statut de la demande : "validée" ou "rejetée" <br> - Justification du rejet (si applicable) | **RME-03** : Validation biologique obligatoire avant analyse <br> **RME-04** : Rejet des demandes non conformes (données manquantes, protocoles non respectés) |
| Classer une demande par niveau d’urgence | Biologiste médical (ou SIL si automatisé) | - Niveau d’urgence clinique (hémorragie active, chirurgie en urgence, etc.) <br> - Délais critiques définis <br> - Disponibilité des ressources | - Niveau de priorité attribué (urgence absolue, haute, modérée, routine) <br> - Ordonnancement des analyses | **RM-02** : Délais maximaux acceptables par niveau de priorité (ex. : urgence absolue ≤ 1h) |

**Informations structurantes** :
- **Données d’entrée** :
  - Identité du patient, service prescripteur, contexte clinique, type d’AOD, posologie, heure de la dernière prise, clairance de la créatinine, autres traitements.
- **Données de sortie** :
  - Statut de la demande, niveau de priorité, justification du rejet, données contextuelles validées.
- **Flux d’information** :
  - Prescription → Validation → Priorisation → Transmission au laboratoire.

**Règles métier spécifiques ou probables** :
- **RME-01** : Toute demande de dosage anti-Xa doit être formalisée via une **prescription électronique obligatoire** dans le SIL.
  - *Source* : 02_acteurs_du_domaine.md, 03_concepts_metier_initiaux.md.
  - *Justification* : Éviter les erreurs de transcription et garantir la traçabilité.
- **RME-02** : La prescription doit respecter les **indications définies par les protocoles de la CAI**.
  - *Source* : 02_acteurs_du_domaine.md.
  - *Justification* : Respecter les bonnes pratiques et éviter les prescriptions inappropriées.
- **RME-03** : Toute demande de dosage anti-Xa doit être **validée par un biologiste** avant analyse.
  - *Source* : 02_acteurs_du_domaine.md.
  - *Justification* : Garantir la pertinence clinique et éviter les analyses inutiles.
- **RME-04** : Les demandes **non conformes** (données manquantes, protocoles non respectés) doivent être **rejetées avec justification**.
  - *Source* : 04_regles_metier.md (RME-04).
  - *Justification* : Éviter les analyses inappropriées et les rejets d’échantillons.
- **RM-01** : **Grille de priorisation automatique** basée sur le contexte clinique.
  - *Exemples* :
    - Hémorragie active → urgence absolue (délai ≤ 1h).
    - Chirurgie programmée → urgence haute (délai ≤ 4h).
    - Contrôle systématique → urgence modérée (délai ≤ 24h).
    - Routine → délai ≤ 48h.
  - *Source* : 01_reformulation_du_besoin.md, 03_concepts_metier_initiaux.md, 05_priorites_exceptions_contraintes.md.
  - *Justification* : Optimiser les ressources et réduire les risques cliniques.
- **RM-02** : **Délais maximaux acceptables par niveau de priorité**.
  - *Exemples* :
    - Urgence absolue : ≤ 1h.
    - Urgence haute : ≤ 4h.
    - Urgence modérée : ≤ 24h.
    - Routine : ≤ 48h.
  - *Source* : 04_contraintes_et_risques.md, 05_priorites_exceptions_contraintes.md.
  - *Justification* : Garantir une prise en charge thérapeutique optimale.

**Indices du corpus** :
- **Problème métier principal** : "Gestion inefficace et non sécurisée des demandes urgentes de dosage anti-Xa" (01_reformulation_du_besoin.md).
- **Objectifs opérationnels** :
  - "Mise en place d’un système informatisé pour gérer les prescriptions" (01_reformulation_du_besoin.md).
  - "Priorisation automatique des demandes en fonction de leur urgence clinique" (01_reformulation_du_besoin.md).
- **Acteurs** :
  - Cliniciens prescripteurs (02_acteurs_du_domaine.md).
  - Biologistes médicaux (02_acteurs_du_domaine.md).
  - CAI (02_acteurs_du_domaine.md).
- **Décisions** :
  - Prescription électronique (03_decisions_informations_manipulees.md).
  - Validation biologique (03_decisions_informations_manipulees.md).
  - Priorisation (03_decisions_informations_manipulees.md, 05_priorites_exceptions_contraintes.md).

**Statut** : **Cœur stratégique** (valeur métier centrale : prise en charge optimale des patients sous AOD).

**Hypothèses à valider** :
1. **Automatisation de la priorisation** :
   - Le SIL doit-il classer automatiquement les demandes, ou cette tâche reste-t-elle manuelle pour les biologistes ?
   - *Source* : 05_vision_globale_du_domaine.md mentionne une "priorisation automatique", mais les critères ne sont pas détaillés.
2. **Critères exacts de rejet** :
   - Quels sont les seuils pour rejeter une demande (ex. : non-respect des protocoles, données manquantes) ?
   - *Source* : 04_regles_metier.md (RME-04) est incomplète.
3. **Rôle de la CAI dans la validation** :
   - La CAI valide-t-elle les protocoles, ou participe-t-elle aussi à la validation des demandes ?
   - *Source* : 02_acteurs_du_domaine.md mentionne la CAI, mais son rôle exact n’est pas précisé.

---

### 2.2. Sous-domaine 2 : Gestion pré-analytique et logistique des échantillons
**Finalité métier** :
Garantir que **tous les échantillons biologiques** (tubes de prélèvement) respectent les **exigences pré-analytiques strictes** avant analyse, et que leur **transport est optimisé** pour éviter les résultats invalides, les rejets d’échantillons et les retards critiques.

**Responsabilité métier principale** :
- **Vérifier la conformité** des tubes (type, volume, délai de transport, conditions de transport).
- **Signaler les non-conformités** en temps réel et déclencher des actions correctives.
- **Coordonner le transport** des échantillons entre les services et le laboratoire.
- **Archiver les échantillons non conformes** avec motif du rejet.

**Problèmes métier traités** :
- Non-conformité des tubes → résultats invalides ou rejets.
- Absence de vérification systématique → analyse d’échantillons non conformes.
- Retards dans le transport → dégradation des échantillons.
- Traçabilité insuffisante des non-conformités.

**Acteurs principalement concernés** :
- **Techniciens de laboratoire** (vérification de la conformité, préparation des échantillons).
- **Cliniciens prescripteurs** (vérification initiale des tubes avant envoi).
- **Personnel administratif** (coordination du transport).
- **Système d’Information de Laboratoire (SIL)** (vérification automatique des conformités, traçabilité).
- **Middleware de laboratoire** (routage des échantillons).

**Décisions clés** :
| **Décision** | **Acteur responsable** | **Informations nécessaires** | **Informations produites** | **Règles métier associées** |
|--------------|------------------------|------------------------------|---------------------------|-----------------------------|
| Vérifier la conformité d’un tube | Technicien de laboratoire (assisté par le SIL) | - Type de tube (citraté 3.2%) <br> - Volume minimal requis <br> - Délai maximal entre prélèvement et analyse (< 4h) <br> - Conditions de transport (température 15-25°C, protection de la lumière) | - Statut de conformité : "conforme" ou "non conforme" <br> - Alerte au biologiste si non conforme | **RMP-01** : Critères de conformité des tubes <br> **RMP-02** : Procédure de gestion des non-conformités |
| Signaler une non-conformité ou un résultat aberrant | Technicien de laboratoire | - Détection d’une non-conformité ou d’un résultat aberrant <br> - Procédure de gestion des non-conformités | - Alerte au biologiste <br> - Demande de complément (nouveau prélèvement) si nécessaire <br> - Archivage de l’échantillon non conforme avec motif | **RMP-03** : Archivage des échantillons non conformes <br> **RMP-04** : Signalement immédiat des non-conformités |
| Coordonner le transport des échantillons | Personnel administratif | - Statut des prélèvements (en attente, en cours, terminés) <br> - Alertes de non-conformité ou de retard | - Relance du service prescripteur <br> - Mise à jour du statut dans le SIL | **RMP-05** : Délais maximaux de transport <br> **RMP-06** : Conditions de transport |

**Informations structurantes** :
- **Données d’entrée** :
  - Type de tube, volume, heure de prélèvement, heure d’arrivée au laboratoire, température de transport, statut de conformité.
- **Données de sortie** :
  - Statut de conformité, motif de rejet, demande de complément, archivage des échantillons non conformes.
- **Flux d’information** :
  - Prélèvement → Vérification de la conformité → Transport → Archivage.

**Règles métier spécifiques ou probables** :
- **RMP-01** : **Critères de conformité des tubes**.
  - *Exemples* :
    - Type de tube : citraté 3.2% (ex. : BD Vacutainer 9NC 3.2%).
    - Volume minimal : 1.8 mL à 2.7 mL (selon l’analyseur).
    - Délai maximal entre prélèvement et analyse : < 4 heures.
    - Conditions de transport : température entre 15°C et 25°C, protection de la lumière.
  - *Source* : 04_contraintes_et_risques.md, 03_concepts_metier_initiaux.md.
  - *Justification* : Garantir la validité des résultats et éviter les rejets.
- **RMP-02** : **Procédure de gestion des non-conformités**.
  - *Exemples* :
    - Refus systématique de l’échantillon.
    - Demande de complément (nouveau prélèvement).
    - Escalade vers le biologiste pour décision.
  - *Source* : 04_contraintes_et_risques.md.
  - *Justification* : Éviter les résultats invalides et les retards.
- **RMP-03** : **Archivage des échantillons non conformes**.
  - *Source* : Hypothèse basée sur les bonnes pratiques de laboratoire (ISO 15189).
  - *Justification* : Preuve de conformité et traçabilité.
- **RMP-04** : **Signalement immédiat des non-conformités**.
  - *Source* : 04_contraintes_et_risques.md.
  - *Justification* : Permettre une action corrective rapide.
- **RMP-05** : **Délais maximaux de transport**.
  - *Exemple* : Délai < 4 heures entre prélèvement et analyse.
  - *Source* : 04_cont