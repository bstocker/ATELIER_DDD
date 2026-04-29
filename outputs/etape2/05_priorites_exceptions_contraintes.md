```markdown
# Priorités, exceptions et contraintes
**Domaine métier** : Gestion des demandes urgentes de dosage anti-Xa dans le SIL
**Date** : [À compléter]
**Version** : 1.0
**Auteurs** : Analyste Métier
**Sources** : Livrables étape 1 (01_reformulation_du_besoin.md, 02_acteurs_du_domaine.md, 03_concepts_metier_initiaux.md, 04_contraintes_et_risques.md, 05_vision_globale_du_domaine.md)

---

## 1. Introduction
Ce document identifie et formalise :
- Les **priorités métier** identifiées dans le circuit des demandes urgentes de dosage anti-Xa
- Les **exceptions et cas particuliers** à prendre en compte
- Les **contraintes temporelles, cliniques, pré-analytiques et organisationnelles**
- Les **contraintes réglementaires et de traçabilité**
- Les **risques associés** à chaque exception ou contrainte
- Les **arbitrages à clarifier** avec les experts métier

Il s'appuie sur les livrables de l'étape 1 et met en lumière les **enjeux critiques** pour la conception du futur système.

---

## 2. Priorités métier identifiées

### 2.1. Priorités de traitement des demandes

| **Niveau de priorité** | **Critères d'attribution** | **Délai maximal acceptable** | **Acteurs concernés** | **Conséquences en cas de non-respect** | **Source** |
|------------------------|---------------------------|-----------------------------|-----------------------|----------------------------------------|------------|
| **Urgence absolue** | - Hémorragie active non contrôlée <br> - Suspicion de surdosage avec signes cliniques graves <br> - Chirurgie en urgence vitale sous AOD | ≤ 1 heure | Cliniciens, Biologistes, SIL, Techniciens de laboratoire | Aggravation de l'état clinique, décès, complications thrombotiques ou hémorragiques | 01_reformulation_du_besoin.md, 04_contraintes_et_risques.md |
| **Urgence haute** | - Chirurgie programmée sous AOD <br> - Contrôle post-opératoire immédiat <br> - Suspicion de surdosage sans signes cliniques graves | ≤ 4 heures | Cliniciens, Biologistes, SIL | Retard dans l'adaptation thérapeutique, complications post-opératoires | 01_reformulation_du_besoin.md, 05_vision_globale_du_domaine.md |
| **Urgence modérée** | - Contrôle systématique sous AOD <br> - Bilan pré-opératoire non urgent <br> - Suivi de traitement | ≤ 24 heures | Cliniciens, Biologistes, SIL | Retard dans la prise en charge, mais pas de risque vital immédiat | 03_concepts_metier_initiaux.md |
| **Routine** | - Contrôle de routine sous AOD <br> - Bilan de suivi | ≤ 48 heures | Cliniciens, Biologistes | Aucun risque vital, mais impact sur la planification des ressources | Hypothèse basée sur les bonnes pratiques |

---

### 2.2. Priorités de traitement des échantillons

| **Critère de priorité** | **Niveau de priorité** | **Acteurs concernés** | **Actions associées** | **Source** |
|-------------------------|------------------------|-----------------------|-----------------------|------------|
| **Type d'AOD** | Urgence absolue pour : apixaban, rivaroxaban, édoxaban | Biologistes, Techniciens de laboratoire | Traitement immédiat de l'échantillon | 03_concepts_metier_initiaux.md |
| **Fonction rénale** | Urgence absolue si clairance < 30 mL/min | Biologistes | Interprétation rapide avec adaptation posologique | Hypothèse basée sur les recommandations HAS/ANSM |
| **Contexte clinique** | Urgence absolue si : <br> - Hémorragie active <br> - Suspicion de surdosage <br> - Chirurgie en urgence | Cliniciens, Biologistes | Transmission immédiate des résultats | 02_acteurs_du_domaine.md |
| **Heure de la dernière prise** | Urgence absolue si : <br> - Prise < 6h pour apixaban/rivaroxaban <br> - Prise < 12h pour édoxaban | Biologistes | Interprétation avec prise en compte du délai | 03_concepts_metier_initiaux.md |

---

## 3. Exceptions et cas particuliers

### 3.1. Exceptions cliniques

| **Cas particulier** | **Description** | **Niveau de priorité** | **Acteurs concernés** | **Actions spécifiques** | **Risques associés** | **Source** |
|--------------------|-----------------|------------------------|-----------------------|------------------------|----------------------|------------|
| **Hémorragie active sous AOD** | Patient présentant un saignement actif nécessitant une adaptation immédiate du traitement | Urgence absolue | Cliniciens, Biologistes, Pharmaciens | - Administration immédiate d'antidote si disponible <br> - Adaptation posologique <br> - Surveillance renforcée | Décès, séquelles permanentes, complications thrombotiques | 01_reformulation_du_besoin.md, 04_contraintes_et_risques.md |
| **Suspicion de surdosage sans hémorragie** | Patient asymptomatique mais avec résultat de dosage anti-Xa anormalement élevé | Urgence haute | Biologistes, Cliniciens | - Vérification du résultat <br> - Adaptation posologique <br> - Surveillance clinique | Risque de surdosage → hémorragie retardée | 03_concepts_metier_initiaux.md |
| **Insuffisance rénale aiguë** | Patient avec clairance de la créatinine < 30 mL/min | Urgence absolue | Biologistes, Cliniciens | - Adaptation posologique immédiate <br> - Surveillance renforcée | Risque de surdosage → hémorragie | Hypothèse basée sur les recommandations HAS/ANSM |
| **Patient sous plusieurs anticoagulants** | Patient sous AOD + antiagrégant plaquettaire ou autre anticoagulant | Urgence haute | Cliniciens, Pharmaciens, Biologistes | - Évaluation du risque hémorragique <br> - Adaptation posologique | Risque accru d'hémorragie | 02_acteurs_du_domaine.md |
| **Grossesse ou allaitement** | Patient sous AOD en situation de grossesse ou d'allaitement | Urgence haute | Cliniciens, Biologistes | - Adaptation du traitement <br> - Surveillance spécifique | Risque tératogène, complications hémorragiques | Hypothèse clinique |
| **Patient en pédiatrie** | Patient pédiatrique sous AOD | Urgence haute | Cliniciens pédiatriques, Biologistes | - Adaptation posologique spécifique <br> - Surveillance renforcée | Risque de surdosage ou sous-dosage | Hypothèse basée sur les bonnes pratiques pédiatriques |
| **Patient en gériatrie** | Patient âgé (> 75 ans) sous AOD | Urgence modérée à haute | Cliniciens gériatres, Biologistes | - Adaptation posologique <br> - Surveillance renforcée | Risque accru d'effets indésirables | Hypothèse basée sur les recommandations gériatriques |

---

### 3.2. Exceptions pré-analytiques

| **Cas particulier** | **Description** | **Impact sur le circuit** | **Acteurs concernés** | **Actions spécifiques** | **Risques associés** | **Source** |
|--------------------|-----------------|---------------------------|-----------------------|------------------------|----------------------|------------|
| **Tube non conforme** | Tube citraté incorrect, volume insuffisant, délai de transport dépassé | Rejet de l'échantillon, demande de complément | Techniciens de laboratoire, Cliniciens | - Signalement immédiat au prescripteur <br> - Demande de nouveau prélèvement <br> - Archivage de l'échantillon non conforme | Retard dans la prise en charge, perte de temps pour le laboratoire | 04_contraintes_et_risques.md |
| **Échantillon hémolysé** | Échantillon présentant une hémolyse visible | Rejet de l'échantillon, risque de résultat erroné | Techniciens de laboratoire | - Signalement au biologiste <br> - Demande de nouveau prélèvement <br> - Archivage de l'échantillon | Résultat ininterprétable → erreur d'interprétation | Hypothèse basée sur les bonnes pratiques de laboratoire |
| **Délai de transport dépassé** | Délai > 4 heures entre prélèvement et analyse | Rejet de l'échantillon, risque de dégradation du résultat | Techniciens de laboratoire, SIL | - Signalement au prescripteur <br> - Demande de nouveau prélèvement <br> - Archivage de l'échantillon | Résultat ininterprétable → erreur d'interprétation | 04_contraintes_et_risques.md |
| **Température de transport incorrecte** | Transport à température non conforme (< 15°C ou > 25°C) | Risque de dégradation de l'échantillon | Personnel administratif, Techniciens de laboratoire | - Signalement au prescripteur <br> - Demande de nouveau prélèvement <br> - Archivage de l'échantillon | Résultat ininterprétable → erreur d'interprétation | Hypothèse basée sur les bonnes pratiques pré-analytiques |

---

### 3.3. Exceptions organisationnelles

| **Cas particulier** | **Description** | **Impact sur le circuit** | **Acteurs concernés** | **Actions spécifiques** | **Risques associés** | **Source** |
|--------------------|-----------------|---------------------------|-----------------------|------------------------|----------------------|------------|
| **Hors heures ouvrables** | Demande urgente en dehors des heures de bureau (nuit, week-end, jours fériés) | Gestion par astreinte biologique | Biologistes d'astreinte, SIL | - Accès sécurisé aux données patients <br> - Validation des résultats <br> - Transmission des recommandations | Retard dans la prise en charge, perte de contexte clinique | 04_cont