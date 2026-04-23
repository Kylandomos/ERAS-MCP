# Dossier de lancement — MCP OpenCities Map 2025 + Érâs MDB

## 1. Objet du document

Ce document sert de base de travail à transmettre à Codex pour lancer le développement d'un **MCP local Windows** capable de :

- scanner un poste Windows existant où **OpenCities Map 2025** et **Érâs** sont déjà installés et utilisés ;
- inventorier les dépendances, fichiers, configurations, scripts, données et points d’intégration ;
- analyser une ou plusieurs bases **MDB Access** utilisées par Érâs ;
- identifier la surface d’automatisation réellement disponible côté **OpenCities Map / MicroStation** ;
- produire les premiers livrables d’architecture, de PRD, de backlog et de plan de développement ;
- mettre en place un **serveur MCP** orchestrant l’environnement Bentley et la base métier Érâs.

Le développement doit partir du terrain réel : **le logiciel est déjà installé, déjà utilisé, et doit être compris avant toute implémentation intrusive**.

---

## 2. Contexte synthétique

### 2.1. Plateforme Bentley

Le poste cible utilise **OpenCities Map 2025** dans l’écosystème MicroStation. Le projet doit considérer comme point d’entrée prioritaire l’automatisation **MicroStation / OpenCities Map** côté poste Windows.

### 2.2. Plateforme Érâs

Érâs est traité comme une application métier reposant sur une **base Access (.mdb)** et une logique métier spécifique. Le projet doit considérer la **MDB comme un artefact central** à analyser, documenter et exploiter avec prudence.

### 2.3. Contrainte majeure

Le projet ne doit pas démarrer par des suppositions abstraites sur les APIs. Il doit d’abord produire une **cartographie factuelle** de l’environnement existant : logiciels, versions, chemins, scripts, fichiers, modules, données, exports, logs, configurations, schémas de tables et flux métier observables.

---

## 3. Résultat attendu du projet

À terme, le projet doit livrer un **MCP local Windows** permettant à un agent LLM de :

- interroger l’environnement OpenCities Map / MicroStation ;
- exécuter des opérations d’inspection et, plus tard, des opérations contrôlées d’automatisation ;
- interroger la base MDB d’Érâs ;
- produire des contrôles de cohérence entre dessin, objets, attributs et données métier ;
- générer des sorties de preuve, d’audit et de reporting ;
- préparer le terrain à des automatisations plus avancées.

Dans la première phase, l’objectif principal est **l’observabilité et la compréhension du système**. Les écritures et automatisations actives doivent être différées tant que l’inventaire et l’analyse n’ont pas été stabilisés.

---

## 4. Hypothèses de travail

1. Le poste cible est un **Windows** déjà opérationnel.
2. **OpenCities Map 2025** est installé et utilisé avec sa configuration réelle.
3. **Érâs** est installé et utilisé avec au moins une **MDB** active.
4. Il peut exister des fichiers de configuration, profils, macros, scripts, exports, tables auxiliaires, modèles, cellules, espaces de travail, logs ou docs internes déjà présents sur le poste.
5. Le projet doit partir de **copies de travail** et non manipuler les artefacts de production sans précaution.
6. Toute opération potentiellement destructive ou modifiant la base doit être explicitement isolée, tracée et désactivée par défaut.

---

## 5. Principes de sécurité et d’exploitation

### 5.1. Politique générale

- **Lecture seule par défaut**.
- Aucune écriture directe dans la MDB de production au début du projet.
- Aucune suppression, migration ou transformation non réversible pendant la phase de scan.
- Toute preuve collectée doit être horodatée et versionnée.
- Les chemins, mots de passe, secrets, clés, licences et données sensibles doivent être **redactés** dans les livrables destinés à être partagés.

### 5.2. Politique sur la MDB Érâs

- Toujours commencer par **copier** la MDB vers un espace de travail dédié.
- Produire une **empreinte** du fichier source et de la copie.
- Travailler sur une copie d’analyse.
- Journaliser tout accès.
- Interdire toute écriture automatique tant qu’un modèle de données minimal n’a pas été validé.

### 5.3. Politique sur OpenCities Map / MicroStation

- Distinguer clairement :
  - inspection de l’environnement ;
  - exécution de scripts de lecture ;
  - automatisations actives.
- Si des scripts sont exécutés, les limiter d’abord à des opérations **observables et non destructives**.
- Conserver toute sortie, log, capture et trace d’appel.

---

## 6. Périmètre de la phase 0 — Scan et cartographie du poste

La phase 0 est obligatoire. Aucun développement de logique métier avancée ne doit commencer avant sa complétion.

