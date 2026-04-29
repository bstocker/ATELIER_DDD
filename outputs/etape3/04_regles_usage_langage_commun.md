# **Règles d'usage du langage commun**
**Domaine** : Gestion des demandes urgentes de dosage anti-Xa dans le SIL
**Version** : 1.0
**Date** : [À compléter]
**Auteurs** : Analyste DDD
**Sources** : Livrables étapes 1 et 2 (01_reformulation_du_besoin.md, 02_acteurs_du_domaine.md, 03_concepts_metier_initiaux.md, 04_contraintes_et_risques.md, 05_vision_globale_du_domaine.md, 01_cartographie_acteurs_responsabilites.md, 02_attentes_objectifs_acteurs.md, 03_decisions_informations_manipulees.md, 04_regles_metier.md, 05_priorites_exceptions_contraintes.md, 06_conflits_objectifs_arbitrages.md, 07_base_modelisation_comportementale.md)

---

## **1. Introduction**
Ce document définit les **règles d'usage du langage commun** pour le domaine des **demandes urgentes de dosage anti-Xa** dans le SIL. Il vise à :
- **Standardiser l'utilisation des termes validés** dans tous les artefacts du projet (ateliers, documentation, user stories, tests, code).
- **Éviter les ambiguïtés** et les malentendus entre parties prenantes.
- **Garantir la cohérence** du vocabulaire métier tout au long du projet.
- **Faciliter la maintenance** du glossaire et son adoption par les équipes.

Ces règles s'appliquent à **tous les livrables** du projet et doivent être respectées par :
- Les **experts métier** (cliniciens, biologistes, pharmaciens).
- Les **analystes métier** et **PO**.
- Les **développeurs** et **testeurs**.
- Les **DSI** et **équipes techniques**.

---

---

## **2. Conventions de nommage des concepts métier**

### **2.1. Règles générales de nommage**

| **Règle** | **Description** | **Exemple** | **Justification** |
|------------|-----------------|-------------|-------------------|
| **Utiliser des termes métier validés** | Toujours utiliser les termes définis dans le glossaire, sans modification ni traduction. | ✅ *"Prescription électronique"* au lieu de *"Ordonnance dématérialisée"* | Évite les malentendus entre vocabulaire métier et technique. |
| **Privilégier les sigles standardisés** | Utiliser les sigles validés (ex. : **SIL**, **DPI**, **AOD**, **CAI**). | ✅ *"Le SIL priorise automatiquement la demande"* <br> ❌ *"Le logiciel de laboratoire classe la demande"* | Les sigles sont plus concis et universellement compris dans le domaine. |
| **Éviter les termes techniques non validés** | Ne pas utiliser de termes techniques non définis dans le glossaire (ex. : *"API"*, *"middleware"*, *"backend"*). | ✅ *"Le SIL vérifie la conformité des tubes"* <br> ❌ *"Le backend valide les tubes"* | Le langage doit rester centré sur le métier, sans intrusion de jargon technique. |
| **Respecter la casse** | Utiliser la **majuscule initiale** pour les termes validés (ex. : **Clinicien prescripteur**, **Dosage anti-Xa**). | ✅ *"Le Clinicien prescripteur saisit le type d'AOD"* <br> ❌ *"le clinicien prescripteur saisit le type d'aod"* | Facilite la lecture et l'identification des termes clés. |
| **Utiliser le singulier** | Privilégier le singulier pour les concepts métier (ex. : **une Demande urgente**, **un Tube**). | ✅ *"Une Demande urgente est classée en priorité absolue"* <br> ❌ *"Les demandes urgentes sont classées en priorité absolue"* | Plus naturel en français et évite les confusions avec les pluriels techniques. |
| **Éviter les anglicismes** | Remplacer les termes anglais par leur équivalent français validé. | ✅ *"Système d'alerte"* au lieu de *"Alerting system"* <br> ✅ *"Traçabilité"* au lieu de *"Traceability"* | Le langage doit être naturel pour les experts métier. |
| **Utiliser des formulations actives** | Formuler les phrases avec un verbe d'action pour clarifier les responsabilités. | ✅ *"Le Biologiste médical valide la demande"* <br> ❌ *"La validation de la demande est effectuée par le biologiste"* | Plus direct et aligné avec les processus métier. |

---

### **2.2. Règles spécifiques par catégorie**

#### **2.2.1. Acteurs**

