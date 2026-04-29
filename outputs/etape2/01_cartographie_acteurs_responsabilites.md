```markdown
# Cartographie des acteurs et responsabilités
**Domaine métier** : Gestion des demandes urgentes de dosage anti-Xa dans le SIL
**Date** : [À compléter]
**Version** : 1.0
**Auteurs** : Analyste Métier
**Sources** : Livrables étape 1 (01_reformulation_du_besoin.md, 02_acteurs_du_domaine.md, 03_concepts_metier_initiaux.md, 04_contraintes_et_risques.md, 05_vision_globale_du_domaine.md)

---

## 1. Introduction
Ce document structure les acteurs impliqués dans le domaine des **demandes urgentes de dosage anti-Xa**, en précisant leur rôle, leurs responsabilités, leurs interactions et les points à clarifier. Il s’appuie sur les livrables de l’étape 1 et met en évidence les **responsabilités partagées**, les **ambiguïtés** et les **règles métier implicites** à valider avec les experts.

---

## 2. Acteurs humains

### 2.1. Cliniciens prescripteurs
**Services concernés** :
- Urgences
- Réanimation
- Bloc opératoire
- Services extérieurs (ex. : cardiologie, médecine interne)

**Rôle métier** :
- Prescrire un dosage anti-Xa en urgence pour les patients sous AOD.
- Évaluer le **contexte clinique** du patient (ex. : hémorragie active, chirurgie programmée).
- Saisir les **données contextuelles** nécessaires à l’interprétation (type d’AOD, posologie, heure de la dernière prise, fonction rénale).
- Adapter le traitement anticoagulant en fonction des résultats et des recommandations.

**Responsabilités principales** :
| Responsabilité | Détail | Source |
|----------------|--------|--------|
| Respect des indications | Prescrire le dosage anti-Xa uniquement selon les protocoles locaux ou recommandations HAS/ANSM. | 02_acteurs_du_domaine.md |
| Saisie des données contextuelles | Renseigner obligatoirement : type d’AOD, posologie, heure de la dernière prise, clairance de la créatinine, contexte clinique. | 03_concepts_metier_initiaux.md, 04_contraintes_et_risques.md |
| Vérification des tubes | Contrôler la conformité des tubes avant envoi au laboratoire (si applicable). | 02_acteurs_du_domaine.md |
| Utilisation des résultats | Adapter la prise en charge thérapeutique en fonction des résultats et des recommandations du biologiste. | 02_acteurs_du_domaine.md |
| Transmission des informations | Informer le patient des résultats et des actions thérapeutiques. | 02_acteurs_du_domaine.md |

**Responsabilités partagées/ambiguës** :
- **Priorisation des demandes** : Les cliniciens doivent-ils classer manuellement les demandes par urgence, ou cette tâche est-elle automatisée par le SIL ? *(À clarifier : 05_vision_globale_du_domaine.md mentionne une "priorisation automatique", mais les critères ne sont pas détaillés.)*
- **Validation des tubes** : La vérification de la conformité des tubes est-elle une responsabilité exclusive du clinicien, ou peut-elle être déléguée au système (ex. : alerte automatique dans le SIL) ? *(Hypothèse : le clinicien reste responsable, mais le SIL peut l’assister via des alertes.)*

**Décisions clés** :
- Décider de la nécessité du dosage anti-Xa en urgence.
- Classer manuellement la demande par niveau d’urgence si le SIL ne le fait pas automatiquement.
- Valider la conformité des tubes avant envoi.

**Informations manipulées** :
- Identité du patient.
- Service prescripteur.
- Type d’AOD (apixaban, rivaroxaban, édoxaban, etc.).
- Posologie et heure de la dernière prise.
- Clairance de la créatinine (fonction rénale).
- Contexte clinique (ex. : hémorragie active, chirurgie programmée).
- Résultat du dosage anti-Xa (reçu via le SIL ou le biologiste).
- Recommandations thérapeutiques (ex. : adaptation de la posologie, administration d’un antidote).

**Interactions majeures** :
| Acteur | Type d'interaction | Enjeu |
|--------|--------------------|-------|
| **SIL** | Prescription électronique, saisie des données contextuelles. | Rapidité et exhaustivité des données. |
| **Laboratoire** | Transmission des échantillons et des demandes. | Respect des délais et conformité des tubes. |
| **Biologiste** | Communication des résultats et recommandations. | Adaptation thérapeutique optimale. |
| **Pharmacien** | Collaboration pour l’adaptation du traitement. | Cohérence du traitement avec les résultats. |
| **Patient** | Information sur les résultats et les actions. | Transparence et adhésion au traitement. |

**Points à clarifier** :
1. **Critères de priorisation** : Quels sont les seuils exacts pour classer une demande en "urgence absolue", "haute", ou "basse" ? *(Exemple : hémorragie active = urgence absolue, chirurgie programmée = haute.)*
2. **Intégration des données contextuelles** : Les données de fonction rénale et de posologie sont-elles saisies manuellement ou récupérées automatiquement depuis le DPI ? *(03_concepts_metier_initiaux.md mentionne une intégration nécessaire, mais la méthode n’est pas précisée.)*
3. **Rôle dans la gestion des non-conformités** : Que faire si un tube est non conforme ? Le clinicien doit-il refaire le prélèvement immédiatement, ou peut-il attendre une alerte du système ? *(04_contraintes_et_risques.md souligne le risque de rejet des échantillons.)*

---

### 2.2. Biologistes médicaux
**Rôle métier** :
- Valider les demandes de dosage anti-Xa et **prioriser les analyses** en fonction de l’urgence clinique.
- Interpréter les résultats en tenant compte :
  - Du type d’AOD et de la posologie.
  - De l’heure de la dernière prise.
  - De la fonction rénale du patient.
  - Du contexte clinique (ex. : suspicion de surdosage).
- Rédiger un **compte-rendu d’interprétation** avec recommandations thérapeutiques si nécessaire.
- Garantir la **qualité et la fiabilité** des résultats.

**Responsabilités principales** :
| Responsabilité | Détail | Source |
|----------------|--------|--------|
| Validation des demandes | Vérifier la cohérence de la prescription avec les protocoles locaux. | 02_acteurs_du_domaine.md |
| Priorisation des analyses | Classer les demandes par urgence (ex. : hémorragie active en priorité absolue). | 03_concepts_metier_initiaux.md |
| Interprétation des résultats | Analyser le résultat du dosage anti-Xa en fonction du contexte clinique et des données patients. | 02_acteurs_du_domaine.md |
| Rédaction de recommandations | Émettre des conseils thérapeutiques (ex. : adaptation de la posologie, arrêt temporaire du traitement). | 02_acteurs_du_domaine.md |
| Respect des délais critiques | Garantir que les résultats sont interprétés et transmis dans les délais impartis. | 04_contraintes_et_risques.md |
| Traçabilité | Assurer l’enregistrement systématique des actions (audit trail). | 03_concepts_metier_initiaux.md |
| Supervision des techniciens | Valider les résultats bruts saisis par les techniciens. | 02_acteurs_du_domaine.md |

**Responsabilités partagées/ambiguës** :
- **Priorisation automatique vs. manuelle** : La priorisation est-elle entièrement automatisée par le SIL, ou le biologiste peut-il ajuster manuellement l’ordre des analyses ? *(05_vision_globale_du_domaine.md mentionne une "priorisation automatique", mais les règles métiers ne sont pas détaillées.)*
- **Validation des tubes** : Le biologiste est-il responsable de la validation finale des tubes, ou cette tâche est-elle partagée avec les techniciens ? *(02_acteurs_du_domaine.md attribue cette responsabilité aux techniciens, mais le biologiste peut avoir un rôle de supervision.)*

**Décisions clés** :
- Valider ou rejeter une demande de dosage.
- Classer une demande en urgence absolue, haute, ou basse.
- Interpréter un résultat de dosage anti-Xa et émettre des recommandations thérapeutiques.
- Gérer les cas de non-conformité des tubes (ex. : demander un nouveau prélèvement).

**Informations manipulées** :
- Demande de dosage (prescription électronique).
- Données contextuelles (type d’AOD, posologie, heure de la dernière prise, fonction rénale, contexte clinique).
- Résultat brut du dosage anti-Xa (transmis par l’analyseur ou le technicien).
- Compte-rendu d’interprétation (avec recommandations thérapeutiques).
- Historique des actions (audit trail).

**Interactions majeures** :
| Acteur | Type d'interaction | Enjeu |
|--------|--------------------|-------|
| **SIL** | Validation des résultats, saisie des interprétations. | Traçabilité et sécurité des données. |
| **Cliniciens** | Communication des résultats et recommandations. | Adaptation thérapeutique optimale. |
| **Techniciens de laboratoire** | Supervision des analyses et transmission des résultats bruts. | Fiabilité des données. |
| **Pharmaciens** | Collaboration pour l’adaptation du traitement. | Cohérence du traitement. |
| **Équipe de gestion des risques** | Signalement des incidents (ex. : retard, erreur d’interprétation). | Amélioration continue des processus. |

**Points à clarifier** :
1. **Grille d’interprétation** : Quels sont les seuils exacts pour chaque AOD (apixaban, rivaroxaban, édoxaban) en fonction du contexte clinique ? *(Exemple : pour l’apixaban, un résultat > 1.5 UI/mL peut indiquer un surdosage en cas d’insuffisance rénale.)*
2. **Recommandations thérapeutiques** : Qui valide les recommandations émises par le biologiste ? Le pharmacien peut-il les contester ? *(02_acteurs_du_domaine.md mentionne une collaboration, mais les responsabilités ne sont pas précisées.)*
3. **Gestion des astreintes** : En dehors des heures ouvrables, qui valide les résultats et émet les recommandations ? *(04_contraintes_et_risques.md souligne l’importance de l’astreinte biologique.)*

---

### 2.3. Techniciens de laboratoire
**Rôle métier** :
- Préparer et analyser les échantillons biologiques (dosage anti-Xa).
- Vérifier la **conformité des tubes** (type, volume, délai de transport).
- Saisir les **résultats bruts** dans le SIL.
- Participer à la maintenance des équipements de dosage.

**Responsabilités principales** :
| Responsabilité | Détail | Source |
|----------------|--------|--------|
| Préparation des échantillons | Centrifugation, dilution si nécessaire, vérification de la conformité des tubes. | 02_acteurs_du_domaine.md |
| Réalisation de l’analyse | Effectuer le dosage anti-Xa sur l’analyseur. | 02_acteurs_du_domaine.md |
| Saisie des résultats | Transmettre les résultats bruts au SIL (manuellement ou automatiquement). | 02_acteurs_du_domaine.md |
| Signalement des non-conformités | Alerter le biologiste en cas de tube non conforme ou de résultat aberrant. | 04_contraintes_et_risques.md |
| Maintenance des équipements | Respecter les procédures de contrôle qualité et de maintenance. | 02_acteurs_du_domaine.md |

**Responsabilités partagées/ambiguës** :
- **Validation des tubes** : Le technicien est-il responsable de la validation finale, ou cette tâche est-elle partagée avec le biologiste ? *(02_acteurs_du_domaine.md attribue cette responsabilité aux techniciens, mais le biologiste peut avoir un rôle de supervision.)*
- **Saisie des résultats** : La saisie est-elle manuelle ou automatisée (intégration entre l’analyseur et le SIL) ? *(05_vision_globale_du_domaine.md mentionne une intégration nécessaire, mais la méthode n’est pas précisée.)*

**Décisions clés** :
- Valider la conformité d’un tube avant analyse.
- Signaler une non-conformité ou un résultat aberrant au biologiste.
- Corriger une erreur de saisie si détectée.

**Informations manipulées** :
- Échantillons biologiques (tubes).
- Résultats bruts du dosage anti-Xa.
- Logs de maintenance des équipements.
- Alertes de non-conformité.

**Interactions majeures** :
| Acteur | Type d'interaction | Enjeu |
|--------|--------------------|-------|
| **SIL** | Saisie des résultats, gestion des échantillons. | Fiabilité des données. |
| **Biologistes** | Transmission des résultats bruts et alertes. | Qualité des analyses. |
| **Analyseurs** | Transmission automatique des résultats (si intégration disponible). | Rapidité et précision. |
| **Personnel administratif** | Coordination des prélèvements et du transport. | Respect des délais. |

**Points à clarifier** :
1. **Critères de conformité des tubes** : Quels sont les seuils exacts pour le volume, le type de tube et le délai de transport ? *(04_contraintes_et_risques.md souligne l’importance des exigences pré-analytiques.)*
2. **Intégration avec les analyseurs** : Les résultats sont-ils transmis automatiquement au SIL, ou la saisie est-elle manuelle ? *(05_vision_globale_du_domaine.md mentionne une intégration nécessaire.)*
3. **Procédure de gestion des non-conformités** : Que faire si un tube est non conforme ? Le technicien doit-il refuser l’analyse immédiatement, ou peut-il demander une validation au biologiste ? *(04_contraintes_et_risques.md souligne le risque de rejet des échantillons.)*

---

### 2.4. Pharmaciens hospitaliers
**Rôle métier** :
- Conseiller les cliniciens sur le **choix et l’adaptation des anticoagulants** (AOD).
- Analyser les **interactions médicamenteuses** et les contre-indications.
- Participer à la gestion des **urgences hémorragiques** (ex. : administration d’antidotes comme l’andexanet alfa).
- Vérifier la **cohérence du traitement** avec les résultats du dosage anti-Xa.

**Responsabilités principales** :
| Responsabilité | Détail | Source |
|----------------|--------|--------|
| Conseil thérapeutique | Recommander l’adaptation des AOD en fonction des résultats et du contexte clinique. | 02_acteurs_du_domaine.md |
| Analyse des interactions | Identifier les risques d’interactions médicamenteuses (ex. : AOD + antiagrégants). | 02_acteurs_du_domaine.md |
| Gestion des urgences hémorragiques | Proposer l’administration d’antidotes si nécessaire. | 02_acteurs_du_domaine.md |
| Collaboration pluridisciplinaire | Travailler avec les cliniciens et les biologistes pour optimiser le traitement. | 02_acteurs_du_domaine.md |

**Responsabilités partagées/ambiguës** :
- **Validation des recommandations** : Les recommandations du biologiste sont-elles systématiquement validées par le pharmacien, ou cette tâche est-elle partagée ? *(02_acteurs_du_domaine.md mentionne une collaboration, mais les responsabilités ne sont pas précisées.)*
- **Décision finale** : En cas de divergence entre le biologiste et le pharmacien, qui prend la décision finale ? *(Hypothèse : le clinicien, en dernier recours.)*

**Décisions clés** :
- Proposer l’administration d’un antidote (ex. : andexanet alfa).
- Adapter la posologie d’un AOD en fonction des résultats et des interactions.
- Valider ou contester les recommandations du biologiste.

**Informations manipulées** :
- Prescriptions d’AOD.
- Résultats du dosage anti-Xa.
- Données d’interactions médicamenteuses.
- Protocoles locaux de gestion des urgences hémorragiques.

**Interactions majeures** :
| Acteur | Type d'interaction | Enjeu |
|--------|--------------------|-------|
| **Cliniciens** | Collaboration pour l’adaptation du traitement. | Cohérence thérapeutique. |
| **Biologistes** | Validation des recommandations thérapeutiques. | Optimisation du traitement. |
| **SIL** | Accès aux données patients et aux résultats. | Prise de décision éclairée. |

**Points à clarifier** :
1. **Rôle dans l’urgence hémorragique** : Le pharmacien est-il systématiquement impliqué dans la gestion des hémorragies actives, ou cette tâche est-elle partagée avec le biologiste ? *(02_acteurs_du_domaine.md mentionne une collaboration, mais les responsabilités ne sont pas précisées.)*
2. **Validation des recommandations** : Qui valide les recommandations émises par le biologiste ? Le pharmacien peut-il les modifier ? *(02_acteurs_du_domaine.md mentionne une collaboration, mais les responsabilités ne sont pas précisées.)*

---
### 2.5. Personnel administratif / Coordinateurs de soins
**Rôle métier** :
- Gérer les **flux de demandes** entre les services et le laboratoire.
- Coordonner les **prélèvements** et le **transport des échantillons**.
- Suivre les **délais de traitement** des demandes.

**Responsabilités principales** :
| Responsabilité | Détail | Source |
|----------------|--------|--------|
| Organisation des prélèvements | Planifier les prélèvements en urgence et s’assurer de leur réalisation. | 02_acteurs_du_domaine.md |
| Gestion du transport | Organiser l’acheminement rapide des tubes vers le laboratoire. | 02_acteurs_du_domaine.md |
| Suivi des délais | Vérifier que les demandes sont traitées dans les délais impartis. | 04_contraintes_et_risques.md |
| Coordination pluridisciplinaire | Faciliter la communication entre les services et le laboratoire. | 02_acteurs_du_domaine.md |

**Responsabilités partagées/ambiguës** :
- **Gestion des non-conformités** : Que faire si un prélèvement est non conforme ? Le personnel administratif doit-il relancer le service prescripteur ? *(04_contraintes_et_risques.md souligne le risque de rejet des échantillons.)*

**Décisions clés** :
- Relancer un service si un prélèvement est en retard.
- Gérer les cas de non-conformité des tubes (ex. : demander un nouveau prélèvement).

**Informations manipulées** :
- Liste des demandes urgentes.
- Statut des prélèvements (en attente, en cours, terminés).
- Alertes de non-conformité ou de retard.

**Interactions majeures** :
| Acteur | Type d'interaction | Enjeu |
|--------|--------------------|-------|
| **Cliniciens** | Organisation des prélèvements. | Respect des délais. |
| **Laboratoire** | Suivi des échantillons. | Traçabilité et rapidité. |
| **SIL** | Mise à jour des statuts des demandes. | Visibilité en temps réel. |

**Points à clarifier** :
1. **Procédure de relance** : En cas de retard ou de non-conformité, qui est responsable de la relance ? Le personnel administratif, le biologiste, ou le système automatisé ? *(04_contraintes_et_risques.md souligne l’importance de la traçabilité.)*
2. **Gestion des astreintes** : Qui coordonne les prélèvements en dehors des heures ouvrables ? *(04_contraintes_et_risques.md souligne l’importance de l’astreinte biologique.)*

---
### 2.6. Patients
**Rôle métier** :
- Être informé de la **nécessité du dosage** et des **résultats**.
- Donner son **consentement éclairé** pour l’analyse (si applicable).
- Informer les cliniciens de la **dernière prise d’AOD** et des **effets indésirables**.

**Responsabilités principales** :
| Responsabilité | Détail | Source |
|----------------|--------|--------|
| Information sur les résultats | Accéder aux résultats via un portail patient (si disponible). | 02_acteurs_du_domaine.md |
| Consentement | Donner son accord pour le dosage (si requis par la réglementation). | 03_concepts_metier_initiaux.md |
| Signalement des effets indésirables | Informer les cliniciens en cas de saignement ou autre symptôme. | 02_acteurs_du_domaine.md |

**Responsabilités partagées/ambiguës** :
- **Accès aux résultats** : Le patient a-t-il accès à ses résultats via un portail dédié, ou cette information est-elle transmise uniquement par les cliniciens ? *(02_acteurs_du_domaine.md mentionne un rôle implicite, mais l’accès n’est pas précisé.)*

**Décisions clés** :
- Donner son consentement pour le dosage.
- Signaler un effet indésirable (ex. : saignement).

**Informations manipulées** :
- Résultats du dosage anti-Xa.
- Recommandations thérapeutiques.
- Consentement éclairé.

**Interactions majeures** :
| Acteur | Type d'interaction | Enjeu |
|--------|--------------------|-------|
| **Cliniciens** | Communication des résultats et des actions. | Transparence et adhésion au traitement. |
| **SIL** | Accès aux résultats via un portail patient. | Autonomie du patient. |

**Points à clarifier** :
1. **Portail patient** : Un portail patient sera-t-il mis en place pour accéder aux résultats ? Si oui, quelles données seront accessibles ? *(02_acteurs_du_domaine.md mentionne un rôle implicite, mais l’accès n’est pas précisé.)*
2. **Consentement** : Le consentement du patient est-il systématiquement requis pour les dosages urgents, ou cette exigence est-elle levée en cas d’urgence vitale ? *(Hypothèse : le consentement est implicite en cas d’urgence.)*

---
## 3. Acteurs organisationnels

### 3.1. Comité de pilotage du projet SIL
**Rôle métier** :
- Superviser l’évolution du SIL pour intégrer le circuit des demandes urgentes de dosage anti-Xa.

**Responsabilités principales** :
| Responsabilité | Détail | Source |
|----------------|--------|--------|
| Validation des priorités | Valider les fonctionnalités prioritaires du nouveau circuit. | 02_acteurs_du_domaine.md |
| Allocation des ressources | Allouer les budgets et les équipes nécessaires au projet. | 02_acteurs_du_domaine.md |
| Suivi du projet | Assurer le suivi des délais et des livrables. | 02_acteurs_du_domaine.md |

**Interactions majeures** :
| Acteur | Type d'interaction | Enjeu |
|--------|--------------------|-------|
| **DSI** | Suivi technique et budgétaire. | Réussite du projet. |
| **Biologistes** | Recueil des besoins fonctionnels. | Adéquation avec les attentes métier. |
| **Cliniciens** | Validation des processus. | Acceptation par les utilisateurs. |

**Points à clarifier** :
1. **Budget et planning** : Quel est le budget alloué au projet, et quels sont les délais impartis ? *(05_vision_globale_du_domaine.md mentionne ces éléments, mais ils ne sont pas détaillés.)*

---
### 3.2. Commission des Anti-infectieux et des Anticoagulants (CAI)
**Rôle métier** :
- Définir les **protocoles locaux** pour la prescription, l’analyse et l’interprétation des dosages anti-Xa.

**Responsabilités principales** :
| Responsabilité | Détail | Source |
|----------------|--------|--------|
| Mise à jour des protocoles | Adapter les protocoles en fonction des recommandations HAS/ANSM et des bonnes pratiques. | 02_acteurs_du_domaine.md |
| Formation des équipes | Organiser des sessions de formation sur les nouveaux protocoles. | 02_acteurs_du_domaine.md |
| Audit des pratiques | Vérifier le respect des protocoles par les cliniciens et les biologistes. | 02_acteurs_du_domaine.md |

**Interactions majeures** :
| Acteur | Type d'interaction | Enjeu |
|--------|--------------------|-------|
| **Cliniciens** | Diffusion des protocoles. | Harmonisation des pratiques. |
| **Biologistes** | Validation des grilles d’interprétation. | Cohérence des recommandations. |
| **Pharmaciens** | Collaboration pour la gestion des urgences hémorragiques. | Optimisation des traitements. |

**Points à clarifier** :
1. **Protocoles locaux** : Quels sont les protocoles actuels pour la prescription et l’interprétation des dosages anti-Xa ? *(02_acteurs_du_domaine.md mentionne la CAI, mais les protocoles ne sont pas détaillés.)*
2. **Fréquence de mise à jour** : À quelle fréquence les protocoles sont-ils révisés ? *(Hypothèse : au moins une fois par an, ou en cas de changement des recommandations HAS/ANSM.)*

---
### 3.3. Équipe de gestion des risques
**Rôle métier** :
- Identifier et atténuer les **risques** liés au circuit des demandes urgentes de dosage anti-Xa.

**Responsabilités principales** :
| Responsabilité | Détail | Source |
|----------------|--------|--------|
| Analyse des risques | Identifier les risques cliniques, réglementaires et opérationnels. | 04_contraintes_et_risques.md |
| Mise en place de barrières | Implémenter des alertes automatiques et des procédures de secours. | 04_contraintes_et_risques.md |
| Audit des processus | Vérifier le respect des bonnes pratiques et des normes. | 04_contraintes_et_risques.md |

**Interactions majeures** :
| Acteur | Type d'interaction | Enjeu |
|--------|--------------------|-------|
| **Laboratoire** | Signalement des incidents. | Amélioration continue. |
| **DSI** | Mise en place de mécanismes de sécurité. | Conformité réglementaire. |
| **Direction** | Rapport des risques identifiés. | Prise de décision stratégique. |

**Points à clarifier** :
1. **Liste des risques** : Quels sont les risques prioritaires identifiés pour le circuit actuel ? *(04_contraintes_et_risques.md liste les risques, mais une priorisation serait utile.)*
2. **Barrières de sécurité** : Quelles barrières de sécurité (ex. : alertes automatiques) sont déjà en place, et lesquelles doivent être ajoutées ? *(04_contraintes_et_risques.md souligne l’importance des alertes.)*

---
## 4. Acteurs techniques

### 4.1. Système d'Information de Laboratoire (SIL)
**Rôle métier** :
- Centraliser les **demandes de dosage**, les **résultats** et les **données contextuelles**.
- Automatiser la **priorisation** des demandes.
- Assurer la **traçabilité** et la **sécurité** des données.

**Responsabilités principales** :
| Responsabilité | Détail | Source |
|----------------|--------|--------|
| Gestion des demandes | Enregistrer les prescriptions électroniques et les données contextuelles. | 02_acteurs_du_domaine.md |
| Priorisation automatique | Classer les demandes par urgence en fonction de règles métiers prédéfinies. | 03_concepts_metier_initiaux.md |
| Vérification des conformités | Alerter en cas de non-conformité des tubes ou de délai de transport dépassé. | 04_contraintes_et_risques.md |
| Traçabilité | Enregistrer systématiquement toutes les actions (audit trail). | 03_concepts_metier_initiaux.md |
| Sécurité des données | Mettre en place une authentification forte et des droits d’accès différenciés. | 04_contraintes_et_risques.md |
| Intégration avec les systèmes externes | Échanger des données avec le DPI, les analyseurs et les middleware. | 05_vision_globale_du_domaine.md |

**Responsabilités partagées/ambiguës** :
- **Validation des demandes** : Le SIL valide-t-il automatiquement les demandes, ou cette tâche est-elle partagée avec le biologiste ? *(02_acteurs_du_domaine.md mentionne une validation par le biologiste.)*
- **Émission des recommandations** : Le SIL peut-il émettre des recommandations thérapeutiques automatiques, ou cette tâche est-elle exclusive au biologiste ? *(03_concepts_metier_initiaux.md mentionne une "aide à la décision", mais les limites ne sont pas précisées.)*

**Décisions clés** :
- Classer une demande en urgence absolue, haute, ou basse.
- Bloquer l’analyse si un tube est non conforme.
- Alerter les acteurs en cas de non-conformité ou de retard.

**Informations manipulées** :
- Prescriptions électroniques.
- Données contextuelles (type d’AOD, posologie, heure de la dernière prise, fonction rénale, contexte clinique).
- Résultats bruts et interprétés.
- Logs d’audit (audit trail).
- Alertes de non-conformité ou de retard.

**Interactions majeures** :
| Acteur | Type d'interaction | Enjeu |
|--------|--------------------|-------|
| **Cliniciens** | Prescription électronique, saisie des données contextuelles. | Rapidité et exhaustivité des données. |
| **Biologistes** | Validation des résultats, interprétation. | Traçabilité et sécurité. |
| **Techniciens de laboratoire** | Saisie des résultats, gestion des échantillons. | Fiabilité des données. |
| **DPI** | Échanges de données patients (fonction rénale, traitements). | Cohérence des informations. |
| **Analyseurs** | Transmission automatique des résultats bruts. | Intégration des données analytiques. |
| **Middleware** | Gestion des flux d’échantillons. | Optimisation des délais. |

**Points à clarifier** :
1. **Règles de priorisation** : Quelles sont les règles métiers exactes pour classer une demande en urgence absolue, haute, ou basse ? *(03_concepts_metier_initiaux.md mentionne une "grille de priorisation", mais elle n’est pas détaillée.)*
2. **Intégration avec le DPI** : Quelles données du DPI sont nécessaires au SIL, et comment sont-elles échangées ? *(05_vision_globale_du_domaine.md mentionne une intégration nécessaire.)*
3. **Sécurité des données** : Quels mécanismes d’authentification et de chiffrement sont déjà en place, et lesquels doivent être ajoutés ? *(04_contraintes_et_risques.md souligne l’importance de la sécurité.)*

---
### 4.2. Dossier Patient Informatisé (DPI)
**Rôle métier** :
- Stocker les **données médicales** du patient, incluant les traitements en cours et les résultats d’examens.

**Responsabilités principales** :
| Responsabilité | Détail | Source |
|----------------|--------|--------|
| Stockage des données | Conserver les données patients (fonction rénale, traitements, antécédents). | 02_acteurs_du_domaine.md |
| Partage des données | Fournir les données pertinentes au SIL pour l’interprétation des résultats. | 05_vision_globale_du_domaine.md |
| Sécurité des données | Garantir la confidentialité et l’intégrité des données. | 04_contraintes_et_risques.md |

**Interactions majeures** :
| Acteur | Type d'interaction | Enjeu |
|--------|--------------------|-------|
| **SIL** | Échanges de données patients (fonction rénale, traitements). | Cohérence des informations. |
| **Cliniciens** | Consultation et mise à jour des données. | Prise de décision éclairée. |

**Points à clarifier** :
1. **Données à partager** : Quelles données du DPI sont nécessaires au SIL pour l’interprétation des dosages anti-Xa ? *(03_concepts_metier_initiaux.md liste les données contextuelles, mais leur disponibilité dans le DPI n’est pas précisée.)*
2. **Format des données** : Quel est le format des données échangées entre le DPI et le SIL ? *(05_vision_globale_du_domaine.md mentionne une interopérabilité nécessaire.)*

---
### 4.3. Analyseurs de laboratoire
**Rôle métier** :
- Réaliser le **dosage anti-Xa** sur les échantillons biologiques.

**Responsabilités principales** :
| Responsabilité | Détail | Source |
|----------------|--------|--------|
| Réalisation de l’analyse | Effectuer le dosage anti-Xa avec précision. | 02_acteurs_du_domaine.md |
| Contrôle qualité | Respecter les procédures analytiques et les contrôles qualité. | 02_acteurs_du_domaine.md |
| Transmission des résultats | Envoyer les résultats bruts au SIL (automatiquement ou manuellement). | 02_acteurs_du_domaine.md |

**Interactions majeures** :
| Acteur | Type d'interaction | Enjeu |
|--------|--------------------|-------|
| **SIL** | Transmission automatique des résultats bruts. | Intégration des données analytiques. |
| **Techniciens de laboratoire** | Supervision des analyses. | Fiabilité des résultats. |

**Points à clarifier** :
1. **Intégration avec le SIL** : Les résultats sont-ils transmis automatiquement au SIL, ou la saisie est-elle manuelle ? *(05_vision_globale_du_domaine.md mentionne une intégration nécessaire.)*
2. **Modèles d’analyseurs** : Quels sont les modèles d’analyseurs utilisés (ex. : ACL TOP, STA R Max), et sont-ils compatibles avec le SIL ? *(02_acteurs_du_domaine.md mentionne des exemples, mais la compatibilité n’est pas précisée.)*

---
### 4.4. Middleware de laboratoire
**Rôle métier** :
- Gérer les **flux d’échantillons** entre les services et le laboratoire.
- Automatiser la **vérification des conformités pré-analytiques**.

**Responsabilités principales** :
| Responsabilité | Détail | Source |
|----------------|--------|--------|
| Routage des échantillons | Diriger les tubes vers les analyseurs appropriés. | 02_acteurs_du_domaine.md |
| Vérification des conformités | Contrôler le type de tube, le volume et le délai de transport. | 04_contraintes_et_risques.md |
| Transmission des résultats | Envoyer les résultats au SIL. | 02_acteurs_du_domaine.md |

**Interactions majeures** :
| Acteur | Type d'interaction | Enjeu |
|--------|--------------------|-------|
| **SIL** | Transmission des résultats et des statuts des échantillons. | Traçabilité et rapidité. |
| **Techniciens de laboratoire** | Supervision des flux. | Optimisation des délais. |

**Points à clarifier** :
1. **Fonctionnalités du middleware** : Quelles fonctionnalités sont déjà implémentées (ex. : vérification des conformités), et lesquelles doivent être ajoutées ? *(02_acteurs_du_domaine.md mentionne un rôle de gestion des flux.)*
2. **Compatibilité avec le SIL** : Le middleware est-il compatible avec le SIL actuel, ou des adaptations sont-elles nécessaires ? *(05_vision_globale_du_domaine.md mentionne une intégration nécessaire.)*

---
### 4.5. Systèmes d'alerte et de priorisation
**Rôle métier** :
- Classer les **demandes** en fonction de leur urgence clinique.
- Envoyer des **alertes** aux biologistes et aux cliniciens en cas de criticité.

**Responsabilités principales** :
| Responsabilité | Détail | Source |
|----------------|--------|--------|
| Priorisation automatique | Appliquer des règles métiers pour classer les demandes. | 03_concepts_metier_initiaux.md |
| Envoi d’alertes | Notifier les acteurs en cas de non-conformité ou de retard. | 04_contraintes_et_risques.md |

**Interactions majeures** :
| Acteur | Type d'interaction | Enjeu |
|--------|--------------------|-------|
| **SIL** | Intégration des règles de priorisation. | Automatisation du circuit. |
| **Biologistes** | Notification des demandes urgentes. | Réactivité. |
| **Cliniciens** | Alerte en cas de non-conformité. | Correction rapide. |

**Points à clarifier** :
1. **Règles de priorisation** : Quelles sont les règles métiers exactes pour classer une demande en urgence absolue, haute, ou basse ? *(03_concepts_metier_initiaux.md mentionne une "grille de priorisation", mais elle n’est pas détaillée.)*
2. **Canaux d’alerte** : Quels canaux sont utilisés pour envoyer les alertes (ex. : messagerie sécurisée, SMS, notification dans le SIL) ? *(04_contraintes_et_risques.md souligne l’importance des alertes.)*

---
### 4.6. Autorités réglementaires (HAS, ANSM, ARS, CNIL)
**Rôle métier** :
- Vérifier la **conformité** du circuit avec les bonnes pratiques et les normes.

**Responsabilités principales** :
| Responsabilité | Détail | Source |
|----------------|--------|--------|
| Audit des processus | Vérifier le respect des normes (ISO 15189, RGPD). | 04_contraintes_et_risques.md |
| Sanction en cas de non-conformité | Appliquer des mesures correctives ou des sanctions. | 04_contraintes_et_risques.md |

**Interactions majeures** :
| Acteur | Type d'interaction | Enjeu |
|--------|--------------------|-------|
| **Laboratoire** | Réalisation des audits. | Conformité réglementaire. |
| **Direction de l’établissement** | Rapport des non-conformités. | Prise de décision stratégique. |

**Points à clarifier** :
1. **Normes applicables** : Quelles sont les normes exactes à respecter (ex. : ISO 15189, RGPD, recommandations HAS/ANSM) ? *(04_contraintes_et_risques.md liste les normes, mais une priorisation serait utile.)*
2. **Durée de conservation des données** : Quelle est la durée minimale de conservation des logs d’audit ? *(03_concepts_metier_initiaux.md mentionne une conservation de 10 ans, mais la source n’est pas précisée.)*

---
### 4.7. Équipe informatique (DSI)
**Rôle métier** :
- Maintenir et faire évoluer le **SIL** pour répondre aux besoins du circuit.
- Garantir la **sécurité** et la **disponibilité** du système.

**Responsabilités principales** :
| Responsabilité | Détail | Source |
|----------------|--------|--------|
| Maintenance du SIL | Assurer la disponibilité 24/7 du système. | 02_acteurs_du_domaine.md |
| Évolution fonctionnelle | Implémenter les nouvelles fonctionnalités (priorisation, traçabilité). | 02_acteurs_du_domaine.md |
| Sécurité des données | Mettre en place des mécanismes d’authentification et de chiffrement. | 04_contraintes_et_risques.md |
| Formation des utilisateurs | Organiser des sessions de formation sur le nouveau circuit. | 02_acteurs_du_domaine.md |

**Interactions majeures** :
| Acteur | Type d'interaction | Enjeu |
|--------|--------------------|-------|
| **Comité de pilotage** | Suivi technique et budgétaire. | Réussite du projet. |
| **Biologistes et cliniciens** | Recueil des besoins fonctionnels. | Adéquation avec les attentes métier. |
| **Fournisseurs d’équipements** | Intégration des analyseurs. | Compatibilité technique. |

**Points à clarifier** :
1. **Compatibilité du SIL actuel** : Le SIL actuel permet-il une telle évolution, ou un remplacement est-il nécessaire ? *(01_reformulation_du_besoin.md mentionne un "SIL actuel" sans préciser ses capacités.)*
2. **Exigences techniques** : Quelles sont les exigences techniques pour le nouveau circuit (ex. : disponibilité 24/7, interopérabilité avec le DPI) ? *(04_contraintes_et_risques.md souligne l’importance de la disponibilité et de la sécurité.)*

---
## 5. Synthèse des interactions clés

| **Acteur A**               | **Acteur B**               | **Type d'interaction**                     | **Enjeu**                                  | **Source** |
|----------------------------|----------------------------|--------------------------------------------|--------------------------------------------|------------|
| **Cliniciens**             | **SIL**                    | Prescription électronique, saisie des données contextuelles. | Rapidité et exhaustivité des données. | 02_acteurs_du_domaine.md |
| **Cliniciens**             | **Laboratoire**            | Transmission des échantillons et des demandes. | Respect des délais et conformité des tubes. | 02_acteurs_du_domaine.md |
| **Biologistes**            | **SIL**                    | Validation des résultats, interprétation. | Traçabilité et sécurité des données. | 02_acteurs_du_domaine.md |
| **Techniciens de laboratoire** | **SIL**                | Saisie des résultats. | Fiabilité des données. | 02_acteurs_du_domaine.md |
| **SIL**                    | **DPI**                    | Échanges de données (fonction rénale, traitements). | Cohérence des informations. | 05_vision_globale_du_domaine.md |
| **SIL**                    | **Analyseurs**             | Transmission des résultats bruts. | Intégration des données analytiques. | 02_acteurs_du_domaine.md |
| **CAI**                    | **Cliniciens/Biologistes** | Mise à jour des protocoles. | Adaptation aux bonnes pratiques. | 02_acteurs_du_domaine.md |
| **DSI**                    | **SIL**                    | Maintenance et évolution du système. | Disponibilité et sécurité du SIL. | 02_acteurs_du_domaine.md |
| **Patient**                | **Cliniciens/SIL**         | Accès aux résultats et consentement. | Transparence et information du patient. | 02_acteurs_du_domaine.md |
| **Systèmes d'alerte**      | **Biologistes/Cliniciens** | Envoi d’alertes en cas de criticité. | Réactivité et sécurité. | 04_contraintes_et_risques.md |

---
## 6. Responsabilités partagées ou ambiguës

### 6.1. Responsabilités partagées
| **Responsabilité** | **Acteurs impliqués** | **Détail** | **Source** |
|--------------------|-----------------------|------------|------------|
| **Gestion des non-conformités des tubes** | Cliniciens, Techniciens de laboratoire, Biologistes | Le clinicien vérifie la conformité avant envoi, le technicien valide avant analyse, et le biologiste peut rejeter l’échantillon si nécessaire. | 02_acteurs_du_domaine.md, 04_contraintes_et_risques.md |
| **Priorisation des demandes** | SIL, Biologistes | Le SIL classe automatiquement les demandes, mais le biologiste peut ajuster manuellement l’ordre en cas de conflit. | 03_concepts_metier_initiaux.md, 05_vision_globale_du_domaine.md |
| **Interprétation des résultats** | Biologistes, Pharmaciens | Le biologiste interprète le résultat et émet des recommandations, mais le pharmacien peut valider ou contester ces recommandations. | 02_acteurs_du_domaine.md |
| **Adaptation du traitement** | Cliniciens, Pharmaciens, Biologistes | Le clinicien adapte le traitement en fonction des résultats et des recommandations, avec l’aide du pharmacien et du biologiste. | 02_acteurs_du_domaine.md |

### 6.2. Ambiguïtés à lever
| **Ambiguïté** | **Acteurs concernés** | **Question à clarifier** | **Source** |
|---------------|-----------------------|--------------------------|------------|
| **Validation des tubes** | Cliniciens, Techniciens de laboratoire, Biologistes | Qui valide définitivement la conformité d’un tube ? Le clinicien, le technicien, ou le biologiste ? | 02_acteurs_du_domaine.md |
| **Priorisation automatique vs. manuelle** | SIL, Biologistes | La priorisation est-elle entièrement automatisée, ou le biologiste peut-il ajuster manuellement l’ordre des analyses ? | 03_concepts_metier_initiaux.md, 05_vision_globale_du_domaine.md |
| **Émission des recommandations** | Biologistes, Pharmaciens | Les recommandations du biologiste sont-elles systématiquement validées par le pharmacien, ou cette tâche est-elle partagée ? | 02_acteurs_du_domaine.md |
| **Gestion des astreintes** | Biologistes, Personnel administratif | Qui coordonne les prélèvements et valide les résultats en dehors des heures ouvrables ? | 04_contraintes_et_risques.md |
| **Portail patient** | Patients, Cliniciens, SIL | Un portail patient sera-t-il mis en place pour accéder aux résultats ? Si oui, quelles données seront accessibles ? | 02_acteurs_du_domaine.md |

---
## 7. Points à clarifier avec les experts métier

### 7.1. Exigences pré-analytiques
1. **Critères de conformité des tubes** :
   - Quel est le **type de tube exact** requis (ex. : tube citraté 3.2%) ?
   - Quel est le **volume minimal** requis ?
   - Quel est le **délai maximal** entre prélèvement et analyse ?
   - Quelles sont les **conditions de transport** (température, protection de la lumière) ?

2. **Procédure de gestion des non-conformités** :
   - Que faire en cas de non-conformité des tubes ? (Refus systématique, demande de complément, escalade ?)
   - Qui valide la conformité des tubes ? (Clinicien, technicien, biologiste, système automatisé ?)

### 7.2. Critères de priorisation
1. **Grille de priorisation** :
   - Quels sont les **critères exacts** pour classer une demande en "urgence absolue", "haute", ou "basse" ?
   - Quels sont les **délais maximaux** acceptables pour chaque niveau de priorité ?
   - Exemples :
     - Hémorragie active → urgence absolue (délai : 1 heure).
     - Chirurgie programmée → priorité haute (délai : 4 heures).
     - Contrôle systématique → priorité basse (délai : 24 heures).

2. **Règles d'escalade** :
   - Que faire en cas de **conflit de priorités** ? (Ex. : deux demandes en urgence absolue ?)

### 7.3. Données contextuelles
1. **Liste exhaustive des données à collecter** :
   - Type d’AOD (apixaban, rivaroxaban, édoxaban, etc.).
   - Posologie (dose et fréquence).
   - Heure de la dernière prise (précision requise : minutes/heures ?).
   - Fonction rénale (clairance de la créatinine, formule utilisée : CKD-EPI ou MDRD ?).
   - Contexte clinique (hémorragie active, chirurgie programmée, etc.).
   - Autres traitements (antiagrégants, autres anticoagulants).

2. **Méthode de saisie** :
   - Les données sont-elles saisies **manuellement** ou récupérées **automatiquement** depuis le DPI ?
   - Quels **champs sont obligatoires** ?
   - Y a-t-il un **formatage automatique** (ex. : heure de la dernière prise au format HH:MM) ?

### 7.4. Rôles et responsabilités
1. **Validation des demandes** :
   - Qui valide les demandes ? (Biologiste, technicien, système automatisé ?)

2. **Accès aux résultats** :
   - Qui a accès aux résultats et dans quelles conditions ? (Cliniciens, pharmaciens, patient ?)

3. **Recommandations thérapeutiques** :
   - Qui émet les recommandations ? (Biologiste, pharmacien, système automatisé ?)
   - Qui valide les recommandations ? (Pharmacien, clinicien ?)

### 7.5. Intégration avec les systèmes existants
1. **Compatibilité du SIL** :
   - Le SIL actuel permet-il une telle évolution ?
   - Existe-t-il des **API ou connecteurs** pour échanger des données avec le DPI, les analyseurs, ou le middleware ?

2. **Interfaces dédiées** :
   - Faut-il prévoir une **interface spécifique** pour les cliniciens ?

### 7.6. Gestion des exceptions
1. **Hors heures ouvrables** :
   - Quels sont les **services couverts** par l’astreinte ?
   - Quelle est la **procédure de déclenchement** de l’astreinte ?

2. **Demandes non conformes** :
   - Que faire en cas de non-conformité des tubes ? (Refus, demande de complément, escalade ?)

### 7.7. Exigences réglementaires
1. **Normes à respecter** :
   - Quelles sont les **normes exactes** à respecter (ex. : ISO 15189, RGPD, recommandations HAS/ANSM) ?
   - Quelle est la **durée de conservation** des logs d’audit ?

2. **Signature électronique** :
   - Faut-il prévoir une **signature électronique** pour les résultats validés ?

### 7.8. Retours d'expérience
1. **Analyse des dysfonctionnements actuels** :
   - Quels sont les **principaux irritants** du circuit actuel ?
   - Quelles sont les **causes racines** des retards ou des erreurs ?

2. **Bonnes pratiques** :
   - Existe-t-il des **retours d’expérience** d’autres établissements ayant mis en place un circuit similaire ?

### 7.9. Attentes des utilisateurs
1. **Cliniciens** :
   - Quelles **fonctionnalités** attendent-ils du futur SIL ? (Ex. : priorisation automatique, intégration des données contextuelles.)

2. **Biologistes** :
   - Quels **outils d’aide à la décision** souhaitent-ils ? (Ex. : grilles d’interprétation, seuils d’alerte.)

3. **Techniciens de laboratoire** :
   - Quels **modules de vérification automatique** des conformités souhaitent-ils ?

### 7.10. Budget et planning
1. **Budget alloué** :
   - Quel est le **budget disponible** pour le projet ?

2. **Planning** :
   - Quels sont les **délais impartis** pour la mise en place du nouveau circuit ?

---
## 8. Conclusion
Cette cartographie met en évidence :
- La **complexité du circuit** des demandes urgentes de dosage anti-Xa, impliquant de multiples acteurs aux rôles et responsabilités variés.
- Les **points de friction** actuels (non-conformité des tubes, absence de priorisation automatique, traçabilité insuffisante).
- Les **ambiguïtés** à lever avec les experts métier pour concevoir un circuit informatisé sécurisé, tracé et priorisé.

**Prochaine étape** : Valider les points à clarifier avec les experts métier, puis passer à l’étape 3 de la démarche DDD (modélisation comportementale).
```