### 6.1. Objectifs de la phase 0

- Identifier l’architecture réelle du poste.
- Recenser les logiciels, composants, dépendances et chemins utiles.
- Cartographier l’emplacement des fichiers utiles au projet.
- Déterminer comment OpenCities Map est réellement exploité sur cette machine.
- Déterminer comment Érâs est réellement configuré sur cette machine.
- Produire un état de référence réutilisable pour la suite du développement.

### 6.2. Inventaire Windows à réaliser

Le scan doit couvrir au minimum :

- version Windows ;
- utilisateur courant et droits ;
- logiciels installés pertinents ;
- services et processus liés à Bentley / Érâs / Office Access ;
- variables d’environnement ;
- profils utilisateurs ;
- arborescences de travail principales ;
- clés de registre pertinentes ;
- raccourcis, scripts, fichiers batch, macros, tâches planifiées ;
- logs applicatifs détectables ;
- emplacements de cache, config et workspace.

### 6.3. Inventaire spécifique OpenCities Map / MicroStation

Le scan doit chercher au minimum :

- chemin d’installation ;
- version exacte ;
- workspace / workset utilisés ;
- répertoires de configuration ;
- présence de Python Manager / scripts Python / exemples ;
- macros, VBA, key-ins, scripts batch ;
- cellules, bibliothèques, schémas, modèles, catalogues ;
- fichiers DGN, seed files, préférences, configs ;
- plugins, extensions, modules additionnels ;
- tout indice d’automatisation existante déjà utilisée en interne.

### 6.4. Inventaire spécifique Érâs

Le scan doit chercher au minimum :

- chemin d’installation ;
- version exacte si détectable ;
- chemins vers les **MDB** ;
- fichiers de configuration ;
- exports Excel ou SIG ;
- modèles, palettes, thèmes, menus, objets personnalisés ;
- fichiers de paramétrage métier ;
- traces de calculs, états techniques, métrés ;
- docs locales éventuelles ;
- tout script ou outil externe qui interagit déjà avec Érâs.

### 6.5. Artefacts métiers à collecter

Le scan doit rechercher de manière systématique :

- `.mdb`
- `.accdb`
- `.dgn`
- `.rdl`
- `.xml`
- `.json`
- `.ini`
- `.cfg`
- `.bat`
- `.ps1`
- `.vbs`
- `.vba`
- `.py`
- `.xls` / `.xlsx`
- `.csv`
- `.txt`
- `.log`
- fichiers de paramétrage, docs, exports, modèles et preuves

et également le futur artefact de projet :

- `PRD.md`

---

## 7. Analyse de la MDB Érâs

### 7.1. Objectif

Construire une compréhension exploitable de la base sans supposer son schéma.

### 7.2. Tâches minimales

- identifier le format exact ;
- établir l’empreinte du fichier ;
- lister toutes les tables ;
- lister les colonnes, types, index et clés détectables ;
- compter les enregistrements par table ;
- détecter les relations évidentes ou probables ;
- identifier les tables métier les plus structurantes ;
- produire des exports de schéma lisibles ;
- échantillonner les données de façon sûre ;
- identifier les champs candidats pour les correspondances avec le dessin.

### 7.3. Sorties attendues

- `ERAS_MDB_SCHEMA.md`
- `ERAS_MDB_TABLES.csv`
- `ERAS_MDB_RELATIONSHIPS.md`
- `ERAS_MDB_FIELD_DICTIONARY.md`
- `ERAS_MDB_SAMPLE_QUERIES.sql`
- `ERAS_MDB_RISKS.md`

### 7.4. Règles d’analyse

- pas d’écriture ;
- pas de modification de structure ;
- pas de compactage ;
- pas de tentative de réparation ;
- pas de déduction non explicitée ;
- toute hypothèse doit être marquée comme **hypothèse**.

---

## 8. Analyse de la surface d’automatisation OpenCities Map / MicroStation

### 8.1. Objectif

Déterminer ce qui est **réellement accessible** depuis le poste et dans quelles conditions.

### 8.2. Questions à trancher

- Quels scripts Python existent déjà ?
- Python Manager est-il disponible et utilisable ?
- Quels exemples locaux sont présents ?
- Quelles opérations de lecture sont faisables sans risque ?
- Quels modules, key-ins, macros ou outils existent déjà ?
- Quelles sorties de preuve peut-on générer ?
- Quelles fonctions devront être pilotées autrement si Python ne couvre pas tout ?

### 8.3. Sorties attendues