| **Catégorie** | **Règle** | **Exemple** | **Justification** |
|---------------|-----------|-------------|-------------------|
| **Acteurs humains** | Utiliser le terme validé suivi d'un article défini ou indéfini. | ✅ *"Le Clinicien prescripteur"* <br> ✅ *"Un Biologiste médical"* <br> ❌ *"Un médecin prescripteur"* (trop générique) | Précise le rôle métier et évite les confusions. |
| **Acteurs organisationnels** | Utiliser le nom complet de la commission ou du comité. | ✅ *"La Commission des Anti-infectieux et des Anticoagulants (CAI)"* <br> ✅ *"Le Comité de pilotage du projet SIL"* <br> ❌ *"La commission"* (trop vague) | Clarifie le rôle et l'autorité de chaque instance. |
| **Acteurs techniques** | Utiliser le terme validé avec une majuscule initiale. | ✅ *"Le Système d'Information de Laboratoire (SIL)"* <br> ✅ *"Le Middleware de laboratoire"* <br> ❌ *"le sil"* ou *"le middleware"* (trop technique) | Évite les confusions avec les outils techniques non validés. |

---

#### **2.2.2. Concepts métier**

| **Catégorie** | **Règle** | **Exemple** | **Justification** |
|---------------|-----------|-------------|-------------------|
| **Concepts centraux** | Utiliser le terme validé avec une majuscule initiale, suivi d'un article si nécessaire. | ✅ *"Une Demande urgente de dosage anti-Xa"* <br> ✅ *"Les Exigences pré-analytiques"* <br> ❌ *"une demande urgente"* (trop vague) | Assure la précision et l'unicité des termes. |
| **Informations manipulées** | Utiliser le terme validé avec une majuscule initiale, suivi d'un article. | ✅ *"Le Type d'AOD"* <br> ✅ *"La Heure de la dernière prise"* <br> ❌ *"le type d'aod"* ou *"l'heure de la dernière prise"* (trop technique) | Clarifie le rôle des données dans les processus. |
| **Décisions métier** | Formuler les décisions comme des verbes d'action suivis du sujet. | ✅ *"Le Clinicien prescripteur Valide la conformité des tubes"* <br> ✅ *"Le Biologiste médical Priorise une analyse"* <br> ❌ *"La validation des tubes est effectuée par le clinicien"* (passif) | Montre clairement qui fait quoi. |
| **Règles métier** | Formuler les règles comme des obligations ou des interdictions claires. | ✅ *"Toute Demande urgente doit être validée par un Biologiste médical"* <br> ✅ *"Le SIL doit vérifier automatiquement la conformité des tubes"* <br> ❌ *"On peut vérifier la conformité des tubes"* (trop vague) | Rend les règles explicites et actionnables. |
| **Événements** | Utiliser des verbes au présent ou au passé pour décrire les événements. | ✅ *"Le Prélèvement sanguin est réalisé dans un tube citraté 3.2%"* <br> ✅ *"La Transmission des résultats bruts est automatique"* <br> ❌ *"Il y a eu une transmission des résultats"* (trop passif) | Décrit les processus de manière dynamique. |
| **Contraintes** | Formuler les contraintes comme des obligations ou des limites claires. | ✅ *"Le SIL doit être disponible 24/7 pour les urgences"* <br> ✅ *"Les délais critiques doivent être respectés"* <br> ❌ *"Les délais sont importants"* (trop vague) | Rend les contraintes explicites et mesurables. |

---

---

## **3. Règles pour utiliser les termes retenus dans les échanges projet**

### **3.1. Dans les ateliers et réunions**

| **Règle** | **Description** | **Exemple** | **Justification** |
|------------|-----------------|-------------|-------------------|
| **Utiliser le vocabulaire validé** | Toujours utiliser les termes du glossaire dans les discussions. | ✅ *"Le Clinicien prescripteur doit saisir le Contexte clinique dans le SIL"* <br> ❌ *"Le médecin doit remplir le formulaire"* | Évite les malentendus et les traductions inutiles. |
| **Éviter les synonymes non validés** | Ne pas utiliser de termes alternatifs, même s'ils semblent équivalents. | ✅ *"La Priorisation des demandes est automatique"* <br> ❌ *"Le tri des demandes est automatique"* | Garantit la cohérence du langage. |
| **Clarifier les termes ambigus** | Si un terme n'est pas compris, demander une clarification plutôt que d'utiliser un synonyme. | ✅ *"Que signifie 'Exigences pré-analytiques' ?"* <br> ❌ *"C'est quoi les critères pour les tubes ?"* | Évite les interprétations erronées. |
| **Documenter les décisions** | Noter les termes validés dans les comptes-rendus d'atelier. | ✅ *"Dans l'atelier du 15/05, il a été décidé d'utiliser 'Prescription électronique' au lieu de 'Ordonnance dématérialisée'."* | Permet de tracer les choix terminologiques. |

---

### **3.2. Dans la documentation**

| **Règle** | **Description** | **Exemple** | **Justification** |
|------------|-----------------|-------------