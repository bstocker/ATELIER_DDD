```markdown
# Conflits d’objectifs et arbitrages
**Domaine métier** : Gestion des demandes urgentes de dosage anti-Xa dans le SIL
**Date** : [À compléter]
**Version** : 1.0
**Auteurs** : Analyste Métier
**Sources** : Livrables étape 1 (01_reformulation_du_besoin.md, 02_acteurs_du_domaine.md, 03_concepts_metier_initiaux.md, 04_contraintes_et_risques.md, 05_vision_globale_du_domaine.md)

---

## 1. Introduction
Ce document identifie et analyse les **tensions, conflits d'objectifs et arbitrages** potentiels entre les acteurs du domaine des **demandes urgentes de dosage anti-Xa**, afin de :
- Mettre en lumière les **divergences d'intérêts** entre parties prenantes
- Identifier les **tensions organisationnelles ou métier**
- Proposer des **arbitrages** pour garantir un circuit sécurisé, priorisé et traçable
- Formuler des **questions clés** à poser aux experts métier

Ces conflits peuvent émerger de :
- **Objectifs contradictoires** entre acteurs
- **Contraintes réglementaires vs. contraintes opérationnelles**
- **Priorités divergentes** (ex. : rapidité vs. exhaustivité)
- **Responsabilités partagées** mal définies
- **Ressources limitées** (temps, personnel, budget)

---

## 2. Conflits d'objectifs identifiés

### 2.1. Conflit entre cliniciens et biologistes

| **Conflit** | **Acteurs concernés** | **Description** | **Causes probables** | **Impacts métier** | **Arbitrage nécessaire** | **Questions à poser** |
|-------------|-----------------------|-----------------|-----------------------|--------------------|--------------------------|-----------------------|
| **Priorisation des demandes** | Cliniciens vs. Biologistes | Les cliniciens veulent une réponse immédiate pour leurs patients, tandis que les biologistes doivent prioriser les analyses en fonction de critères cliniques objectifs. | - Urgences perçues différemment (ex. : chirurgie programmée vs. hémorragie active) <br> - Manque de règles claires de priorisation dans le SIL actuel | - Retard dans les cas critiques <br> - Surcharge du laboratoire <br> - Frustration des cliniciens | Définir une **grille de priorisation objective** intégrée au SIL, avec des critères cliniques validés par la CAI. Mettre en place un **système d'alerte automatique** pour les cas urgents. | - Quels sont les critères **exacts** pour classer une demande en "urgence absolue" ? <br> - Qui a l'autorité finale en cas de désaccord ? <br> - Comment gérer les conflits de priorité (ex. : deux urgences absolues simultanées) ? |
| **Validation des demandes** | Cliniciens vs. Biologistes | Les cliniciens veulent que toutes leurs demandes soient traitées rapidement, tandis que les biologistes doivent valider la pertinence clinique. | - Prescriptions non conformes aux protocoles <br> - Demandes redondantes ou inappropriées | - Retard dans le traitement des cas légitimes <br> - Surcharge administrative <br> - Risque de rejet des échantillons non conformes | Établir des **critères de rejet clairs** et une **procédure de validation automatisée** pour les demandes conformes aux protocoles. Prévoir un **feedback immédiat** aux cliniciens en cas de non-conformité. | - Quels sont les **seuils exacts** pour rejeter une demande ? <br> - Comment informer le clinicien en cas de rejet ? <br> - Qui valide la conformité des demandes en cas de désaccord ? |

---

### 2.2. Conflit entre biologistes et techniciens de laboratoire

| **Conflit** | **Acteurs concernés** | **Description** | **Causes probables** | **Impacts métier** | **Arbitrage nécessaire** | **Questions à poser** |
|-------------|-----------------------|-----------------|-----------------------|--------------------|--------------------------|-----------------------|
| **Validation des tubes** | Biologistes vs. Techniciens | Les techniciens veulent traiter tous les échantillons reçus, tandis que les biologistes doivent rejeter les tubes non conformes pour éviter des résultats erronés. | - Manque de formation des techniciens sur les exigences pré-analytiques <br> - Absence de vérification automatique dans le SIL | - Résultats invalides → erreurs d'interprétation <br> - Perte de temps et de ressources <br> - Frustration des techniciens face aux rejets | Définir une **procédure standardisée** pour la validation des tubes, avec des **critères de conformité clairs** et un **système d'alerte automatique** pour les non-conformités. Former les techniciens aux exigences pré-analytiques. | - Quels sont les **critères exacts** de conformité des tubes ? <br> - Qui valide définitivement la conformité : technicien, biologiste ou système automatisé ? <br> - Comment gérer les échantillons non conformes en dehors des heures ouvrables ? |
| **Saisie des résultats** | Biologistes vs. Techniciens | Les techniciens veulent saisir rapidement les résultats pour libérer le SIL, tandis que les biologistes doivent valider ces résultats avant interprétation. | - Saisie manuelle des résultats → erreurs de transcription <br> - Absence d'intégration automatique entre analyseurs et SIL | - Résultats erronés → erreurs d'interprétation <br> - Retard dans la validation <br> - Surcharge des biologistes | **Automatiser la transmission des résultats** depuis les analyseurs vers le SIL. Mettre en place un **système de double vérification** pour les résultats critiques. Former les techniciens à la saisie précise. | - Les analyseurs sont-ils **compatibles** avec le SIL actuel ? <br> - Quels sont les **seuils d'alerte** pour les résultats aberrants ? <br> - Comment gérer les erreurs de saisie détectées après validation ? |

---

### 2.3. Conflit entre cliniciens et patients

| **Conflit** | **Acteurs concernés** | **Description** | **Causes probables** | **Impacts métier** | **Arbitrage nécessaire** | **Questions à poser** |
|-------------|-----------------------|-----------------|-----------------------|--------------------|--------------------------|-----------------------|
| **Accès aux résultats** | Cliniciens vs. Patients | Les cliniciens veulent contrôler l'accès aux résultats pour éviter l'anxiété des patients, tandis que les patients demandent un accès direct à leurs données. | - Crainte de mauvaise interprétation par le patient <br> - Respect du RGPD et de la confidentialité | - Frustration des patients <br> - Risque de mauvaise interprétation des résultats <br> - Charge supplémentaire pour les cliniciens | Mettre en place un **portail patient sécurisé** avec accès limité aux résultats validés et accompagnés de commentaires cliniques. Prévoir un **système de messagerie sécurisée** pour les questions des patients. | - Quelles **données** doivent être accessibles aux patients ? <br> - Comment **former les patients** à l'interprétation des résultats ? <br> - Qui valide le contenu du portail patient ? |

---
### 2.4. Conflit entre DSI et utilisateurs (cliniciens/biologistes)

| **Conflit** | **Acteurs concernés** | **Description** | **Causes probables** | **Impacts métier** | **Arbitrage nécessaire** | **Questions à poser** |
|-------------|-----------------------|-----------------|-----------------------|--------------------|--------------------------|-----------------------|
| **Évolutivité du SIL** | DSI vs. Cliniciens/Biologistes | La DSI veut une solution robuste et évolutive, tandis que les cliniciens/biologistes veulent une interface simple et rapide. | - Complexité technique vs. simplicité d'utilisation <br> - Budget et délais contraints | - Rejet de la solution par les utilisateurs <br> - Surcharge de la DSI pour des ajustements constants <br> - Retard dans le déploiement | Impliquer les **utilisateurs finaux** dès la phase de conception. Prévoir des **tests utilisateurs** avant déploiement. Mettre en place un **comité de pilotage** pour arbitrer les compromis. | - Quels sont les **besoins fonctionnels critiques** pour les cliniciens et biologistes ? <br> - Quel est le **budget disponible** pour le projet ? <br> - Quels sont les **délais impartis** pour le déploiement ? |

---
### 2.5. Conflit entre CAI et autres acteurs

| **Conflit** | **Acteurs concernés** | **Description** | **Causes probables** | **Impacts métier** | **Arbitrage nécessaire** | **Questions à poser** |
|-------------|-----------------------|-----------------|-----------------------|--------------------|--------------------------|-----------------------|
| **Mise à jour des protocoles** | CAI vs. Cliniciens/Biologistes | La CAI veut des protocoles stricts pour garantir la qualité, tandis que les cliniciens/biologistes veulent de la flexibilité pour adapter les traitements. | - Protocoles perçus comme trop rigides <br> - Évolution rapide des recommandations médicales | - Non-respect des protocoles → risque clinique <br> - Frustration des cliniciens <br> - Retard dans l'adaptation des traitements | **Actualiser régulièrement les protocoles** en fonction des dernières recommandations. Prévoir des **exceptions formalisées** pour les cas particuliers. Former les cliniciens aux protocoles. | - À quelle **fréquence** les protocoles doivent-ils être mis à jour ? <br> - Quels sont les **cas d'exception** autorisés ? <br> - Comment **former les cliniciens** aux nouveaux protocoles ? |

---
### 2.6. Conflit entre sécurité des données et accessibilité

| **Conflit** | **Acteurs concernés** | **Description** | **Causes prob