- `POWEMAP_AUTOMATION_SURFACE.md`
- `POWEMAP_SCRIPT_INVENTORY.md`
- `POWEMAP_SAFE_READ_ACTIONS.md`
- `POWEMAP_GAPS_AND_FALLBACKS.md`

---

## 9. Spécification cible du futur MCP

## 9.1. Nature du système

Le futur produit est un **MCP local Windows** orienté observabilité, audit, lecture de données et automatisation progressive.

## 9.2. Architecture logique cible

Le système doit au minimum comporter :

1. **Scanner d’environnement**
2. **Adaptateur OpenCities Map / MicroStation**
3. **Adaptateur MDB Érâs**
4. **Moteur de preuves / artefacts**
5. **Serveur MCP**
6. **Suite de tests**
7. **Documentation vivante**

### 9.3. Outils MCP visés

Première proposition de surface MCP :

- `env_status()`
- `env_inventory()`
- `find_artifacts(patterns, roots)`
- `snapshot_environment()`
- `eras_list_databases()`
- `eras_describe_mdb(path)`
- `eras_list_tables(path)`
- `eras_describe_table(path, table)`
- `eras_sample_rows(path, table, limit)`
- `eras_run_readonly_query(path, query_name, params)`
- `powermap_status()`
- `powermap_list_workspaces()`
- `powermap_list_scripts()`
- `powermap_run_safe_probe(probe_name, params)`
- `powermap_collect_capabilities()`
- `compare_eras_to_powermap(context)`
- `build_prd_from_findings()`
- `build_gap_report()`

### 9.4. Contraintes MCP

- toutes les opérations dangereuses doivent être désactivées par défaut ;
- les requêtes libres doivent être interdites ou sévèrement encadrées ;
- toutes les actions doivent produire un journal ;
- les outils doivent être idempotents autant que possible ;
- les sorties doivent être conçues pour être relues par un humain.

---

## 10. Gouvernance du développement par agents

## 10.1. Rôle de l’agent principal

L’agent principal est un **orchestrateur/contrôleur**, pas un développeur manuel.

Il doit :

- planifier ;
- découper ;
- déléguer ;
- suivre ;
- contrôler la qualité ;
- valider ou refuser les livrables ;
- demander des corrections ;
- tenir à jour le plan, les risques et les preuves.

Il ne doit **pas** :

- corriger lui-même le code ;
- éditer les fichiers à la main ;
- contourner les délégations ;
- fusionner du travail sans preuves ;
- “réparer vite” localement ce qui doit être renvoyé au delegate.

## 10.2. Rôle des delegates

Les delegates doivent exécuter la quasi-totalité du travail de production.

Le modèle cible pour ces delegates est **GPT-5.3-Codex** en **effort high** dès qu’il faut explorer, coder, tester, refactorer, documenter ou analyser le système.

## 10.3. Règle de délégation

Déléguer au maximum à GPT-5.3-Codex :

- scan Windows ;
- scripts d’inventaire ;
- analyse de la MDB ;
- génération de docs ;
- mise en place du repo ;
- implémentation du MCP ;
- tests ;
- validation technique ;
- corrections.

L’agent principal garde la responsabilité du **pilotage** et du **contrôle**, mais pas de la **production manuelle**.

---

## 11. Livrables obligatoires

Le projet doit produire les fichiers suivants très tôt :

- `README.md`
- `PRD.md`
- `ARCHITECTURE.md`
- `PLAN.md`
- `BACKLOG.md`
- `RISK_REGISTER.md`
- `ENVIRONMENT_SCAN.md`
- `WINDOWS_INVENTORY.md`
- `POWEMAP_AUTOMATION_SURFACE.md`
- `ERAS_MDB_SCHEMA.md`
- `EVIDENCE_INDEX.md`
- `TEST_STRATEGY.md`
- `SECURITY_GUARDRAILS.md`

Et une structure projet similaire à :

```text
repo/
  README.md
  PRD.md
  ARCHITECTURE.md
  PLAN.md
  BACKLOG.md
  RISK_REGISTER.md
  TEST_STRATEGY.md
  SECURITY_GUARDRAILS.md
  docs/
    scans/
    evidence/
    schemas/
    reports/
  scripts/
    windows_scan/
    eras/
    powermap/
    reporting/
  src/
    mcp_server/
    adapters/
      eras_mdb/
      powermap/
    domain/
    services/
    utils/
  tests/
    unit/
    integration/
    fixtures/
  artifacts/
    inventories/
    snapshots/
    logs/
    exports/
```

---

## 12. Ordre d’exécution recommandé

## Phase 0 — Installation de la base projet

