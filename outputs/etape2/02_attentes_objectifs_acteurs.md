```markdown
# Attentes et objectifs des acteurs
**Domaine métier** : Gestion des demandes urgentes de dosage anti-Xa dans le SIL
**Date** : [À compléter]
**Version** : 1.0
**Auteurs** : Analyste Métier
**Sources** : Livrables étape 1 (01_reformulation_du_besoin.md, 02_acteurs_du_domaine.md, 03_concepts_metier_initiaux.md, 04_contraintes_et_risques.md, 05_vision_globale_du_domaine.md)

---

## 1. Introduction
Ce document analyse les **attentes, objectifs, motivations et contraintes** de chaque acteur impliqué dans le domaine des **demandes urgentes de dosage anti-Xa**, en mettant en lumière :
- Ce que chaque acteur cherche à **obtenir, éviter ou sécuriser**.
- Les **critères de réussite métier** perçus.
- Les **irritants** ou difficultés rencontrées.
- Les **divergences d’intérêts** potentielles entre acteurs.

Il s’appuie sur les livrables de l’étape 1 et synthétise les enjeux stratégiques, opérationnels et réglementaires pour chaque partie prenante.

---

## 2. Attentes et objectifs par acteur

### 2.1. Cliniciens prescripteurs
**Services concernés** :
- Urgences
- Réanimation
- Bloc opératoire
- Services extérieurs (cardiologie, médecine interne)

---

#### **Objectifs principaux**
| **Objectif** | **Détail** | **Source** |
|--------------|------------|------------|
| **Prise en charge thérapeutique optimale** | Adapter rapidement le traitement anticoagulant en fonction des résultats du dosage anti-Xa. | 01_reformulation_du_besoin.md, 02_acteurs_du_domaine.md |
| **Réduction des délais critiques** | Obtenir les résultats du dosage anti-Xa dans les délais impartis pour éviter les complications (ex. : hémorragie active). | 01_reformulation_du_besoin.md, 04_contraintes_et_risques.md |
| **Fiabilité des données** | S’assurer que les données saisies (type d’AOD, posologie, heure de la dernière prise) sont exactes et complètes. | 03_concepts_metier_initiaux.md, 04_contraintes_et_risques.md |
| **Conformité aux protocoles** | Respecter les indications de dosage anti-Xa selon les recommandations HAS/ANSM et les protocoles locaux. | 02_acteurs_du_domaine.md |
| **Collaboration pluridisciplinaire** | Faciliter la communication avec les biologistes et les pharmaciens pour une prise en charge coordonnée. | 02_acteurs_du_domaine.md |

---

#### **Attentes explicites**
| **Attente** | **Détail** | **Critère de réussite** | **Source** |
|-------------|------------|-------------------------|------------|
| **Automatisation de la priorisation** | Le SIL doit classer automatiquement les demandes par niveau d’urgence pour éviter les erreurs de tri manuel. | Délai de traitement des demandes urgentes respecté (ex. : 1h pour une hémorragie active). | 05_vision_globale_du_domaine.md |
| **Intégration des données contextuelles** | Récupérer automatiquement les données depuis le DPI (fonction rénale, traitements en cours) pour éviter les erreurs de saisie. | Données complètes et exactes à 100% pour l’interprétation. | 03_concepts_metier_initiaux.md |
| **Feedback en temps réel** | Recevoir des alertes automatiques en cas de non-conformité des tubes ou de retard dans le traitement. | Réduction des rejets d’échantillons à moins de 5%. | 04_contraintes_et_risques.md |
| **Accès simplifié aux résultats** | Visualiser rapidement les résultats et les recommandations thérapeutiques via le SIL. | Temps de consultation des résultats < 2 minutes. | 02_acteurs_du_domaine.md |
| **Portail patient** | Permettre aux patients d’accéder à leurs résultats pour améliorer l’adhésion au traitement. | Satisfaction patient > 90% (enquête post-consultation). | 02_acteurs_du_domaine.md |

---

#### **Attentes implicites**
| **Attente** | **Détail** | **Risque si non satisfait** | **Source** |
|-------------|------------|-----------------------------|------------|
| **Réduction de la charge administrative** | Éviter de saisir manuellement les données contextuelles (ex. : heure de la dernière prise). | Surcharge de travail → erreurs de saisie ou omission de données critiques. | 05_vision_globale_du_domaine.md |
| **Transparence sur les délais** | Connaître en temps réel le statut de la demande (en attente, en cours, terminée). | Anxiété des cliniciens et des patients en cas d’attente prolongée. | 04_contraintes_et_risques.md |
| **Formation adaptée** | Bénéficier de formations ciblées sur l’utilisation du nouveau circuit. | Mauvaise utilisation du SIL → erreurs de prescription ou d’interprétation. | 02_acteurs_du_domaine.md |
| **Sécurité des données** | Garantir que les données patients sont protégées contre les accès non autorisés. | Violation du RGPD → sanctions légales et perte de confiance. | 04_cont