- créer le repo ;
- créer le squelette documentaire ;
- créer le plan ;
- créer les scripts d’inventaire ;
- définir les garde-fous.

## Phase 1 — Scan terrain

- lancer le scan Windows ;
- indexer les chemins ;
- inventorier logiciels et artefacts ;
- collecter les preuves ;
- construire le rapport d’environnement.

## Phase 2 — Analyse Érâs MDB

- dupliquer la MDB ;
- extraire le schéma ;
- documenter tables et champs ;
- identifier les tables cœur ;
- proposer les premières vues logiques métier.

## Phase 3 — Analyse OpenCities Map / MicroStation

- confirmer version et environnement ;
- recenser scripts, exemples, key-ins, points d’entrée ;
- valider un premier probe de lecture non destructif ;
- documenter le périmètre réellement automatisable.

## Phase 4 — PRD et architecture détaillée

- rédiger `PRD.md` ;
- figer le découpage du MCP ;
- définir les adapters ;
- définir les outils MCP ;
- formaliser les critères d’acceptation.

## Phase 5 — MVP MCP

- exposer les premiers outils d’inventaire ;
- exposer les premiers outils MDB en lecture seule ;
- exposer les premiers probes OpenCities Map ;
- produire des artefacts robustes et testés.

## Phase 6 — Contrôles de cohérence

- définir le mapping minimal dessin ↔ base ;
- construire les premiers audits ;
- produire des rapports comparatifs.

---

## 13. Critères d’acceptation du MVP

Le MVP est accepté uniquement si :

1. l’environnement Windows a été scanné et documenté ;
2. au moins une MDB a été analysée sans écriture ;
3. la surface d’automatisation OpenCities Map a été documentée avec preuves ;
4. un `PRD.md` clair a été généré ;
5. le MCP expose des outils utiles et testés ;
6. toutes les opérations potentiellement destructives sont bloquées par défaut ;
7. les artefacts de preuve sont consultables ;
8. le backlog et les risques sont à jour.

---

## 14. Définition détaillée du futur `PRD.md`

Le `PRD.md` doit contenir au minimum :

- but du produit ;
- utilisateurs ;
- contexte métier ;
- périmètre ;
- hors périmètre ;
- contraintes techniques ;
- hypothèses ;
- architecture fonctionnelle ;
- description des adapters ;
- description des outils MCP ;
- exigences de sécurité ;
- exigences de traçabilité ;
- stratégie de tests ;
- plan de livraison ;
- risques ;
- dépendances ;
- questions ouvertes.

---

## 15. Demandes explicites à Codex

Codex doit :

- agir comme une équipe de delivery structurée ;
- commencer par le scan et les preuves ;
- ne jamais supposer la structure de la MDB sans extraction ;
- ne jamais supposer les capacités de l’environnement Bentley sans observation ;
- produire des documents lisibles avant de produire du code complexe ;
- privilégier les scripts reproductibles plutôt que l’analyse opaque ;
- maintenir un journal clair de ce qui est sûr, de ce qui est prouvé, de ce qui reste hypothétique ;
- proposer des fallback techniques quand une capacité manque ;
- tester tout ce qui peut l’être sans danger.

---

## 16. Ce qu’il faut éviter

- démarrer par une implémentation “tout de suite” sans scan ;
- écrire dans la MDB de production ;
- automatiser des commandes Bentley non comprises ;
- supposer qu’un nom de table décrit correctement sa sémantique ;
- masquer les incertitudes ;
- modifier manuellement du code depuis l’agent principal ;
- fusionner des livrables non testés.

---

## 17. Sortie attendue dès le premier cycle

À l’issue du premier cycle de travail, l’équipe Codex doit fournir au minimum :

1. un repo initial ;
2. un `README.md` ;
3. un `PLAN.md` ;
4. un `PRD.md` v0 ;
5. un script de scan Windows ;
6. un script d’analyse MDB en lecture seule ;
7. un premier rapport d’inventaire ;
8. un premier rapport de surface d’automatisation OpenCities Map ;
9. un registre des risques ;
10. un backlog priorisé.

---

## 18. Format de reporting attendu

Chaque cycle doit remonter :

- **faits prouvés** ;
- **preuves collectées** ;
- **hypothèses** ;
- **blocages** ;
- **décisions proposées** ;
- **prochaines délégations**.

Le reporting doit être bref, traçable et actionnable.

---

## 19. Directive finale

Le projet doit être conduit comme un **reverse engineering contrôlé d’un poste de production** débouchant sur un **MCP local sûr, traçable et extensible**. Le but n’est pas seulement de coder, mais de **comprendre, documenter, sécuriser, puis automatiser**.
