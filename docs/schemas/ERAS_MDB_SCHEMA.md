# ERAS MDB Schema

_Generated (UTC): 2026-04-23T10:50:35.641174+00:00_

## Database: `C:\Users\killi\Documents\0 - Playground\ERAS-MCP\artifacts\work\eras_mdb\client__1f83fae2dd07.mdb`

- ODBC driver: `Microsoft Access Driver (*.mdb, *.accdb)`
- pyodbc available: `True`
- Tables discovered: `6`

### Table `cells`

- Row count: `147`
- Columns: `2`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| Nom | VARCHAR | True |
| Id | INTEGER | True |

### Table `Famille`

- Row count: `4`
- Columns: `3`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| FAM_CODE | COUNTER | False |
| FAM_NOM | VARCHAR | True |
| FAM_DESC | VARCHAR | True |

### Table `FiltreNiveau`

- Row count: `923`
- Columns: `5`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| idfiltre | COUNTER | False |
| parentid | INTEGER | True |
| idniveau | INTEGER | True |
| description | CHAR | True |
| Position | INTEGER | True |

### Table `fonts`

- Row count: `31`
- Columns: `3`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| Nom | CHAR | True |
| Id | INTEGER | True |
| Type | INTEGER | True |

### Table `levels`

- Row count: `562`
- Columns: `6`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| Id | INTEGER | True |
| nom | VARCHAR | True |
| pos | INTEGER | True |
| Couleur | INTEGER | True |
| Style | VARCHAR | True |
| Epaisseur | INTEGER | True |

### Table `version`

- Row count: `13`
- Columns: `3`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| Base | VARCHAR | True |
| Description | VARCHAR | True |
| Application | VARCHAR | True |

## Database: `C:\Users\killi\Documents\0 - Playground\ERAS-MCP\artifacts\work\eras_mdb\enedis23__251ae5c84ddf.mdb`

- ODBC driver: `Microsoft Access Driver (*.mdb, *.accdb)`
- pyodbc available: `True`
- Tables discovered: `6`

### Table `cells`

- Row count: `201`
- Columns: `2`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| Nom | VARCHAR | True |
| Id | INTEGER | True |

### Table `Famille`

- Row count: `1`
- Columns: `3`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| FAM_CODE | COUNTER | False |
| FAM_NOM | VARCHAR | True |
| FAM_DESC | VARCHAR | True |

### Table `FiltreNiveau`

- Row count: `166`
- Columns: `5`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| idfiltre | COUNTER | False |
| parentid | INTEGER | True |
| idniveau | INTEGER | True |
| description | CHAR | True |
| Position | INTEGER | True |

### Table `fonts`

- Row count: `17`
- Columns: `3`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| Nom | CHAR | True |
| Id | INTEGER | True |
| Type | INTEGER | True |

### Table `levels`

- Row count: `397`
- Columns: `6`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| Id | INTEGER | True |
| Nom | VARCHAR | True |
| pos | INTEGER | True |
| Couleur | INTEGER | True |
| Style | VARCHAR | True |
| Epaisseur | INTEGER | True |

### Table `version`

- Row count: `13`
- Columns: `3`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| Base | VARCHAR | True |
| Description | VARCHAR | True |
| Application | VARCHAR | True |

## Database: `C:\Users\killi\Documents\0 - Playground\ERAS-MCP\artifacts\work\eras_mdb\enedis23___b4781bdb9489.mdb`

- ODBC driver: `Microsoft Access Driver (*.mdb, *.accdb)`
- pyodbc available: `True`
- Tables discovered: `0`

### Warnings

- ODBC schema read failed: 'utf-16-le' codec can't decode bytes in position 72-73: illegal UTF-16 surrogate

## Database: `C:\Users\killi\Documents\0 - Playground\ERAS-MCP\artifacts\work\eras_mdb\GLOBLUTI__2a2393abd7e2.mdb`

- ODBC driver: `Microsoft Access Driver (*.mdb, *.accdb)`
- pyodbc available: `True`
- Tables discovered: `0`

### Warnings

- ODBC schema read failed: 'utf-16-le' codec can't decode bytes in position 72-73: illegal UTF-16 surrogate

## Database: `C:\Users\killi\Documents\0 - Playground\ERAS-MCP\artifacts\work\eras_mdb\ITRv2__fe69b72ac86c.mdb`

- ODBC driver: `Microsoft Access Driver (*.mdb, *.accdb)`
- pyodbc available: `True`
- Tables discovered: `6`

### Table `cells`

- Row count: `247`
- Columns: `2`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| Nom | VARCHAR | True |
| Id | INTEGER | True |

### Table `Famille`

- Row count: `1`
- Columns: `3`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| FAM_CODE | COUNTER | False |
| FAM_NOM | VARCHAR | True |
| FAM_DESC | VARCHAR | True |

### Table `FiltreNiveau`

- Row count: `133`
- Columns: `5`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| idfiltre | COUNTER | False |
| parentid | INTEGER | True |
| idniveau | INTEGER | True |
| description | CHAR | True |
| Position | INTEGER | True |

### Table `fonts`

- Row count: `17`
- Columns: `3`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| Nom | CHAR | True |
| Id | INTEGER | True |
| Type | INTEGER | True |

### Table `levels`

- Row count: `396`
- Columns: `6`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| Id | INTEGER | True |
| Nom | VARCHAR | True |
| pos | INTEGER | True |
| Couleur | INTEGER | True |
| Style | VARCHAR | True |
| Epaisseur | INTEGER | True |

### Table `version`

- Row count: `13`
- Columns: `3`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| Base | VARCHAR | True |
| Description | VARCHAR | True |
| Application | VARCHAR | True |

## Database: `C:\Users\killi\Documents\0 - Playground\ERAS-MCP\artifacts\work\eras_mdb\ITRv2___fd622f48e247.mdb`

- ODBC driver: `Microsoft Access Driver (*.mdb, *.accdb)`
- pyodbc available: `True`
- Tables discovered: `0`

### Warnings

- ODBC schema read failed: 'utf-16-le' codec can't decode bytes in position 72-73: illegal UTF-16 surrogate

## Database: `C:\Users\killi\Documents\0 - Playground\ERAS-MCP\artifacts\work\eras_mdb\enedADL_cel__3b7acb984e91.mdb`

- ODBC driver: `Microsoft Access Driver (*.mdb, *.accdb)`
- pyodbc available: `True`
- Tables discovered: `0`

### Warnings

- ODBC schema read failed: 'utf-16-le' codec can't decode bytes in position 72-73: illegal UTF-16 surrogate

## Database: `C:\Users\killi\Documents\0 - Playground\ERAS-MCP\artifacts\work\eras_mdb\ITRv3__fd5013017036.mdb`

- ODBC driver: `Microsoft Access Driver (*.mdb, *.accdb)`
- pyodbc available: `True`
- Tables discovered: `6`

### Table `cells`

- Row count: `242`
- Columns: `2`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| Nom | VARCHAR | True |
| Id | INTEGER | True |

### Table `Famille`

- Row count: `1`
- Columns: `3`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| FAM_CODE | COUNTER | False |
| FAM_NOM | VARCHAR | True |
| FAM_DESC | VARCHAR | True |

### Table `FiltreNiveau`

- Row count: `166`
- Columns: `5`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| idfiltre | COUNTER | False |
| parentid | INTEGER | True |
| idniveau | INTEGER | True |
| description | CHAR | True |
| Position | INTEGER | True |

### Table `fonts`

- Row count: `17`
- Columns: `3`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| Nom | CHAR | True |
| Id | INTEGER | True |
| Type | INTEGER | True |

### Table `levels`

- Row count: `397`
- Columns: `6`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| Id | INTEGER | True |
| Nom | VARCHAR | True |
| pos | INTEGER | True |
| Couleur | INTEGER | True |
| Style | VARCHAR | True |
| Epaisseur | INTEGER | True |

### Table `version`

- Row count: `13`
- Columns: `3`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| Base | VARCHAR | True |
| Description | VARCHAR | True |
| Application | VARCHAR | True |

## Database: `C:\Users\killi\Documents\0 - Playground\ERAS-MCP\artifacts\work\eras_mdb\ITRv3___ae93f47dbeb1.mdb`

- ODBC driver: `Microsoft Access Driver (*.mdb, *.accdb)`
- pyodbc available: `True`
- Tables discovered: `0`

### Warnings

- ODBC schema read failed: 'utf-16-le' codec can't decode bytes in position 72-73: illegal UTF-16 surrogate

## Database: `C:\Users\killi\Documents\0 - Playground\ERAS-MCP\artifacts\work\eras_mdb\enedADL_cel__3b7acb984e91.mdb`

- ODBC driver: `Microsoft Access Driver (*.mdb, *.accdb)`
- pyodbc available: `True`
- Tables discovered: `0`

### Warnings

- ODBC schema read failed: 'utf-16-le' codec can't decode bytes in position 72-73: illegal UTF-16 surrogate

## Database: `C:\Users\killi\Documents\0 - Playground\ERAS-MCP\artifacts\work\eras_mdb\ITRv4__96f0e20272d7.mdb`

- ODBC driver: `Microsoft Access Driver (*.mdb, *.accdb)`
- pyodbc available: `True`
- Tables discovered: `6`

### Table `cells`

- Row count: `201`
- Columns: `2`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| Nom | VARCHAR | True |
| Id | INTEGER | True |

### Table `Famille`

- Row count: `1`
- Columns: `3`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| FAM_CODE | COUNTER | False |
| FAM_NOM | VARCHAR | True |
| FAM_DESC | VARCHAR | True |

### Table `FiltreNiveau`

- Row count: `170`
- Columns: `5`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| idfiltre | COUNTER | False |
| parentid | INTEGER | True |
| idniveau | INTEGER | True |
| description | CHAR | True |
| Position | INTEGER | True |

### Table `fonts`

- Row count: `17`
- Columns: `3`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| Nom | CHAR | True |
| Id | INTEGER | True |
| Type | INTEGER | True |

### Table `levels`

- Row count: `397`
- Columns: `6`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| Id | INTEGER | True |
| Nom | VARCHAR | True |
| pos | INTEGER | True |
| Couleur | INTEGER | True |
| Style | VARCHAR | True |
| Epaisseur | INTEGER | True |

### Table `version`

- Row count: `13`
- Columns: `3`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| Base | VARCHAR | True |
| Description | VARCHAR | True |
| Application | VARCHAR | True |

## Database: `C:\Users\killi\Documents\0 - Playground\ERAS-MCP\artifacts\work\eras_mdb\ITRv4___1d55017817f1.mdb`

- ODBC driver: `Microsoft Access Driver (*.mdb, *.accdb)`
- pyodbc available: `True`
- Tables discovered: `0`

### Warnings

- ODBC schema read failed: 'utf-16-le' codec can't decode bytes in position 72-73: illegal UTF-16 surrogate

## Database: `C:\Users\killi\Documents\0 - Playground\ERAS-MCP\artifacts\work\eras_mdb\Modele_SIG__27dc1b587e20.mdb`

- ODBC driver: `Microsoft Access Driver (*.mdb, *.accdb)`
- pyodbc available: `True`
- Tables discovered: `14`

### Table `CABLEAER`

- Row count: `0`
- Columns: `3`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| MSLINK | COUNTER | False |
| MAPID | INTEGER | True |
| NOM | VARCHAR | True |

### Table `CANALISATION`

- Row count: `0`
- Columns: `4`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| MSLINK | COUNTER | False |
| MAPID | INTEGER | True |
| section | VARCHAR | True |
| Longueur | DOUBLE | True |

### Table `ELEMENT`

- Row count: `0`
- Columns: `3`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| MSLINK | COUNTER | False |
| MAPID | INTEGER | True |
| Nom | VARCHAR | True |

### Table `EQUIPEMENT`

- Row count: `0`
- Columns: `4`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| MSLINK | COUNTER | False |
| MAPID | INTEGER | True |
| REPERE | VARCHAR | True |
| NOM | VARCHAR | True |

### Table `FEATURE`

- Row count: `0`
- Columns: `11`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| MSLINK | INTEGER | True |
| FCODE | VARCHAR | True |
| FNAME | VARCHAR | True |
| CATEGORY | INTEGER | True |
| TABLENAME | VARCHAR | True |
| FTYPE | INTEGER | True |
| FLEVEL | INTEGER | True |
| FSTYLE | INTEGER | True |
| FWEIGHT | INTEGER | True |
| FCOLOR | INTEGER | True |
| DIGCMD | VARCHAR | True |

### Table `INPUTFORMS`

- Row count: `0`
- Columns: `7`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| FORMID | INTEGER | True |
| FORMTITLE | VARCHAR | True |
| DELETE_FLAG | INTEGER | True |
| INSERT_FLAG | INTEGER | True |
| APP_TOLOAD | VARCHAR | True |
| RSC_FILENAME | VARCHAR | True |
| PDM_ID1 | INTEGER | True |

### Table `INPUTGADGETS`

- Row count: `0`
- Columns: `17`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| FORMID | INTEGER | True |
| GADGETID | INTEGER | True |
| COLUMN_PROMPT | VARCHAR | True |
| COLUMNNAME | VARCHAR | True |
| VALUE_REQUIRED | INTEGER | True |
| DISPLAYONLY | INTEGER | True |
| WITHLIST | INTEGER | True |
| SELECTSTMT | VARCHAR | True |
| VISIBLECHARS | INTEGER | True |
| MAXCHARS | INTEGER | True |
| FIELDTYPE | INTEGER | True |
| GADGET_FORMAT | VARCHAR | True |
| SUB_FORM | INTEGER | True |
| SUB_REF_ID | INTEGER | True |
| COLUMN_ID | INTEGER | True |
| GADGET_PICTURE | VARCHAR | True |
| SELECTSTMTID | INTEGER | True |

### Table `Lien`

- Row count: `0`
- Columns: `7`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| IDLIEN | COUNTER | False |
| IDPERE | INTEGER | True |
| IDFILS | INTEGER | True |
| ChampsFils | VARCHAR | True |
| ChampsPere | VARCHAR | True |
| IdValeurFils | INTEGER | True |
| IdValeurPere | INTEGER | True |

### Table `maps`

- Row count: `0`
- Columns: `3`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| mslink | COUNTER | False |
| category | INTEGER | True |
| mapname | VARCHAR | True |

### Table `MSCATALOG`

- Row count: `15`
- Columns: `9`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| TABLENAME | VARCHAR | True |
| ENTITYNUM | INTEGER | True |
| NEXTOCC | INTEGER | True |
| SCREENFORM | VARCHAR | True |
| REPORTTABLE | VARCHAR | True |
| SQLREVIEW | VARCHAR | True |
| FENCEFILTER | VARCHAR | True |
| DASTABLE | VARCHAR | True |
| TABLETYPE | VARCHAR | True |

### Table `POTEAU`

- Row count: `0`
- Columns: `4`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| MSLINK | COUNTER | False |
| MAPID | INTEGER | True |
| REPERE | VARCHAR | True |
| NOM | VARCHAR | True |

### Table `TblDocument`

- Row count: `6`
- Columns: `7`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| IdDocument | COUNTER | False |
| IdBdElement | INTEGER | True |
| NomFichier | VARCHAR | True |
| TypeFichier | INTEGER | True |
| Observation | VARCHAR | True |
| DateCreation | DATETIME | True |
| Parent | INTEGER | True |

### Table `TblTypeDocument`

- Row count: `6`
- Columns: `3`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| IdTypeDocument | COUNTER | False |
| Libelle | VARCHAR | True |
| ExtensionFichier | CHAR | True |

### Table `VALDEFAUT`

- Row count: `0`
- Columns: `5`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| FEATUREID | DOUBLE | True |
| FNAME | VARCHAR | True |
| TABLENAME | VARCHAR | True |
| COLUMN_NAME | VARCHAR | True |
| VALUE | VARCHAR | True |

## Database: `C:\Users\killi\Documents\0 - Playground\ERAS-MCP\artifacts\work\eras_mdb\Affaires__53aaa8dfe53a.mdb`

- ODBC driver: `Microsoft Access Driver (*.mdb, *.accdb)`
- pyodbc available: `True`
- Tables discovered: `0`

### Warnings

- ODBC schema read failed: 'utf-16-le' codec can't decode bytes in position 72-73: illegal UTF-16 surrogate

## Database: `C:\Users\killi\Documents\0 - Playground\ERAS-MCP\artifacts\work\eras_mdb\C11_201__de89ce11c288.mdb`

- ODBC driver: `Microsoft Access Driver (*.mdb, *.accdb)`
- pyodbc available: `True`
- Tables discovered: `17`

### Table `CalculPart`

- Row count: `20`
- Columns: `95`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| Nom | VARCHAR | True |
| Type Ligne(0) | SMALLINT | True |
| Type Ligne(1) | SMALLINT | True |
| Type Ligne(2) | SMALLINT | True |
| Type Ligne(3) | SMALLINT | True |
| Calcul en GD | SMALLINT | True |
| Application de givre en GD(0) | SMALLINT | True |
| Application de givre en GD(1) | SMALLINT | True |
| Application de givre en GD(2) | SMALLINT | True |
| Application de givre en GD(3) | SMALLINT | True |
| Présence ligne(00) | SMALLINT | True |
| Coef hypothèse(00) | REAL | True |
| Présence ligne(01) | SMALLINT | True |
| Coef hypothèse(01) | REAL | True |
| Présence ligne(02) | SMALLINT | True |
| Coef hypothèse(02) | REAL | True |
| Présence ligne(03) | SMALLINT | True |
| Coef hypothèse(03) | REAL | True |
| Présence ligne(10) | SMALLINT | True |
| Coef hypothèse(10) | REAL | True |
| Présence ligne(11) | SMALLINT | True |
| Coef hypothèse(11) | REAL | True |
| Présence ligne(12) | SMALLINT | True |
| Coef hypothèse(12) | REAL | True |
| Présence ligne(13) | SMALLINT | True |
| Coef hypothèse(13) | REAL | True |
| Présence ligne(20) | SMALLINT | True |
| Coef hypothèse(20) | REAL | True |
| Présence ligne(21) | SMALLINT | True |
| Coef hypothèse(21) | REAL | True |
| Présence ligne(22) | SMALLINT | True |
| Coef hypothèse(22) | REAL | True |
| Présence ligne(23) | SMALLINT | True |
| Coef hypothèse(23) | REAL | True |
| Présence ligne(30) | SMALLINT | True |
| Coef hypothèse(30) | REAL | True |
| Présence ligne(31) | SMALLINT | True |
| Coef hypothèse(31) | REAL | True |
| Présence ligne(32) | SMALLINT | True |
| Coef hypothèse(32) | REAL | True |
| Présence ligne(33) | SMALLINT | True |
| Coef hypothèse(33) | REAL | True |
| Présence ligne(40) | SMALLINT | True |
| Coef hypothèse(40) | REAL | True |
| Présence ligne(41) | SMALLINT | True |
| Coef hypothèse(41) | REAL | True |
| Présence ligne(42) | SMALLINT | True |
| Coef hypothèse(42) | REAL | True |
| Présence ligne(43) | SMALLINT | True |
| Coef hypothèse(43) | REAL | True |
| Présence ligne(50) | SMALLINT | True |
| Coef hypothèse(50) | REAL | True |
| Présence ligne(51) | SMALLINT | True |
| Coef hypothèse(51) | REAL | True |
| Présence ligne(52) | SMALLINT | True |
| Coef hypothèse(52) | REAL | True |
| Présence ligne(53) | SMALLINT | True |
| Coef hypothèse(53) | REAL | True |
| Présence ligne(60) | SMALLINT | True |
| Coef hypothèse(60) | REAL | True |
| Présence ligne(61) | SMALLINT | True |
| Coef hypothèse(61) | REAL | True |
| Présence ligne(62) | SMALLINT | True |
| Coef hypothèse(62) | REAL | True |
| Présence ligne(63) | SMALLINT | True |
| Coef hypothèse(63) | REAL | True |
| Présence ligne(70) | SMALLINT | True |
| Coef hypothèse(70) | REAL | True |
| Présence ligne(71) | SMALLINT | True |
| Coef hypothèse(71) | REAL | True |
| Présence ligne(72) | SMALLINT | True |
| Coef hypothèse(72) | REAL | True |
| Présence ligne(73) | SMALLINT | True |
| Coef hypothèse(73) | REAL | True |
| Présence ligne(80) | SMALLINT | True |
| Coef hypothèse(80) | REAL | True |
| Présence ligne(81) | SMALLINT | True |
| Coef hypothèse(81) | REAL | True |
| Présence ligne(82) | SMALLINT | True |
| Coef hypothèse(82) | REAL | True |
| Présence ligne(83) | SMALLINT | True |
| Coef hypothèse(83) | REAL | True |
| Présence ligne(90) | SMALLINT | True |
| Coef hypothèse(90) | REAL | True |
| Présence ligne(91) | SMALLINT | True |
| Coef hypothèse(91) | REAL | True |
| Présence ligne(92) | SMALLINT | True |
| Coef hypothèse(92) | REAL | True |
| Présence ligne(93) | SMALLINT | True |
| Coef hypothèse(93) | REAL | True |
| Hypothèse(0) | VARCHAR | True |
| Hypothèse(1) | VARCHAR | True |
| Hypothèse(2) | VARCHAR | True |
| Hypothèse(3) | VARCHAR | True |
| Numéro | SMALLINT | True |

### Table `Classe`

- Row count: `40`
- Columns: `23`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| Nom | VARCHAR | True |
| Nature | SMALLINT | True |
| Structure | SMALLINT | True |
| Coef Tau | REAL | True |
| Coef Tau en DP | REAL | True |
| Recherche | SMALLINT | True |
| Effort branchement(0) | REAL | True |
| Effort branchement(1) | REAL | True |
| Effort H61 | REAL | True |
| Forme | SMALLINT | True |
| Diagramme effort | SMALLINT | True |
| Cellule BP | VARCHAR | True |
| Fichier graphique | VARCHAR | True |
| Caché | SMALLINT | True |
| Element de base | SMALLINT | True |
| Distance torsion monophasé | REAL | True |
| Distance torsion triphasé | REAL | True |
| Haubanage | SMALLINT | True |
| Assemblage | SMALLINT | True |
| Ecart | REAL | True |
| Description | VARCHAR | True |
| Symetrique | VARCHAR | True |
| Effort Min si H61 | REAL | True |

### Table `Commune`

- Row count: `36211`
- Columns: `7`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| Id | COUNTER | False |
| Dep | VARCHAR | True |
| Insee | VARCHAR | True |
| Nom | VARCHAR | True |
| ZoneVent | REAL | True |
| ZoneGivre | REAL | True |
| ZoneNeige | REAL | True |

### Table `Configuration`

- Row count: `1`
- Columns: `148`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| Nom | VARCHAR | True |
| Libellé | VARCHAR | True |
| Technique nord-américaine | SMALLINT | True |
| Vent sur supports BT | SMALLINT | True |
| Hypothèse DP sur supports bois | SMALLINT | True |
| Installation de DAC | SMALLINT | True |
| Affichage coef travail | SMALLINT | True |
| Option vérification | SMALLINT | True |
| Affichage panneau retournement | SMALLINT | True |
| Vent sur supports(0) | REAL | True |
| Vent sur supports(1) | REAL | True |
| Vent sur supports(2) | REAL | True |
| Vent sur supports(3) | REAL | True |
| Groupe hypothèses | VARCHAR | True |
| Température(0) | REAL | True |
| Température(1) | REAL | True |
| Température(2) | REAL | True |
| Température(3) | REAL | True |
| Température(4) | REAL | True |
| Température(5) | REAL | True |
| Température(6) | REAL | True |
| Coef écartement(0) | VARCHAR | True |
| Coef écartement(1) | VARCHAR | True |
| Coef écartement(2) | VARCHAR | True |
| Ks normal | REAL | True |
| Ks sécurité | REAL | True |
| a(0) | REAL | True |
| b(0) | REAL | True |
| a(1) | REAL | True |
| b(1) | REAL | True |
| a(2) | REAL | True |
| b(2) | REAL | True |
| a(3) | REAL | True |
| b(3) | REAL | True |
| a(4) | REAL | True |
| b(4) | REAL | True |
| a(5) | REAL | True |
| b(5) | REAL | True |
| a(6) | REAL | True |
| b(6) | REAL | True |
| a(7) | REAL | True |
| b(7) | REAL | True |
| a(8) | REAL | True |
| b(8) | REAL | True |
| a(9) | REAL | True |
| b(9) | REAL | True |
| a(10) | REAL | True |
| b(10) | REAL | True |
| a(11) | REAL | True |
| b(11) | REAL | True |
| a(12) | REAL | True |
| b(12) | REAL | True |
| a(13) | REAL | True |
| b(13) | REAL | True |
| a(14) | REAL | True |
| b(14) | REAL | True |
| a(15) | REAL | True |
| b(15) | REAL | True |
| Degré Celsius | SMALLINT | True |
| Grade | SMALLINT | True |
| Sens trigonométrique | SMALLINT | True |
| Valeur de tension(0) | REAL | True |
| Valeur de tension(1) | REAL | True |
| Support-type | VARCHAR | True |
| Sortie récapitulatif word 6 | SMALLINT | True |
| Protection | VARCHAR | True |
| Angle de profil limite | REAL | True |
| Hypothèse standard chainettes | VARCHAR | True |
| Hypothèse complémentaire chainettes | VARCHAR | True |
| Fichier obstacles | VARCHAR | True |
| Pression pour zone vent fort | REAL | True |
| Effort référence fouille | REAL | True |
| Libellé de tension(0) | VARCHAR | True |
| Libellé de tension(1) | VARCHAR | True |
| Libellé de tension(2) | VARCHAR | True |
| Libellé de tension(3) | VARCHAR | True |
| Hypo de surcharge pour définition conducteur(0) | VARCHAR | True |
| Hypo de surcharge pour définition conducteur(1) | VARCHAR | True |
| Hypo de surcharge pour définition conducteur(2) | VARCHAR | True |
| Hypo de surcharge pour définition conducteur(3) | VARCHAR | True |
| Valeur de tension par défaut(0) | REAL | True |
| Valeur de tension par défaut(1) | REAL | True |
| Valeur de tension par défaut(2) | REAL | True |
| Valeur de tension par défaut(3) | REAL | True |
| Distance min croisement(0) | REAL | True |
| Voltage croisement surplomb(0) | SMALLINT | True |
| Voltage croisement surplombee(0) | SMALLINT | True |
| Distance min croisement(1) | REAL | True |
| Voltage croisement surplomb(1) | SMALLINT | True |
| Voltage croisement surplombee(1) | SMALLINT | True |
| Distance min croisement(2) | REAL | True |
| Voltage croisement surplomb(2) | SMALLINT | True |
| Voltage croisement surplombee(2) | SMALLINT | True |
| Distance min croisement(3) | REAL | True |
| Voltage croisement surplomb(3) | SMALLINT | True |
| Voltage croisement surplombee(3) | SMALLINT | True |
| Distance min croisement(4) | REAL | True |
| Voltage croisement surplomb(4) | SMALLINT | True |
| Voltage croisement surplombee(4) | SMALLINT | True |
| Distance min croisement(5) | REAL | True |
| Voltage croisement surplomb(5) | SMALLINT | True |
| Voltage croisement surplombee(5) | SMALLINT | True |
| Famille hypothèse(0) | VARCHAR | True |
| Famille hypothèse(1) | VARCHAR | True |
| Famille hypothèse(2) | VARCHAR | True |
| Famille hypothèse(3) | VARCHAR | True |
| Famille hypothèse(4) | VARCHAR | True |
| Famille hypothèse(5) | VARCHAR | True |
| Famille hypothèse(6) | VARCHAR | True |
| Famille hypothèse(7) | VARCHAR | True |
| Famille hypothèse(8) | VARCHAR | True |
| Famille hypothèse(9) | VARCHAR | True |
| Famille hypothèse liée(0) | VARCHAR | True |
| Famille hypothèse liée(1) | VARCHAR | True |
| Famille hypothèse liée(2) | VARCHAR | True |
| Famille hypothèse liée(3) | VARCHAR | True |
| Famille hypothèse liée(4) | VARCHAR | True |
| Famille hypothèse liée(5) | VARCHAR | True |
| Famille hypothèse liée(6) | VARCHAR | True |
| Famille hypothèse liée(7) | VARCHAR | True |
| Famille hypothèse liée(8) | VARCHAR | True |
| Famille hypothèse liée(9) | VARCHAR | True |
| Température de réglage(0) | REAL | True |
| Température de réglage(1) | REAL | True |
| Température de réglage(2) | REAL | True |
| Température de réglage(3) | REAL | True |
| Température de réglage(4) | REAL | True |
| Température de réglage(5) | REAL | True |
| Température de réglage(6) | REAL | True |
| Température de réglage(7) | REAL | True |
| Température de réglage(8) | REAL | True |
| Température de réglage(9) | REAL | True |
| Type mécanique(0) | VARCHAR | True |
| Type mécanique(1) | VARCHAR | True |
| Type mécanique(2) | VARCHAR | True |
| Distance min fouille portique | REAL | True |
| Coef distance min croisement | REAL | True |
| Option croisement francais | REAL | True |
| Coef dépassemement portée max | REAL | True |
| Nature autre | VARCHAR | True |
| Nature autre réduit | VARCHAR | True |
| Hypothèse VIB en nu | SMALLINT | True |
| Hypothèse VIB en torsadé | SMALLINT | True |
| Compression supports bois | SMALLINT | True |
| Type haubanage selon orientation | SMALLINT | True |
| Lignes TV avec HTA | SMALLINT | True |
| Version | REAL | True |
| optCommunes | SMALLINT | True |

### Table `Configuration(suite)`

- Row count: `1`
- Columns: `38`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| Sigma(0) | REAL | True |
| Sigma(1) | REAL | True |
| Sigma(2) | REAL | True |
| Sigma(3) | REAL | True |
| Sigma(4) | REAL | True |
| Sigma(5) | REAL | True |
| Sigma(6) | REAL | True |
| Sigma(7) | REAL | True |
| Sigma(8) | REAL | True |
| Sigma(9) | REAL | True |
| Sigma(10) | REAL | True |
| Sigma(11) | REAL | True |
| Sigma(12) | REAL | True |
| Sigma(13) | REAL | True |
| Sigma(14) | REAL | True |
| Sigma(15) | REAL | True |
| Sigma(16) | REAL | True |
| Sigma(17) | REAL | True |
| Sigma(18) | REAL | True |
| Sigma(19) | REAL | True |
| Sigma(20) | REAL | True |
| Sigma(21) | REAL | True |
| Sigma(22) | REAL | True |
| Sigma(23) | REAL | True |
| Sigma(24) | REAL | True |
| Sigma(25) | REAL | True |
| Pression Max Terre | REAL | True |
| Masse Volumique Terre | REAL | True |
| Masse Volumique Béton | REAL | True |
| Temps enregistrement | REAL | True |
| Enregistrement activé | SMALLINT | True |
| Association DAC-Canton | SMALLINT | True |
| VoltMinCroise1 | DOUBLE | True |
| VoltMinCroise2 | DOUBLE | True |
| VoltMinCroise3 | DOUBLE | True |
| TempMinCroise1 | DOUBLE | True |
| TempMinCroise2 | DOUBLE | True |
| TempMinCroise3 | DOUBLE | True |

### Table `Câble`

- Row count: `646`
- Columns: `90`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| Nom | VARCHAR | True |
| Volt | VARCHAR | True |
| Type | SMALLINT | True |
| Section réelle | REAL | True |
| Diamètre | REAL | True |
| Masse linéique | REAL | True |
| Module d'Young | REAL | True |
| Coef de dilatation | REAL | True |
| Charge de rupture nominale | REAL | True |
| Portée maximale suspendu | REAL | True |
| Portée moyenne conseillée suspendu | REAL | True |
| Paramètre conseillé suspendu | REAL | True |
| Portée maximale rigide écart | REAL | True |
| Portée moyenne conseillée rigide écart | REAL | True |
| Tension conseillée rigide écart | REAL | True |
| Portée maximale rigide agglo | REAL | True |
| Portée moyenne conseillée rigide agglo | REAL | True |
| Tension conseillée rigide agglo | REAL | True |
| Portée maximale suspendu ZVF | REAL | True |
| Portée moyenne conseillée suspendu ZVF | REAL | True |
| Paramètre conseillé suspendu ZVF | REAL | True |
| Portée maximale rigide écart ZVF | REAL | True |
| Portée moyenne conseillée rigide écart ZVF | REAL | True |
| Tension conseillée rigide écart ZVF | REAL | True |
| Portée maximale rigide agglo ZVF | REAL | True |
| Portée moyenne conseillée rigide agglo ZVF | REAL | True |
| Tension conseillée rigide agglo ZVF | REAL | True |
| Caché | SMALLINT | True |
| Element de base | SMALLINT | True |
| Portée max sus 1 | REAL | True |
| Portée moyenne conseillée sus 1 | REAL | True |
| Portée moyenne conseillée sus 2 | REAL | True |
| Portée moyenne conseillée sus 3 | REAL | True |
| Portée max sus 2 | REAL | True |
| Portée max sus 3 | REAL | True |
| Paramètre conseillé sus 1 | REAL | True |
| Paramètre conseillé sus 2 | REAL | True |
| Paramètre conseillé sus 3 | REAL | True |
| Portée max sus ZVF 1 | REAL | True |
| Portée max sus ZVF 2 | REAL | True |
| Portée max sus ZVF 3 | REAL | True |
| Portée moyenne conseillée sus ZVF 1 | REAL | True |
| Portée moyenne conseillée sus ZVF 2 | REAL | True |
| Portée moyenne conseillée sus ZVF 3 | REAL | True |
| Paramètre conseillé sus ZVF 1 | REAL | True |
| Paramètre conseillé sus ZVF 2 | REAL | True |
| Paramètre conseillé sus ZVF 3 | REAL | True |
| Portée max rig écart 1 | REAL | True |
| Portée max rig écart 2 | REAL | True |
| Portée max rig écart 3 | REAL | True |
| Portée max rig écart ZVF 1 | REAL | True |
| Portée max rig écart ZVF 2 | REAL | True |
| Portée max rig écart ZVF 3 | REAL | True |
| Portée max rig agglo 1 | REAL | True |
| Portée max rig agglo 2 | REAL | True |
| Portée max rig agglo 3 | REAL | True |
| Portée max rig agglo ZVF 1 | REAL | True |
| Portée max rig agglo ZVF 2 | REAL | True |
| Portée max rig agglo ZVF 3 | REAL | True |
| Portée moy conseillée rig écart 1 | REAL | True |
| Portée moy conseillée rig écart 2 | REAL | True |
| Portée moy conseillée rig écart 3 | REAL | True |
| Portée moy conseillée rig écart ZVF 1 | REAL | True |
| Portée moy conseillée rig écart ZVF 2 | REAL | True |
| Portée moy conseillée rig écart ZVF 3 | REAL | True |
| Portée moy conseillée rig agglo 1 | REAL | True |
| Portée moy conseillée rig agglo 2 | REAL | True |
| Portée moy conseillée rig agglo 3 | REAL | True |
| Portée moy conseillée rig agglo ZVF 1 | REAL | True |
| Portée moy conseillée rig agglo ZVF 2 | REAL | True |
| Portée moy conseillée rig agglo ZVF 3 | REAL | True |
| Tension conseillée rig écart 1 | REAL | True |
| Tension conseillée rig écart 2 | REAL | True |
| Tension conseillée rig écart 3 | REAL | True |
| Tension conseillée rig écart ZVF 1 | REAL | True |
| Tension conseillée rig écart ZVF 2 | REAL | True |
| Tension conseillée rig écart ZVF 3 | REAL | True |
| Tension conseillée rig agglo 1 | REAL | True |
| Tension conseillée rig agglo 2 | REAL | True |
| Tension conseillée rig agglo 3 | REAL | True |
| Tension conseillée rig agglo ZVF 1 | REAL | True |
| Tension conseillée rig agglo ZVF 2 | REAL | True |
| Tension conseillée rig agglo ZVF 3 | REAL | True |
| Limite vibration | REAL | True |
| Gamme de tension | SMALLINT | True |
| Sigma(0) | REAL | True |
| Sigma(1) | REAL | True |
| Valeur | REAL | True |
| AncienNom | VARCHAR | True |
| Description | VARCHAR | True |

### Table `Dac`

- Row count: `22`
- Columns: `8`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| Nom | VARCHAR | True |
| Gamme | VARCHAR | True |
| Effort ruine | REAL | True |
| Longueur de détente | REAL | True |
| Caché | SMALLINT | True |
| Element de base | SMALLINT | True |
| Effort déclenchement | REAL | True |
| Valeur | REAL | True |

### Table `Equipement`

- Row count: `6`
- Columns: `10`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| Nom | VARCHAR | True |
| Effort forfaitaire | REAL | True |
| Décalage armement(0) | REAL | True |
| Décalage armement(1) | REAL | True |
| Décalage armement(2) | REAL | True |
| Décalage armement(3) | REAL | True |
| Elément de base | SMALLINT | True |
| Caché | SMALLINT | True |
| Description | VARCHAR | True |
| Valeur | REAL | True |

### Table `Famille armement`

- Row count: `40`
- Columns: `21`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| Famille | VARCHAR | True |
| Technique | SMALLINT | True |
| Nb fils | SMALLINT | True |
| Kc | REAL | True |
| Angle piquetage maxi | REAL | True |
| Caché | SMALLINT | True |
| Element de base | SMALLINT | True |
| Kc rigide | REAL | True |
| Diagramme effort | SMALLINT | True |
| Tronqué | SMALLINT | True |
| Gamme de tension | SMALLINT | True |
| Conducteur par défaut | VARCHAR | True |
| Tension saisie | SMALLINT | True |
| Neutre par défaut | VARCHAR | True |
| Décalage neutre | REAL | True |
| Kc neutre | REAL | True |
| Option type mécanique | SMALLINT | True |
| Fichier graphique | VARCHAR | True |
| Nom réduit défaut | VARCHAR | True |
| Type NV | SMALLINT | True |
| Fusible | INTEGER | True |

### Table `Groupe d'hypothèses`

- Row count: `7`
- Columns: `10`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| Nom | VARCHAR | True |
| Description | VARCHAR | True |
| Hypo(1) | VARCHAR | True |
| Hypo(2) | VARCHAR | True |
| Hypo(3) | VARCHAR | True |
| Hypo(0) | VARCHAR | True |
| Hypo(4) | VARCHAR | True |
| Hypo(5) | VARCHAR | True |
| Hypo(6) | VARCHAR | True |
| Hypo(7) | VARCHAR | True |

### Table `Hypothèse`

- Row count: `57`
- Columns: `19`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| Nom | VARCHAR | True |
| Volt | VARCHAR | True |
| Description | VARCHAR | True |
| Température | REAL | True |
| Pression de Vent conducteurs | REAL | True |
| Pression de Vent surfaces planes | REAL | True |
| Pression de Vent surfaces cylindriques | REAL | True |
| Pression de Vent surfaces polygonales | REAL | True |
| Masse de givre maxi | REAL | True |
| Masse de givre mini | REAL | True |
| Epaisseur de givre maxi | REAL | True |
| Epaisseur de givre mini | REAL | True |
| Kz | REAL | True |
| Caché | SMALLINT | True |
| Element de base | SMALLINT | True |
| Gamme de tension | SMALLINT | True |
| Utilisation | SMALLINT | True |
| Densité de givre | REAL | True |
| Pression de Vent surfaces autres | REAL | True |

### Table `Isolateur`

- Row count: `19`
- Columns: `28`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| Nom complet | VARCHAR | True |
| Type | VARCHAR | True |
| Effort ruine | REAL | True |
| Longueur chaîne | REAL | True |
| Poids chaîne | REAL | True |
| Tangente max | REAL | True |
| Tension | REAL | True |
| Caché | SMALLINT | True |
| Element de base | SMALLINT | True |
| Famille armement(0) | VARCHAR | True |
| Famille armement(1) | VARCHAR | True |
| Famille armement(2) | VARCHAR | True |
| Famille armement(3) | VARCHAR | True |
| Famille armement(4) | VARCHAR | True |
| Famille armement(5) | VARCHAR | True |
| Famille armement(6) | VARCHAR | True |
| Famille armement(7) | VARCHAR | True |
| Famille armement(8) | VARCHAR | True |
| Famille armement(9) | VARCHAR | True |
| Famille armement(10) | VARCHAR | True |
| Famille armement(11) | VARCHAR | True |
| Famille armement(12) | VARCHAR | True |
| Famille armement(13) | VARCHAR | True |
| Famille armement(14) | VARCHAR | True |
| Famille armement(15) | VARCHAR | True |
| Description | VARCHAR | True |
| Norme | VARCHAR | True |
| Valeur | REAL | True |

### Table `Nom complet armement`

- Row count: `583`
- Columns: `17`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| Nom réduit | VARCHAR | True |
| Nom Complet | VARCHAR | True |
| Effort ruine(0) | REAL | True |
| Flexibilité | REAL | True |
| Caché | SMALLINT | True |
| Element de base | SMALLINT | True |
| Effort ruine(1) | REAL | True |
| Effort ruine(2) | REAL | True |
| Effort ruine(3) | REAL | True |
| Pente trapèze | REAL | True |
| Effort minimal support | REAL | True |
| Classe support min | VARCHAR | True |
| Effort réf | REAL | True |
| Traverse | REAL | True |
| Montant | REAL | True |
| Valeur | REAL | True |
| EffortFusible | DOUBLE | True |

### Table `Nom réduit armement`

- Row count: `133`
- Columns: `19`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| Famille | VARCHAR | True |
| Nom réduit | VARCHAR | True |
| Structure | SMALLINT | True |
| y0 | REAL | True |
| y1 | REAL | True |
| y2 | REAL | True |
| y3 | REAL | True |
| y4 | REAL | True |
| y5 | REAL | True |
| z0 | REAL | True |
| z1 | REAL | True |
| z2 | REAL | True |
| z3 | REAL | True |
| z4 | REAL | True |
| z5 | REAL | True |
| Caché | SMALLINT | True |
| Element de base | SMALLINT | True |
| Coef tangente inclinaison | REAL | True |
| Ecart | REAL | True |

### Table `Observations`

- Row count: `9`
- Columns: `1`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| Libellé | VARCHAR | True |

### Table `Support`

- Row count: `2651`
- Columns: `29`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| Nom | VARCHAR | True |
| Hauteur | REAL | True |
| Classe | VARCHAR | True |
| Effort ruine | REAL | True |
| Flexibilité | REAL | True |
| Flexibilité Y | REAL | True |
| Largeur base | REAL | True |
| Epaisseur base | REAL | True |
| Largeur sommet | REAL | True |
| Epaisseur sommet | REAL | True |
| Fondation b(0) | REAL | True |
| Fondation b(1) | REAL | True |
| Fondation b(2) | REAL | True |
| Fondation b(3) | REAL | True |
| Fondation b(4) | REAL | True |
| Fondation b(5) | REAL | True |
| Fondation b(6) | REAL | True |
| Fondation b(7) | REAL | True |
| Fondation b(8) | REAL | True |
| Fondation b(9) | REAL | True |
| Fondation b(10) | REAL | True |
| Fondation b(11) | REAL | True |
| Effort max compression | REAL | True |
| Effort ruine en DP | REAL | True |
| Caché HTA | SMALLINT | True |
| Element de base | SMALLINT | True |
| Caché BT | SMALLINT | True |
| Valeur | REAL | True |
| obsolete | INTEGER | True |

### Table `Support-type`

- Row count: `2`
- Columns: `166`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| Nom | VARCHAR | True |
| Hauteur(0) | REAL | True |
| Classe(0) | VARCHAR | True |
| Nature(0) | SMALLINT | True |
| Structure(0) | SMALLINT | True |
| Omega(0) | REAL | True |
| Armement(0) | VARCHAR | True |
| Omega armement(0) | REAL | True |
| Branchement(0) | SMALLINT | True |
| Isolateur(0) | VARCHAR | True |
| Hauteur(1) | REAL | True |
| Classe(1) | VARCHAR | True |
| Nature(1) | SMALLINT | True |
| Structure(1) | SMALLINT | True |
| Omega(1) | REAL | True |
| Armement(1) | VARCHAR | True |
| Omega armement(1) | REAL | True |
| Branchement(1) | SMALLINT | True |
| Isolateur(1) | VARCHAR | True |
| Hauteur(2) | REAL | True |
| Classe(2) | VARCHAR | True |
| Nature(2) | SMALLINT | True |
| Structure(2) | SMALLINT | True |
| Omega(2) | REAL | True |
| Armement(2) | VARCHAR | True |
| Omega armement(2) | REAL | True |
| Branchement(2) | SMALLINT | True |
| Isolateur(2) | VARCHAR | True |
| Hauteur(3) | REAL | True |
| Classe(3) | VARCHAR | True |
| Nature(3) | SMALLINT | True |
| Structure(3) | SMALLINT | True |
| Omega(3) | REAL | True |
| Armement(3) | VARCHAR | True |
| Omega armement(3) | REAL | True |
| Branchement(3) | SMALLINT | True |
| Isolateur(3) | VARCHAR | True |
| Hauteur(4) | REAL | True |
| Classe(4) | VARCHAR | True |
| Nature(4) | SMALLINT | True |
| Structure(4) | SMALLINT | True |
| Omega(4) | REAL | True |
| Armement(4) | VARCHAR | True |
| Omega armement(4) | REAL | True |
| Branchement(4) | SMALLINT | True |
| Isolateur(4) | VARCHAR | True |
| Hauteur(5) | REAL | True |
| Classe(5) | VARCHAR | True |
| Nature(5) | SMALLINT | True |
| Structure(5) | SMALLINT | True |
| Omega(5) | REAL | True |
| Armement(5) | VARCHAR | True |
| Omega armement(5) | REAL | True |
| Branchement(5) | SMALLINT | True |
| Isolateur(5) | VARCHAR | True |
| Hauteur(6) | REAL | True |
| Classe(6) | VARCHAR | True |
| Nature(6) | SMALLINT | True |
| Structure(6) | SMALLINT | True |
| Omega(6) | REAL | True |
| Armement(6) | VARCHAR | True |
| Omega armement(6) | REAL | True |
| Branchement(6) | SMALLINT | True |
| Isolateur(6) | VARCHAR | True |
| Hauteur(7) | REAL | True |
| Classe(7) | VARCHAR | True |
| Nature(7) | SMALLINT | True |
| Structure(7) | SMALLINT | True |
| Omega(7) | REAL | True |
| Armement(7) | VARCHAR | True |
| Omega armement(7) | REAL | True |
| Branchement(7) | SMALLINT | True |
| Isolateur(7) | VARCHAR | True |
| Hauteur(8) | REAL | True |
| Classe(8) | VARCHAR | True |
| Nature(8) | SMALLINT | True |
| Structure(8) | SMALLINT | True |
| Omega(8) | REAL | True |
| Armement(8) | VARCHAR | True |
| Omega armement(8) | REAL | True |
| Branchement(8) | SMALLINT | True |
| Isolateur(8) | VARCHAR | True |
| Hauteur(9) | REAL | True |
| Classe(9) | VARCHAR | True |
| Nature(9) | SMALLINT | True |
| Structure(9) | SMALLINT | True |
| Omega(9) | REAL | True |
| Armement(9) | VARCHAR | True |
| Omega armement(9) | REAL | True |
| Branchement(9) | SMALLINT | True |
| Isolateur(9) | VARCHAR | True |
| Ks(0) | REAL | True |
| Nature sol(0) | VARCHAR | True |
| Ks(1) | REAL | True |
| Nature sol(1) | VARCHAR | True |
| Ks(2) | REAL | True |
| Nature sol(2) | VARCHAR | True |
| Ks(3) | REAL | True |
| Nature sol(3) | VARCHAR | True |
| Ks(4) | REAL | True |
| Nature sol(4) | VARCHAR | True |
| Ks(5) | REAL | True |
| Nature sol(5) | VARCHAR | True |
| Ks(6) | REAL | True |
| Nature sol(6) | VARCHAR | True |
| Ks(7) | REAL | True |
| Nature sol(7) | VARCHAR | True |
| Ks(8) | REAL | True |
| Nature sol(8) | VARCHAR | True |
| Ks(9) | REAL | True |
| Nature sol(9) | VARCHAR | True |
| Hauteur(10) | DOUBLE | True |
| Classe(10) | VARCHAR | True |
| Nature(10) | INTEGER | True |
| Structure(10) | INTEGER | True |
| Omega(10) | DOUBLE | True |
| Armement(10) | VARCHAR | True |
| Omega armement(10) | DOUBLE | True |
| Branchement(10) | INTEGER | True |
| Isolateur(10) | VARCHAR | True |
| Ks(10) | DOUBLE | True |
| Nature sol(10) | VARCHAR | True |
| Hauteur(11) | DOUBLE | True |
| Classe(11) | VARCHAR | True |
| Nature(11) | INTEGER | True |
| Structure(11) | INTEGER | True |
| Omega(11) | DOUBLE | True |
| Armement(11) | VARCHAR | True |
| Omega armement(11) | DOUBLE | True |
| Branchement(11) | INTEGER | True |
| Isolateur(11) | VARCHAR | True |
| Ks(11) | DOUBLE | True |
| Nature sol(11) | VARCHAR | True |
| Hauteur(12) | DOUBLE | True |
| Classe(12) | VARCHAR | True |
| Nature(12) | INTEGER | True |
| Structure(12) | INTEGER | True |
| Omega(12) | DOUBLE | True |
| Armement(12) | VARCHAR | True |
| Omega armement(12) | DOUBLE | True |
| Branchement(12) | INTEGER | True |
| Isolateur(12) | VARCHAR | True |
| Ks(12) | DOUBLE | True |
| Nature sol(12) | VARCHAR | True |
| Hauteur(13) | DOUBLE | True |
| Classe(13) | VARCHAR | True |
| Nature(13) | INTEGER | True |
| Structure(13) | INTEGER | True |
| Omega(13) | DOUBLE | True |
| Armement(13) | VARCHAR | True |
| Omega armement(13) | DOUBLE | True |
| Branchement(13) | INTEGER | True |
| Isolateur(13) | VARCHAR | True |
| Ks(13) | DOUBLE | True |
| Nature sol(13) | VARCHAR | True |
| Hauteur(14) | DOUBLE | True |
| Classe(14) | VARCHAR | True |
| Nature(14) | INTEGER | True |
| Structure(14) | INTEGER | True |
| Omega(14) | DOUBLE | True |
| Armement(14) | VARCHAR | True |
| Omega armement(14) | DOUBLE | True |
| Branchement(14) | INTEGER | True |
| Isolateur(14) | VARCHAR | True |
| Ks(14) | DOUBLE | True |
| Nature sol(14) | VARCHAR | True |

## Database: `C:\Users\killi\Documents\0 - Playground\ERAS-MCP\artifacts\work\eras_mdb\enedis22_DGN__746ab9f2e721.mdb`

- ODBC driver: `Microsoft Access Driver (*.mdb, *.accdb)`
- pyodbc available: `True`
- Tables discovered: `0`

### Warnings

- ODBC schema read failed: 'utf-16-le' codec can't decode bytes in position 72-73: illegal UTF-16 surrogate

## Database: `C:\Users\killi\Documents\0 - Playground\ERAS-MCP\artifacts\work\eras_mdb\enedis22_DGN_sht__bee2f0356f5d.mdb`

- ODBC driver: `Microsoft Access Driver (*.mdb, *.accdb)`
- pyodbc available: `True`
- Tables discovered: `0`

### Warnings

- ODBC schema read failed: 'utf-16-le' codec can't decode bytes in position 72-73: illegal UTF-16 surrogate

## Database: `C:\Users\killi\Documents\0 - Playground\ERAS-MCP\artifacts\work\eras_mdb\ENEDIS23_DGN__b0d05f0db23e.mdb`

- ODBC driver: `Microsoft Access Driver (*.mdb, *.accdb)`
- pyodbc available: `True`
- Tables discovered: `0`

### Warnings

- ODBC schema read failed: 'utf-16-le' codec can't decode bytes in position 72-73: illegal UTF-16 surrogate

## Database: `C:\Users\killi\Documents\0 - Playground\ERAS-MCP\artifacts\work\eras_mdb\ENEDIS23_DGN_sht__a65309b5fae7.mdb`

- ODBC driver: `Microsoft Access Driver (*.mdb, *.accdb)`
- pyodbc available: `True`
- Tables discovered: `0`

### Warnings

- ODBC schema read failed: 'utf-16-le' codec can't decode bytes in position 72-73: illegal UTF-16 surrogate

## Database: `C:\Users\killi\Documents\0 - Playground\ERAS-MCP\artifacts\work\eras_mdb\enedis_DGN__35d2ebf4c831.mdb`

- ODBC driver: `Microsoft Access Driver (*.mdb, *.accdb)`
- pyodbc available: `True`
- Tables discovered: `0`

### Warnings

- ODBC schema read failed: 'utf-16-le' codec can't decode bytes in position 72-73: illegal UTF-16 surrogate

## Database: `C:\Users\killi\Documents\0 - Playground\ERAS-MCP\artifacts\work\eras_mdb\enedis_DGN_sht__1b03fd68d04a.mdb`

- ODBC driver: `Microsoft Access Driver (*.mdb, *.accdb)`
- pyodbc available: `True`
- Tables discovered: `0`

### Warnings

- ODBC schema read failed: 'utf-16-le' codec can't decode bytes in position 72-73: illegal UTF-16 surrogate

## Database: `C:\Users\killi\Documents\0 - Playground\ERAS-MCP\artifacts\work\eras_mdb\ERDFAER2012_DGN_sht__b1729750e426.mdb`

- ODBC driver: `Microsoft Access Driver (*.mdb, *.accdb)`
- pyodbc available: `True`
- Tables discovered: `0`

### Warnings

- ODBC schema read failed: 'utf-16-le' codec can't decode bytes in position 72-73: illegal UTF-16 surrogate

## Database: `C:\Users\killi\Documents\0 - Playground\ERAS-MCP\artifacts\work\eras_mdb\ERDFAER_DGN_sht__b1729750e426.mdb`

- ODBC driver: `Microsoft Access Driver (*.mdb, *.accdb)`
- pyodbc available: `True`
- Tables discovered: `0`

### Warnings

- ODBC schema read failed: 'utf-16-le' codec can't decode bytes in position 72-73: illegal UTF-16 surrogate

## Database: `C:\Users\killi\Documents\0 - Playground\ERAS-MCP\artifacts\work\eras_mdb\ERDFSOUT2012_DGN_sht__e55713b85369.mdb`

- ODBC driver: `Microsoft Access Driver (*.mdb, *.accdb)`
- pyodbc available: `True`
- Tables discovered: `0`

### Warnings

- ODBC schema read failed: 'utf-16-le' codec can't decode bytes in position 72-73: illegal UTF-16 surrogate

## Database: `C:\Users\killi\Documents\0 - Playground\ERAS-MCP\artifacts\work\eras_mdb\ERDFSOUT_DGN_sht__e55713b85369.mdb`

- ODBC driver: `Microsoft Access Driver (*.mdb, *.accdb)`
- pyodbc available: `True`
- Tables discovered: `0`

### Warnings

- ODBC schema read failed: 'utf-16-le' codec can't decode bytes in position 72-73: illegal UTF-16 surrogate

## Database: `C:\Users\killi\Documents\0 - Playground\ERAS-MCP\artifacts\work\eras_mdb\FTTH_DGN_sht__363622659586.mdb`

- ODBC driver: `Microsoft Access Driver (*.mdb, *.accdb)`
- pyodbc available: `True`
- Tables discovered: `0`

### Warnings

- ODBC schema read failed: 'utf-16-le' codec can't decode bytes in position 72-73: illegal UTF-16 surrogate

## Database: `C:\Users\killi\Documents\0 - Playground\ERAS-MCP\artifacts\work\eras_mdb\levels__83a4d02c5645.mdb`

- ODBC driver: `Microsoft Access Driver (*.mdb, *.accdb)`
- pyodbc available: `True`
- Tables discovered: `7`

### Table `cells`

- Row count: `0`
- Columns: `2`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| Nom | VARCHAR | True |
| Id | INTEGER | True |

### Table `Famille`

- Row count: `1`
- Columns: `3`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| FAM_CODE | COUNTER | False |
| FAM_NOM | VARCHAR | True |
| FAM_DESC | VARCHAR | True |

### Table `FiltreNiveau`

- Row count: `0`
- Columns: `5`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| idfiltre | COUNTER | False |
| parentid | INTEGER | True |
| idniveau | INTEGER | True |
| description | CHAR | True |
| Position | INTEGER | True |

### Table `fonts`

- Row count: `0`
- Columns: `3`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| Nom | CHAR | True |
| Id | INTEGER | True |
| Type | INTEGER | True |

### Table `levels`

- Row count: `0`
- Columns: `6`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| Id | INTEGER | True |
| Nom | VARCHAR | True |
| pos | INTEGER | True |
| Couleur | INTEGER | True |
| Style | VARCHAR | True |
| Epaisseur | INTEGER | True |

### Table `Print`

- Row count: `0`
- Columns: `7`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| PLT_CODE | COUNTER | False |
| PLT_NAME | VARCHAR | True |
| PLT_PLOT | VARCHAR | True |
| PLT_PRINTER | VARCHAR | True |
| PLT_FORMAT | VARCHAR | True |
| PLT_ORIENT | VARCHAR | True |
| PLT_DEFAULT | BIT | False |

### Table `version`

- Row count: `10`
- Columns: `3`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| Base | VARCHAR | True |
| Description | VARCHAR | True |
| Application | VARCHAR | True |

## Database: `C:\Users\killi\Documents\0 - Playground\ERAS-MCP\artifacts\work\eras_mdb\modele__7e34ea0aa355.mdb`

- ODBC driver: `Microsoft Access Driver (*.mdb, *.accdb)`
- pyodbc available: `True`
- Tables discovered: `0`

### Warnings

- ODBC schema read failed: 'utf-16-le' codec can't decode bytes in position 72-73: illegal UTF-16 surrogate

## Database: `C:\Users\killi\Documents\0 - Playground\ERAS-MCP\artifacts\work\eras_mdb\Modele_SIG__27dc1b587e20.mdb`

- ODBC driver: `Microsoft Access Driver (*.mdb, *.accdb)`
- pyodbc available: `True`
- Tables discovered: `14`

### Table `CABLEAER`

- Row count: `0`
- Columns: `3`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| MSLINK | COUNTER | False |
| MAPID | INTEGER | True |
| NOM | VARCHAR | True |

### Table `CANALISATION`

- Row count: `0`
- Columns: `4`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| MSLINK | COUNTER | False |
| MAPID | INTEGER | True |
| section | VARCHAR | True |
| Longueur | DOUBLE | True |

### Table `ELEMENT`

- Row count: `0`
- Columns: `3`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| MSLINK | COUNTER | False |
| MAPID | INTEGER | True |
| Nom | VARCHAR | True |

### Table `EQUIPEMENT`

- Row count: `0`
- Columns: `4`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| MSLINK | COUNTER | False |
| MAPID | INTEGER | True |
| REPERE | VARCHAR | True |
| NOM | VARCHAR | True |

### Table `FEATURE`

- Row count: `0`
- Columns: `11`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| MSLINK | INTEGER | True |
| FCODE | VARCHAR | True |
| FNAME | VARCHAR | True |
| CATEGORY | INTEGER | True |
| TABLENAME | VARCHAR | True |
| FTYPE | INTEGER | True |
| FLEVEL | INTEGER | True |
| FSTYLE | INTEGER | True |
| FWEIGHT | INTEGER | True |
| FCOLOR | INTEGER | True |
| DIGCMD | VARCHAR | True |

### Table `INPUTFORMS`

- Row count: `0`
- Columns: `7`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| FORMID | INTEGER | True |
| FORMTITLE | VARCHAR | True |
| DELETE_FLAG | INTEGER | True |
| INSERT_FLAG | INTEGER | True |
| APP_TOLOAD | VARCHAR | True |
| RSC_FILENAME | VARCHAR | True |
| PDM_ID1 | INTEGER | True |

### Table `INPUTGADGETS`

- Row count: `0`
- Columns: `17`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| FORMID | INTEGER | True |
| GADGETID | INTEGER | True |
| COLUMN_PROMPT | VARCHAR | True |
| COLUMNNAME | VARCHAR | True |
| VALUE_REQUIRED | INTEGER | True |
| DISPLAYONLY | INTEGER | True |
| WITHLIST | INTEGER | True |
| SELECTSTMT | VARCHAR | True |
| VISIBLECHARS | INTEGER | True |
| MAXCHARS | INTEGER | True |
| FIELDTYPE | INTEGER | True |
| GADGET_FORMAT | VARCHAR | True |
| SUB_FORM | INTEGER | True |
| SUB_REF_ID | INTEGER | True |
| COLUMN_ID | INTEGER | True |
| GADGET_PICTURE | VARCHAR | True |
| SELECTSTMTID | INTEGER | True |

### Table `Lien`

- Row count: `0`
- Columns: `7`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| IDLIEN | COUNTER | False |
| IDPERE | INTEGER | True |
| IDFILS | INTEGER | True |
| ChampsFils | VARCHAR | True |
| ChampsPere | VARCHAR | True |
| IdValeurFils | INTEGER | True |
| IdValeurPere | INTEGER | True |

### Table `maps`

- Row count: `0`
- Columns: `3`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| mslink | COUNTER | False |
| category | INTEGER | True |
| mapname | VARCHAR | True |

### Table `MSCATALOG`

- Row count: `15`
- Columns: `9`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| TABLENAME | VARCHAR | True |
| ENTITYNUM | INTEGER | True |
| NEXTOCC | INTEGER | True |
| SCREENFORM | VARCHAR | True |
| REPORTTABLE | VARCHAR | True |
| SQLREVIEW | VARCHAR | True |
| FENCEFILTER | VARCHAR | True |
| DASTABLE | VARCHAR | True |
| TABLETYPE | VARCHAR | True |

### Table `POTEAU`

- Row count: `0`
- Columns: `4`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| MSLINK | COUNTER | False |
| MAPID | INTEGER | True |
| REPERE | VARCHAR | True |
| NOM | VARCHAR | True |

### Table `TblDocument`

- Row count: `6`
- Columns: `7`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| IdDocument | COUNTER | False |
| IdBdElement | INTEGER | True |
| NomFichier | VARCHAR | True |
| TypeFichier | INTEGER | True |
| Observation | VARCHAR | True |
| DateCreation | DATETIME | True |
| Parent | INTEGER | True |

### Table `TblTypeDocument`

- Row count: `6`
- Columns: `3`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| IdTypeDocument | COUNTER | False |
| Libelle | VARCHAR | True |
| ExtensionFichier | CHAR | True |

### Table `VALDEFAUT`

- Row count: `0`
- Columns: `5`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| FEATUREID | DOUBLE | True |
| FNAME | VARCHAR | True |
| TABLENAME | VARCHAR | True |
| COLUMN_NAME | VARCHAR | True |
| VALUE | VARCHAR | True |

## Database: `C:\Users\killi\Documents\0 - Playground\ERAS-MCP\artifacts\work\eras_mdb\modeleAff__07f5ffa46fce.mdb`

- ODBC driver: `Microsoft Access Driver (*.mdb, *.accdb)`
- pyodbc available: `True`
- Tables discovered: `0`

### Warnings

- ODBC schema read failed: 'utf-16-le' codec can't decode bytes in position 72-73: illegal UTF-16 surrogate

## Database: `C:\Users\killi\Documents\0 - Playground\ERAS-MCP\artifacts\work\eras_mdb\modeleExportCaneco__1c88aec901f6.mdb`

- ODBC driver: `Microsoft Access Driver (*.mdb, *.accdb)`
- pyodbc available: `True`
- Tables discovered: `2`

### Table `Infos`

- Row count: `0`
- Columns: `3`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| Designation | VARCHAR | True |
| Valeur | VARCHAR | True |
| Commentaire | VARCHAR | True |

### Table `PtLumineux`

- Row count: `0`
- Columns: `14`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| Repere_debut | VARCHAR | True |
| Type_de_repere_debut | INTEGER | True |
| Repere_fin | VARCHAR | True |
| Type_de_repere_fin | INTEGER | True |
| Longueur_canalisation | REAL | True |
| Surlongueur_debut | REAL | True |
| Surlongueur_fin | REAL | True |
| Famille_de_cable | INTEGER | True |
| Mode_de_pose | INTEGER | True |
| Longueur_sous_fourreau | REAL | True |
| Type_de_cable | INTEGER | True |
| Nature_cable | VARCHAR | True |
| Nombre_foyer | INTEGER | True |
| Section_cable | VARCHAR | True |

## Database: `C:\Users\killi\Documents\0 - Playground\ERAS-MCP\artifacts\work\eras_mdb\modelevide__1606f9b0a3b6.mdb`

- ODBC driver: `Microsoft Access Driver (*.mdb, *.accdb)`
- pyodbc available: `True`
- Tables discovered: `0`

### Warnings

- ODBC schema read failed: 'utf-16-le' codec can't decode bytes in position 72-73: illegal UTF-16 surrogate

## Database: `C:\Users\killi\Documents\0 - Playground\ERAS-MCP\artifacts\work\eras_mdb\Sheet__5f080916af57.mdb`

- ODBC driver: `Microsoft Access Driver (*.mdb, *.accdb)`
- pyodbc available: `True`
- Tables discovered: `0`

### Warnings

- ODBC schema read failed: 'utf-16-le' codec can't decode bytes in position 72-73: illegal UTF-16 surrogate

## Database: `C:\Users\killi\Documents\0 - Playground\ERAS-MCP\artifacts\work\eras_mdb\Atlog__13e47fb7fde8.mdb`

- ODBC driver: `Microsoft Access Driver (*.mdb, *.accdb)`
- pyodbc available: `True`
- Tables discovered: `6`

### Table `cells`

- Row count: `139`
- Columns: `2`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| Nom | VARCHAR | True |
| Id | INTEGER | True |

### Table `Famille`

- Row count: `3`
- Columns: `3`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| FAM_CODE | COUNTER | False |
| FAM_NOM | VARCHAR | True |
| FAM_DESC | VARCHAR | True |

### Table `FiltreNiveau`

- Row count: `923`
- Columns: `5`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| idfiltre | COUNTER | False |
| parentid | INTEGER | True |
| idniveau | INTEGER | True |
| description | CHAR | True |
| Position | INTEGER | True |

### Table `fonts`

- Row count: `26`
- Columns: `3`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| Nom | CHAR | True |
| Id | INTEGER | True |
| Type | INTEGER | True |

### Table `levels`

- Row count: `562`
- Columns: `6`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| Id | INTEGER | True |
| nom | VARCHAR | True |
| pos | INTEGER | True |
| Couleur | INTEGER | True |
| Style | VARCHAR | True |
| Epaisseur | INTEGER | True |

### Table `version`

- Row count: `12`
- Columns: `3`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| Base | VARCHAR | True |
| Description | VARCHAR | True |
| Application | VARCHAR | True |

## Database: `C:\Users\killi\Documents\0 - Playground\ERAS-MCP\artifacts\work\eras_mdb\Atlog___eb7dc3b3b1b7.mdb`

- ODBC driver: `Microsoft Access Driver (*.mdb, *.accdb)`
- pyodbc available: `True`
- Tables discovered: `0`

### Warnings

- ODBC schema read failed: 'utf-16-le' codec can't decode bytes in position 72-73: illegal UTF-16 surrogate

## Database: `C:\Users\killi\Documents\0 - Playground\ERAS-MCP\artifacts\work\eras_mdb\Modele_SIG__27dc1b587e20.mdb`

- ODBC driver: `Microsoft Access Driver (*.mdb, *.accdb)`
- pyodbc available: `True`
- Tables discovered: `14`

### Table `CABLEAER`

- Row count: `0`
- Columns: `3`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| MSLINK | COUNTER | False |
| MAPID | INTEGER | True |
| NOM | VARCHAR | True |

### Table `CANALISATION`

- Row count: `0`
- Columns: `4`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| MSLINK | COUNTER | False |
| MAPID | INTEGER | True |
| section | VARCHAR | True |
| Longueur | DOUBLE | True |

### Table `ELEMENT`

- Row count: `0`
- Columns: `3`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| MSLINK | COUNTER | False |
| MAPID | INTEGER | True |
| Nom | VARCHAR | True |

### Table `EQUIPEMENT`

- Row count: `0`
- Columns: `4`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| MSLINK | COUNTER | False |
| MAPID | INTEGER | True |
| REPERE | VARCHAR | True |
| NOM | VARCHAR | True |

### Table `FEATURE`

- Row count: `0`
- Columns: `11`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| MSLINK | INTEGER | True |
| FCODE | VARCHAR | True |
| FNAME | VARCHAR | True |
| CATEGORY | INTEGER | True |
| TABLENAME | VARCHAR | True |
| FTYPE | INTEGER | True |
| FLEVEL | INTEGER | True |
| FSTYLE | INTEGER | True |
| FWEIGHT | INTEGER | True |
| FCOLOR | INTEGER | True |
| DIGCMD | VARCHAR | True |

### Table `INPUTFORMS`

- Row count: `0`
- Columns: `7`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| FORMID | INTEGER | True |
| FORMTITLE | VARCHAR | True |
| DELETE_FLAG | INTEGER | True |
| INSERT_FLAG | INTEGER | True |
| APP_TOLOAD | VARCHAR | True |
| RSC_FILENAME | VARCHAR | True |
| PDM_ID1 | INTEGER | True |

### Table `INPUTGADGETS`

- Row count: `0`
- Columns: `17`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| FORMID | INTEGER | True |
| GADGETID | INTEGER | True |
| COLUMN_PROMPT | VARCHAR | True |
| COLUMNNAME | VARCHAR | True |
| VALUE_REQUIRED | INTEGER | True |
| DISPLAYONLY | INTEGER | True |
| WITHLIST | INTEGER | True |
| SELECTSTMT | VARCHAR | True |
| VISIBLECHARS | INTEGER | True |
| MAXCHARS | INTEGER | True |
| FIELDTYPE | INTEGER | True |
| GADGET_FORMAT | VARCHAR | True |
| SUB_FORM | INTEGER | True |
| SUB_REF_ID | INTEGER | True |
| COLUMN_ID | INTEGER | True |
| GADGET_PICTURE | VARCHAR | True |
| SELECTSTMTID | INTEGER | True |

### Table `Lien`

- Row count: `0`
- Columns: `7`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| IDLIEN | COUNTER | False |
| IDPERE | INTEGER | True |
| IDFILS | INTEGER | True |
| ChampsFils | VARCHAR | True |
| ChampsPere | VARCHAR | True |
| IdValeurFils | INTEGER | True |
| IdValeurPere | INTEGER | True |

### Table `maps`

- Row count: `0`
- Columns: `3`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| mslink | COUNTER | False |
| category | INTEGER | True |
| mapname | VARCHAR | True |

### Table `MSCATALOG`

- Row count: `15`
- Columns: `9`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| TABLENAME | VARCHAR | True |
| ENTITYNUM | INTEGER | True |
| NEXTOCC | INTEGER | True |
| SCREENFORM | VARCHAR | True |
| REPORTTABLE | VARCHAR | True |
| SQLREVIEW | VARCHAR | True |
| FENCEFILTER | VARCHAR | True |
| DASTABLE | VARCHAR | True |
| TABLETYPE | VARCHAR | True |

### Table `POTEAU`

- Row count: `0`
- Columns: `4`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| MSLINK | COUNTER | False |
| MAPID | INTEGER | True |
| REPERE | VARCHAR | True |
| NOM | VARCHAR | True |

### Table `TblDocument`

- Row count: `6`
- Columns: `7`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| IdDocument | COUNTER | False |
| IdBdElement | INTEGER | True |
| NomFichier | VARCHAR | True |
| TypeFichier | INTEGER | True |
| Observation | VARCHAR | True |
| DateCreation | DATETIME | True |
| Parent | INTEGER | True |

### Table `TblTypeDocument`

- Row count: `6`
- Columns: `3`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| IdTypeDocument | COUNTER | False |
| Libelle | VARCHAR | True |
| ExtensionFichier | CHAR | True |

### Table `VALDEFAUT`

- Row count: `0`
- Columns: `5`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| FEATUREID | DOUBLE | True |
| FNAME | VARCHAR | True |
| TABLENAME | VARCHAR | True |
| COLUMN_NAME | VARCHAR | True |
| VALUE | VARCHAR | True |

## Database: `C:\Users\killi\Documents\0 - Playground\ERAS-MCP\artifacts\work\eras_mdb\c11_201__93b63352fc8c.mdb`

- ODBC driver: `Microsoft Access Driver (*.mdb, *.accdb)`
- pyodbc available: `True`
- Tables discovered: `17`

### Table `CalculPart`

- Row count: `20`
- Columns: `95`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| Nom | VARCHAR | True |
| Type Ligne(0) | SMALLINT | True |
| Type Ligne(1) | SMALLINT | True |
| Type Ligne(2) | SMALLINT | True |
| Type Ligne(3) | SMALLINT | True |
| Calcul en GD | SMALLINT | True |
| Application de givre en GD(0) | SMALLINT | True |
| Application de givre en GD(1) | SMALLINT | True |
| Application de givre en GD(2) | SMALLINT | True |
| Application de givre en GD(3) | SMALLINT | True |
| Présence ligne(00) | SMALLINT | True |
| Coef hypothèse(00) | REAL | True |
| Présence ligne(01) | SMALLINT | True |
| Coef hypothèse(01) | REAL | True |
| Présence ligne(02) | SMALLINT | True |
| Coef hypothèse(02) | REAL | True |
| Présence ligne(03) | SMALLINT | True |
| Coef hypothèse(03) | REAL | True |
| Présence ligne(10) | SMALLINT | True |
| Coef hypothèse(10) | REAL | True |
| Présence ligne(11) | SMALLINT | True |
| Coef hypothèse(11) | REAL | True |
| Présence ligne(12) | SMALLINT | True |
| Coef hypothèse(12) | REAL | True |
| Présence ligne(13) | SMALLINT | True |
| Coef hypothèse(13) | REAL | True |
| Présence ligne(20) | SMALLINT | True |
| Coef hypothèse(20) | REAL | True |
| Présence ligne(21) | SMALLINT | True |
| Coef hypothèse(21) | REAL | True |
| Présence ligne(22) | SMALLINT | True |
| Coef hypothèse(22) | REAL | True |
| Présence ligne(23) | SMALLINT | True |
| Coef hypothèse(23) | REAL | True |
| Présence ligne(30) | SMALLINT | True |
| Coef hypothèse(30) | REAL | True |
| Présence ligne(31) | SMALLINT | True |
| Coef hypothèse(31) | REAL | True |
| Présence ligne(32) | SMALLINT | True |
| Coef hypothèse(32) | REAL | True |
| Présence ligne(33) | SMALLINT | True |
| Coef hypothèse(33) | REAL | True |
| Présence ligne(40) | SMALLINT | True |
| Coef hypothèse(40) | REAL | True |
| Présence ligne(41) | SMALLINT | True |
| Coef hypothèse(41) | REAL | True |
| Présence ligne(42) | SMALLINT | True |
| Coef hypothèse(42) | REAL | True |
| Présence ligne(43) | SMALLINT | True |
| Coef hypothèse(43) | REAL | True |
| Présence ligne(50) | SMALLINT | True |
| Coef hypothèse(50) | REAL | True |
| Présence ligne(51) | SMALLINT | True |
| Coef hypothèse(51) | REAL | True |
| Présence ligne(52) | SMALLINT | True |
| Coef hypothèse(52) | REAL | True |
| Présence ligne(53) | SMALLINT | True |
| Coef hypothèse(53) | REAL | True |
| Présence ligne(60) | SMALLINT | True |
| Coef hypothèse(60) | REAL | True |
| Présence ligne(61) | SMALLINT | True |
| Coef hypothèse(61) | REAL | True |
| Présence ligne(62) | SMALLINT | True |
| Coef hypothèse(62) | REAL | True |
| Présence ligne(63) | SMALLINT | True |
| Coef hypothèse(63) | REAL | True |
| Présence ligne(70) | SMALLINT | True |
| Coef hypothèse(70) | REAL | True |
| Présence ligne(71) | SMALLINT | True |
| Coef hypothèse(71) | REAL | True |
| Présence ligne(72) | SMALLINT | True |
| Coef hypothèse(72) | REAL | True |
| Présence ligne(73) | SMALLINT | True |
| Coef hypothèse(73) | REAL | True |
| Présence ligne(80) | SMALLINT | True |
| Coef hypothèse(80) | REAL | True |
| Présence ligne(81) | SMALLINT | True |
| Coef hypothèse(81) | REAL | True |
| Présence ligne(82) | SMALLINT | True |
| Coef hypothèse(82) | REAL | True |
| Présence ligne(83) | SMALLINT | True |
| Coef hypothèse(83) | REAL | True |
| Présence ligne(90) | SMALLINT | True |
| Coef hypothèse(90) | REAL | True |
| Présence ligne(91) | SMALLINT | True |
| Coef hypothèse(91) | REAL | True |
| Présence ligne(92) | SMALLINT | True |
| Coef hypothèse(92) | REAL | True |
| Présence ligne(93) | SMALLINT | True |
| Coef hypothèse(93) | REAL | True |
| Hypothèse(0) | VARCHAR | True |
| Hypothèse(1) | VARCHAR | True |
| Hypothèse(2) | VARCHAR | True |
| Hypothèse(3) | VARCHAR | True |
| Numéro | SMALLINT | True |

### Table `Classe`

- Row count: `39`
- Columns: `23`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| Nom | VARCHAR | True |
| Nature | SMALLINT | True |
| Structure | SMALLINT | True |
| Coef Tau | REAL | True |
| Coef Tau en DP | REAL | True |
| Recherche | SMALLINT | True |
| Effort branchement(0) | REAL | True |
| Effort branchement(1) | REAL | True |
| Effort H61 | REAL | True |
| Forme | SMALLINT | True |
| Diagramme effort | SMALLINT | True |
| Cellule BP | VARCHAR | True |
| Fichier graphique | VARCHAR | True |
| Caché | SMALLINT | True |
| Element de base | SMALLINT | True |
| Distance torsion monophasé | REAL | True |
| Distance torsion triphasé | REAL | True |
| Haubanage | SMALLINT | True |
| Assemblage | SMALLINT | True |
| Ecart | REAL | True |
| Description | VARCHAR | True |
| Symetrique | VARCHAR | True |
| Effort Min si H61 | REAL | True |

### Table `Commune`

- Row count: `36211`
- Columns: `7`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| Id | COUNTER | False |
| Dep | VARCHAR | True |
| Insee | VARCHAR | True |
| Nom | VARCHAR | True |
| ZoneVent | REAL | True |
| ZoneGivre | REAL | True |
| ZoneNeige | REAL | True |

### Table `Configuration`

- Row count: `1`
- Columns: `148`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| Nom | VARCHAR | True |
| Libellé | VARCHAR | True |
| Technique nord-américaine | SMALLINT | True |
| Vent sur supports BT | SMALLINT | True |
| Hypothèse DP sur supports bois | SMALLINT | True |
| Installation de DAC | SMALLINT | True |
| Affichage coef travail | SMALLINT | True |
| Option vérification | SMALLINT | True |
| Affichage panneau retournement | SMALLINT | True |
| Vent sur supports(0) | REAL | True |
| Vent sur supports(1) | REAL | True |
| Vent sur supports(2) | REAL | True |
| Vent sur supports(3) | REAL | True |
| Groupe hypothèses | VARCHAR | True |
| Température(0) | REAL | True |
| Température(1) | REAL | True |
| Température(2) | REAL | True |
| Température(3) | REAL | True |
| Température(4) | REAL | True |
| Température(5) | REAL | True |
| Température(6) | REAL | True |
| Coef écartement(0) | VARCHAR | True |
| Coef écartement(1) | VARCHAR | True |
| Coef écartement(2) | VARCHAR | True |
| Ks normal | REAL | True |
| Ks sécurité | REAL | True |
| a(0) | REAL | True |
| b(0) | REAL | True |
| a(1) | REAL | True |
| b(1) | REAL | True |
| a(2) | REAL | True |
| b(2) | REAL | True |
| a(3) | REAL | True |
| b(3) | REAL | True |
| a(4) | REAL | True |
| b(4) | REAL | True |
| a(5) | REAL | True |
| b(5) | REAL | True |
| a(6) | REAL | True |
| b(6) | REAL | True |
| a(7) | REAL | True |
| b(7) | REAL | True |
| a(8) | REAL | True |
| b(8) | REAL | True |
| a(9) | REAL | True |
| b(9) | REAL | True |
| a(10) | REAL | True |
| b(10) | REAL | True |
| a(11) | REAL | True |
| b(11) | REAL | True |
| a(12) | REAL | True |
| b(12) | REAL | True |
| a(13) | REAL | True |
| b(13) | REAL | True |
| a(14) | REAL | True |
| b(14) | REAL | True |
| a(15) | REAL | True |
| b(15) | REAL | True |
| Degré Celsius | SMALLINT | True |
| Grade | SMALLINT | True |
| Sens trigonométrique | SMALLINT | True |
| Valeur de tension(0) | REAL | True |
| Valeur de tension(1) | REAL | True |
| Support-type | VARCHAR | True |
| Sortie récapitulatif word 6 | SMALLINT | True |
| Protection | VARCHAR | True |
| Angle de profil limite | REAL | True |
| Hypothèse standard chainettes | VARCHAR | True |
| Hypothèse complémentaire chainettes | VARCHAR | True |
| Fichier obstacles | VARCHAR | True |
| Pression pour zone vent fort | REAL | True |
| Effort référence fouille | REAL | True |
| Libellé de tension(0) | VARCHAR | True |
| Libellé de tension(1) | VARCHAR | True |
| Libellé de tension(2) | VARCHAR | True |
| Libellé de tension(3) | VARCHAR | True |
| Hypo de surcharge pour définition conducteur(0) | VARCHAR | True |
| Hypo de surcharge pour définition conducteur(1) | VARCHAR | True |
| Hypo de surcharge pour définition conducteur(2) | VARCHAR | True |
| Hypo de surcharge pour définition conducteur(3) | VARCHAR | True |
| Valeur de tension par défaut(0) | REAL | True |
| Valeur de tension par défaut(1) | REAL | True |
| Valeur de tension par défaut(2) | REAL | True |
| Valeur de tension par défaut(3) | REAL | True |
| Distance min croisement(0) | REAL | True |
| Voltage croisement surplomb(0) | SMALLINT | True |
| Voltage croisement surplombee(0) | SMALLINT | True |
| Distance min croisement(1) | REAL | True |
| Voltage croisement surplomb(1) | SMALLINT | True |
| Voltage croisement surplombee(1) | SMALLINT | True |
| Distance min croisement(2) | REAL | True |
| Voltage croisement surplomb(2) | SMALLINT | True |
| Voltage croisement surplombee(2) | SMALLINT | True |
| Distance min croisement(3) | REAL | True |
| Voltage croisement surplomb(3) | SMALLINT | True |
| Voltage croisement surplombee(3) | SMALLINT | True |
| Distance min croisement(4) | REAL | True |
| Voltage croisement surplomb(4) | SMALLINT | True |
| Voltage croisement surplombee(4) | SMALLINT | True |
| Distance min croisement(5) | REAL | True |
| Voltage croisement surplomb(5) | SMALLINT | True |
| Voltage croisement surplombee(5) | SMALLINT | True |
| Famille hypothèse(0) | VARCHAR | True |
| Famille hypothèse(1) | VARCHAR | True |
| Famille hypothèse(2) | VARCHAR | True |
| Famille hypothèse(3) | VARCHAR | True |
| Famille hypothèse(4) | VARCHAR | True |
| Famille hypothèse(5) | VARCHAR | True |
| Famille hypothèse(6) | VARCHAR | True |
| Famille hypothèse(7) | VARCHAR | True |
| Famille hypothèse(8) | VARCHAR | True |
| Famille hypothèse(9) | VARCHAR | True |
| Famille hypothèse liée(0) | VARCHAR | True |
| Famille hypothèse liée(1) | VARCHAR | True |
| Famille hypothèse liée(2) | VARCHAR | True |
| Famille hypothèse liée(3) | VARCHAR | True |
| Famille hypothèse liée(4) | VARCHAR | True |
| Famille hypothèse liée(5) | VARCHAR | True |
| Famille hypothèse liée(6) | VARCHAR | True |
| Famille hypothèse liée(7) | VARCHAR | True |
| Famille hypothèse liée(8) | VARCHAR | True |
| Famille hypothèse liée(9) | VARCHAR | True |
| Température de réglage(0) | REAL | True |
| Température de réglage(1) | REAL | True |
| Température de réglage(2) | REAL | True |
| Température de réglage(3) | REAL | True |
| Température de réglage(4) | REAL | True |
| Température de réglage(5) | REAL | True |
| Température de réglage(6) | REAL | True |
| Température de réglage(7) | REAL | True |
| Température de réglage(8) | REAL | True |
| Température de réglage(9) | REAL | True |
| Type mécanique(0) | VARCHAR | True |
| Type mécanique(1) | VARCHAR | True |
| Type mécanique(2) | VARCHAR | True |
| Distance min fouille portique | REAL | True |
| Coef distance min croisement | REAL | True |
| Option croisement francais | REAL | True |
| Coef dépassemement portée max | REAL | True |
| Nature autre | VARCHAR | True |
| Nature autre réduit | VARCHAR | True |
| Hypothèse VIB en nu | SMALLINT | True |
| Hypothèse VIB en torsadé | SMALLINT | True |
| Compression supports bois | SMALLINT | True |
| Type haubanage selon orientation | SMALLINT | True |
| Lignes TV avec HTA | SMALLINT | True |
| Version | REAL | True |
| optCommunes | SMALLINT | True |

### Table `Configuration(suite)`

- Row count: `1`
- Columns: `38`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| Sigma(0) | REAL | True |
| Sigma(1) | REAL | True |
| Sigma(2) | REAL | True |
| Sigma(3) | REAL | True |
| Sigma(4) | REAL | True |
| Sigma(5) | REAL | True |
| Sigma(6) | REAL | True |
| Sigma(7) | REAL | True |
| Sigma(8) | REAL | True |
| Sigma(9) | REAL | True |
| Sigma(10) | REAL | True |
| Sigma(11) | REAL | True |
| Sigma(12) | REAL | True |
| Sigma(13) | REAL | True |
| Sigma(14) | REAL | True |
| Sigma(15) | REAL | True |
| Sigma(16) | REAL | True |
| Sigma(17) | REAL | True |
| Sigma(18) | REAL | True |
| Sigma(19) | REAL | True |
| Sigma(20) | REAL | True |
| Sigma(21) | REAL | True |
| Sigma(22) | REAL | True |
| Sigma(23) | REAL | True |
| Sigma(24) | REAL | True |
| Sigma(25) | REAL | True |
| Pression Max Terre | REAL | True |
| Masse Volumique Terre | REAL | True |
| Masse Volumique Béton | REAL | True |
| Temps enregistrement | REAL | True |
| Enregistrement activé | SMALLINT | True |
| Association DAC-Canton | SMALLINT | True |
| VoltMinCroise1 | DOUBLE | True |
| VoltMinCroise2 | DOUBLE | True |
| VoltMinCroise3 | DOUBLE | True |
| TempMinCroise1 | DOUBLE | True |
| TempMinCroise2 | DOUBLE | True |
| TempMinCroise3 | DOUBLE | True |

### Table `Câble`

- Row count: `576`
- Columns: `90`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| Nom | VARCHAR | True |
| Volt | VARCHAR | True |
| Type | SMALLINT | True |
| Section réelle | REAL | True |
| Diamètre | REAL | True |
| Masse linéique | REAL | True |
| Module d'Young | REAL | True |
| Coef de dilatation | REAL | True |
| Charge de rupture nominale | REAL | True |
| Portée maximale suspendu | REAL | True |
| Portée moyenne conseillée suspendu | REAL | True |
| Paramètre conseillé suspendu | REAL | True |
| Portée maximale rigide écart | REAL | True |
| Portée moyenne conseillée rigide écart | REAL | True |
| Tension conseillée rigide écart | REAL | True |
| Portée maximale rigide agglo | REAL | True |
| Portée moyenne conseillée rigide agglo | REAL | True |
| Tension conseillée rigide agglo | REAL | True |
| Portée maximale suspendu ZVF | REAL | True |
| Portée moyenne conseillée suspendu ZVF | REAL | True |
| Paramètre conseillé suspendu ZVF | REAL | True |
| Portée maximale rigide écart ZVF | REAL | True |
| Portée moyenne conseillée rigide écart ZVF | REAL | True |
| Tension conseillée rigide écart ZVF | REAL | True |
| Portée maximale rigide agglo ZVF | REAL | True |
| Portée moyenne conseillée rigide agglo ZVF | REAL | True |
| Tension conseillée rigide agglo ZVF | REAL | True |
| Caché | SMALLINT | True |
| Element de base | SMALLINT | True |
| Portée max sus 1 | REAL | True |
| Portée moyenne conseillée sus 1 | REAL | True |
| Portée moyenne conseillée sus 2 | REAL | True |
| Portée moyenne conseillée sus 3 | REAL | True |
| Portée max sus 2 | REAL | True |
| Portée max sus 3 | REAL | True |
| Paramètre conseillé sus 1 | REAL | True |
| Paramètre conseillé sus 2 | REAL | True |
| Paramètre conseillé sus 3 | REAL | True |
| Portée max sus ZVF 1 | REAL | True |
| Portée max sus ZVF 2 | REAL | True |
| Portée max sus ZVF 3 | REAL | True |
| Portée moyenne conseillée sus ZVF 1 | REAL | True |
| Portée moyenne conseillée sus ZVF 2 | REAL | True |
| Portée moyenne conseillée sus ZVF 3 | REAL | True |
| Paramètre conseillé sus ZVF 1 | REAL | True |
| Paramètre conseillé sus ZVF 2 | REAL | True |
| Paramètre conseillé sus ZVF 3 | REAL | True |
| Portée max rig écart 1 | REAL | True |
| Portée max rig écart 2 | REAL | True |
| Portée max rig écart 3 | REAL | True |
| Portée max rig écart ZVF 1 | REAL | True |
| Portée max rig écart ZVF 2 | REAL | True |
| Portée max rig écart ZVF 3 | REAL | True |
| Portée max rig agglo 1 | REAL | True |
| Portée max rig agglo 2 | REAL | True |
| Portée max rig agglo 3 | REAL | True |
| Portée max rig agglo ZVF 1 | REAL | True |
| Portée max rig agglo ZVF 2 | REAL | True |
| Portée max rig agglo ZVF 3 | REAL | True |
| Portée moy conseillée rig écart 1 | REAL | True |
| Portée moy conseillée rig écart 2 | REAL | True |
| Portée moy conseillée rig écart 3 | REAL | True |
| Portée moy conseillée rig écart ZVF 1 | REAL | True |
| Portée moy conseillée rig écart ZVF 2 | REAL | True |
| Portée moy conseillée rig écart ZVF 3 | REAL | True |
| Portée moy conseillée rig agglo 1 | REAL | True |
| Portée moy conseillée rig agglo 2 | REAL | True |
| Portée moy conseillée rig agglo 3 | REAL | True |
| Portée moy conseillée rig agglo ZVF 1 | REAL | True |
| Portée moy conseillée rig agglo ZVF 2 | REAL | True |
| Portée moy conseillée rig agglo ZVF 3 | REAL | True |
| Tension conseillée rig écart 1 | REAL | True |
| Tension conseillée rig écart 2 | REAL | True |
| Tension conseillée rig écart 3 | REAL | True |
| Tension conseillée rig écart ZVF 1 | REAL | True |
| Tension conseillée rig écart ZVF 2 | REAL | True |
| Tension conseillée rig écart ZVF 3 | REAL | True |
| Tension conseillée rig agglo 1 | REAL | True |
| Tension conseillée rig agglo 2 | REAL | True |
| Tension conseillée rig agglo 3 | REAL | True |
| Tension conseillée rig agglo ZVF 1 | REAL | True |
| Tension conseillée rig agglo ZVF 2 | REAL | True |
| Tension conseillée rig agglo ZVF 3 | REAL | True |
| Limite vibration | REAL | True |
| Gamme de tension | SMALLINT | True |
| Sigma(0) | REAL | True |
| Sigma(1) | REAL | True |
| Valeur | REAL | True |
| AncienNom | VARCHAR | True |
| Description | VARCHAR | True |

### Table `Dac`

- Row count: `22`
- Columns: `8`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| Nom | VARCHAR | True |
| Gamme | VARCHAR | True |
| Effort ruine | REAL | True |
| Longueur de détente | REAL | True |
| Caché | SMALLINT | True |
| Element de base | SMALLINT | True |
| Effort déclenchement | REAL | True |
| Valeur | REAL | True |

### Table `Equipement`

- Row count: `6`
- Columns: `10`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| Nom | VARCHAR | True |
| Effort forfaitaire | REAL | True |
| Décalage armement(0) | REAL | True |
| Décalage armement(1) | REAL | True |
| Décalage armement(2) | REAL | True |
| Décalage armement(3) | REAL | True |
| Elément de base | SMALLINT | True |
| Caché | SMALLINT | True |
| Description | VARCHAR | True |
| Valeur | REAL | True |

### Table `Famille armement`

- Row count: `39`
- Columns: `21`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| Famille | VARCHAR | True |
| Technique | SMALLINT | True |
| Nb fils | SMALLINT | True |
| Kc | REAL | True |
| Angle piquetage maxi | REAL | True |
| Caché | SMALLINT | True |
| Element de base | SMALLINT | True |
| Kc rigide | REAL | True |
| Diagramme effort | SMALLINT | True |
| Tronqué | SMALLINT | True |
| Gamme de tension | SMALLINT | True |
| Conducteur par défaut | VARCHAR | True |
| Tension saisie | SMALLINT | True |
| Neutre par défaut | VARCHAR | True |
| Décalage neutre | REAL | True |
| Kc neutre | REAL | True |
| Option type mécanique | SMALLINT | True |
| Fichier graphique | VARCHAR | True |
| Nom réduit défaut | VARCHAR | True |
| Type NV | SMALLINT | True |
| Fusible | INTEGER | True |

### Table `Groupe d'hypothèses`

- Row count: `7`
- Columns: `10`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| Nom | VARCHAR | True |
| Description | VARCHAR | True |
| Hypo(1) | VARCHAR | True |
| Hypo(2) | VARCHAR | True |
| Hypo(3) | VARCHAR | True |
| Hypo(0) | VARCHAR | True |
| Hypo(4) | VARCHAR | True |
| Hypo(5) | VARCHAR | True |
| Hypo(6) | VARCHAR | True |
| Hypo(7) | VARCHAR | True |

### Table `Hypothèse`

- Row count: `57`
- Columns: `19`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| Nom | VARCHAR | True |
| Volt | VARCHAR | True |
| Description | VARCHAR | True |
| Température | REAL | True |
| Pression de Vent conducteurs | REAL | True |
| Pression de Vent surfaces planes | REAL | True |
| Pression de Vent surfaces cylindriques | REAL | True |
| Pression de Vent surfaces polygonales | REAL | True |
| Masse de givre maxi | REAL | True |
| Masse de givre mini | REAL | True |
| Epaisseur de givre maxi | REAL | True |
| Epaisseur de givre mini | REAL | True |
| Kz | REAL | True |
| Caché | SMALLINT | True |
| Element de base | SMALLINT | True |
| Gamme de tension | SMALLINT | True |
| Utilisation | SMALLINT | True |
| Densité de givre | REAL | True |
| Pression de Vent surfaces autres | REAL | True |

### Table `Isolateur`

- Row count: `19`
- Columns: `28`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| Nom complet | VARCHAR | True |
| Type | VARCHAR | True |
| Effort ruine | REAL | True |
| Longueur chaîne | REAL | True |
| Poids chaîne | REAL | True |
| Tangente max | REAL | True |
| Tension | REAL | True |
| Caché | SMALLINT | True |
| Element de base | SMALLINT | True |
| Famille armement(0) | VARCHAR | True |
| Famille armement(1) | VARCHAR | True |
| Famille armement(2) | VARCHAR | True |
| Famille armement(3) | VARCHAR | True |
| Famille armement(4) | VARCHAR | True |
| Famille armement(5) | VARCHAR | True |
| Famille armement(6) | VARCHAR | True |
| Famille armement(7) | VARCHAR | True |
| Famille armement(8) | VARCHAR | True |
| Famille armement(9) | VARCHAR | True |
| Famille armement(10) | VARCHAR | True |
| Famille armement(11) | VARCHAR | True |
| Famille armement(12) | VARCHAR | True |
| Famille armement(13) | VARCHAR | True |
| Famille armement(14) | VARCHAR | True |
| Famille armement(15) | VARCHAR | True |
| Description | VARCHAR | True |
| Norme | VARCHAR | True |
| Valeur | REAL | True |

### Table `Nom complet armement`

- Row count: `582`
- Columns: `17`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| Nom réduit | VARCHAR | True |
| Nom Complet | VARCHAR | True |
| Effort ruine(0) | REAL | True |
| Flexibilité | REAL | True |
| Caché | SMALLINT | True |
| Element de base | SMALLINT | True |
| Effort ruine(1) | REAL | True |
| Effort ruine(2) | REAL | True |
| Effort ruine(3) | REAL | True |
| Pente trapèze | REAL | True |
| Effort minimal support | REAL | True |
| Classe support min | VARCHAR | True |
| Effort réf | REAL | True |
| Traverse | REAL | True |
| Montant | REAL | True |
| Valeur | REAL | True |
| EffortFusible | DOUBLE | True |

### Table `Nom réduit armement`

- Row count: `132`
- Columns: `19`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| Famille | VARCHAR | True |
| Nom réduit | VARCHAR | True |
| Structure | SMALLINT | True |
| y0 | REAL | True |
| y1 | REAL | True |
| y2 | REAL | True |
| y3 | REAL | True |
| y4 | REAL | True |
| y5 | REAL | True |
| z0 | REAL | True |
| z1 | REAL | True |
| z2 | REAL | True |
| z3 | REAL | True |
| z4 | REAL | True |
| z5 | REAL | True |
| Caché | SMALLINT | True |
| Element de base | SMALLINT | True |
| Coef tangente inclinaison | REAL | True |
| Ecart | REAL | True |

### Table `Observations`

- Row count: `5`
- Columns: `1`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| Libellé | VARCHAR | True |

### Table `Support`

- Row count: `2529`
- Columns: `28`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| Nom | VARCHAR | True |
| Hauteur | REAL | True |
| Classe | VARCHAR | True |
| Effort ruine | REAL | True |
| Flexibilité | REAL | True |
| Flexibilité Y | REAL | True |
| Largeur base | REAL | True |
| Epaisseur base | REAL | True |
| Largeur sommet | REAL | True |
| Epaisseur sommet | REAL | True |
| Fondation b(0) | REAL | True |
| Fondation b(1) | REAL | True |
| Fondation b(2) | REAL | True |
| Fondation b(3) | REAL | True |
| Fondation b(4) | REAL | True |
| Fondation b(5) | REAL | True |
| Fondation b(6) | REAL | True |
| Fondation b(7) | REAL | True |
| Fondation b(8) | REAL | True |
| Fondation b(9) | REAL | True |
| Fondation b(10) | REAL | True |
| Fondation b(11) | REAL | True |
| Effort max compression | REAL | True |
| Effort ruine en DP | REAL | True |
| Caché HTA | SMALLINT | True |
| Element de base | SMALLINT | True |
| Caché BT | SMALLINT | True |
| Valeur | REAL | True |

### Table `Support-type`

- Row count: `2`
- Columns: `111`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| Nom | VARCHAR | True |
| Hauteur(0) | REAL | True |
| Classe(0) | VARCHAR | True |
| Nature(0) | SMALLINT | True |
| Structure(0) | SMALLINT | True |
| Omega(0) | REAL | True |
| Armement(0) | VARCHAR | True |
| Omega armement(0) | REAL | True |
| Branchement(0) | SMALLINT | True |
| Isolateur(0) | VARCHAR | True |
| Hauteur(1) | REAL | True |
| Classe(1) | VARCHAR | True |
| Nature(1) | SMALLINT | True |
| Structure(1) | SMALLINT | True |
| Omega(1) | REAL | True |
| Armement(1) | VARCHAR | True |
| Omega armement(1) | REAL | True |
| Branchement(1) | SMALLINT | True |
| Isolateur(1) | VARCHAR | True |
| Hauteur(2) | REAL | True |
| Classe(2) | VARCHAR | True |
| Nature(2) | SMALLINT | True |
| Structure(2) | SMALLINT | True |
| Omega(2) | REAL | True |
| Armement(2) | VARCHAR | True |
| Omega armement(2) | REAL | True |
| Branchement(2) | SMALLINT | True |
| Isolateur(2) | VARCHAR | True |
| Hauteur(3) | REAL | True |
| Classe(3) | VARCHAR | True |
| Nature(3) | SMALLINT | True |
| Structure(3) | SMALLINT | True |
| Omega(3) | REAL | True |
| Armement(3) | VARCHAR | True |
| Omega armement(3) | REAL | True |
| Branchement(3) | SMALLINT | True |
| Isolateur(3) | VARCHAR | True |
| Hauteur(4) | REAL | True |
| Classe(4) | VARCHAR | True |
| Nature(4) | SMALLINT | True |
| Structure(4) | SMALLINT | True |
| Omega(4) | REAL | True |
| Armement(4) | VARCHAR | True |
| Omega armement(4) | REAL | True |
| Branchement(4) | SMALLINT | True |
| Isolateur(4) | VARCHAR | True |
| Hauteur(5) | REAL | True |
| Classe(5) | VARCHAR | True |
| Nature(5) | SMALLINT | True |
| Structure(5) | SMALLINT | True |
| Omega(5) | REAL | True |
| Armement(5) | VARCHAR | True |
| Omega armement(5) | REAL | True |
| Branchement(5) | SMALLINT | True |
| Isolateur(5) | VARCHAR | True |
| Hauteur(6) | REAL | True |
| Classe(6) | VARCHAR | True |
| Nature(6) | SMALLINT | True |
| Structure(6) | SMALLINT | True |
| Omega(6) | REAL | True |
| Armement(6) | VARCHAR | True |
| Omega armement(6) | REAL | True |
| Branchement(6) | SMALLINT | True |
| Isolateur(6) | VARCHAR | True |
| Hauteur(7) | REAL | True |
| Classe(7) | VARCHAR | True |
| Nature(7) | SMALLINT | True |
| Structure(7) | SMALLINT | True |
| Omega(7) | REAL | True |
| Armement(7) | VARCHAR | True |
| Omega armement(7) | REAL | True |
| Branchement(7) | SMALLINT | True |
| Isolateur(7) | VARCHAR | True |
| Hauteur(8) | REAL | True |
| Classe(8) | VARCHAR | True |
| Nature(8) | SMALLINT | True |
| Structure(8) | SMALLINT | True |
| Omega(8) | REAL | True |
| Armement(8) | VARCHAR | True |
| Omega armement(8) | REAL | True |
| Branchement(8) | SMALLINT | True |
| Isolateur(8) | VARCHAR | True |
| Hauteur(9) | REAL | True |
| Classe(9) | VARCHAR | True |
| Nature(9) | SMALLINT | True |
| Structure(9) | SMALLINT | True |
| Omega(9) | REAL | True |
| Armement(9) | VARCHAR | True |
| Omega armement(9) | REAL | True |
| Branchement(9) | SMALLINT | True |
| Isolateur(9) | VARCHAR | True |
| Ks(0) | REAL | True |
| Nature sol(0) | VARCHAR | True |
| Ks(1) | REAL | True |
| Nature sol(1) | VARCHAR | True |
| Ks(2) | REAL | True |
| Nature sol(2) | VARCHAR | True |
| Ks(3) | REAL | True |
| Nature sol(3) | VARCHAR | True |
| Ks(4) | REAL | True |
| Nature sol(4) | VARCHAR | True |
| Ks(5) | REAL | True |
| Nature sol(5) | VARCHAR | True |
| Ks(6) | REAL | True |
| Nature sol(6) | VARCHAR | True |
| Ks(7) | REAL | True |
| Nature sol(7) | VARCHAR | True |
| Ks(8) | REAL | True |
| Nature sol(8) | VARCHAR | True |
| Ks(9) | REAL | True |
| Nature sol(9) | VARCHAR | True |

## Database: `C:\Users\killi\Documents\0 - Playground\ERAS-MCP\artifacts\work\eras_mdb\Comac__a44696bcf1b0.mdb`

- ODBC driver: `Microsoft Access Driver (*.mdb, *.accdb)`
- pyodbc available: `True`
- Tables discovered: `10`

### Table `Armements`

- Row count: `4`
- Columns: `8`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| Nom | VARCHAR | True |
| Description | VARCHAR | True |
| z(0) | REAL | True |
| z(1) | REAL | True |
| z(2) | REAL | True |
| z(3) | REAL | True |
| z(4) | REAL | True |
| z(5) | REAL | True |

### Table `Commune`

- Row count: `36357`
- Columns: `8`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| Id | COUNTER | False |
| Dep | VARCHAR | True |
| Insee | VARCHAR | True |
| Nom | VARCHAR | True |
| Zone1 | SMALLINT | True |
| Zone2 | REAL | True |
| Zone3 | REAL | True |
| Zone4 | REAL | True |

### Table `Config`

- Row count: `1`
- Columns: `1`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| Version | VARCHAR | True |

### Table `Câble`

- Row count: `477`
- Columns: `26`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| Nom | VARCHAR | True |
| PorteqMax | INTEGER | True |
| Section réelle | REAL | True |
| Diamètre | REAL | True |
| Masse linéique | REAL | True |
| Module d'Young | REAL | True |
| Coef de dilatation | REAL | True |
| Charge de rupture nominale | REAL | True |
| Volt | VARCHAR | True |
| Tension conseillée rigide agglo | REAL | True |
| Description | VARCHAR | True |
| AncienNom | VARCHAR | True |
| Type | VARCHAR | True |
| Tension conseillée rigide écart | REAL | True |
| Paramètre conseillé suspendu | REAL | True |
| Tension conseillée rigide écart ZVF | REAL | True |
| Paramètre conseillé suspendu ZVF | REAL | True |
| Tension conseillée rigide agglo ZVF | REAL | True |
| Caché | SMALLINT | True |
| Element de base | SMALLINT | True |
| Code | VARCHAR | True |
| Porteq | REAL | True |
| optRaccordement | SMALLINT | True |
| Autre paramètre ZVN 1 | REAL | True |
| Autre paramètre ZVN 2 | REAL | True |
| Autre paramètre ZVF | REAL | True |

### Table `Fleche`

- Row count: `6`
- Columns: `3`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| Numero | INTEGER | True |
| Fleche | DOUBLE | True |
| portee | INTEGER | True |

### Table `HypotheseAnnee`

- Row count: `4`
- Columns: `4`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| Nom | VARCHAR | True |
| Id | SMALLINT | True |
| Afficher | SMALLINT | True |
| Indice | SMALLINT | True |

### Table `Hypothèse`

- Row count: `17`
- Columns: `7`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| Nom | VARCHAR | True |
| Volt | VARCHAR | True |
| Description | VARCHAR | True |
| Température | REAL | True |
| Pression de Vent conducteurs | REAL | True |
| Caché | SMALLINT | True |
| Complementaire | INTEGER | True |

### Table `Nappes T/V`

- Row count: `144`
- Columns: `13`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| Nom | VARCHAR | True |
| Description | VARCHAR | True |
| Nb neutres | SMALLINT | True |
| Nb phases | SMALLINT | True |
| Nb EP | SMALLINT | True |
| Neutre | VARCHAR | True |
| Conducteur | VARCHAR | True |
| Eclairage Public | VARCHAR | True |
| Caché | SMALLINT | True |
| Element de base | SMALLINT | True |
| Zone | VARCHAR | True |
| Tension | REAL | True |
| Code | VARCHAR | True |

### Table `PinceFusible`

- Row count: `8`
- Columns: `3`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| Nom | VARCHAR | True |
| Description | VARCHAR | True |
| Effort | REAL | True |

### Table `Support`

- Row count: `1401`
- Columns: `19`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| Nom | VARCHAR | True |
| Nature | VARCHAR | True |
| Classe | VARCHAR | True |
| Structure | VARCHAR | True |
| Effort nominal | REAL | True |
| Tau | REAL | True |
| Effort transversal en DP | REAL | True |
| Tau en DP | REAL | True |
| Caché | SMALLINT | True |
| Hauteur totale | REAL | True |
| Element de base | SMALLINT | True |
| Nom CAPFT | VARCHAR | True |
| NomGESPOT | VARCHAR | True |
| Description | VARCHAR | True |
| Largeurbase | REAL | True |
| Epaisseurbase | REAL | True |
| bC3 | REAL | True |
| bC3C | REAL | True |
| Graphique | VARCHAR | True |

## Database: `C:\Users\killi\Documents\0 - Playground\ERAS-MCP\artifacts\work\eras_mdb\eauAss__c1a041defdd1.mdb`

- ODBC driver: `Microsoft Access Driver (*.mdb, *.accdb)`
- pyodbc available: `True`
- Tables discovered: `6`

### Table `cells`

- Row count: `50`
- Columns: `2`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| Nom | VARCHAR | True |
| Id | INTEGER | True |

### Table `Famille`

- Row count: `1`
- Columns: `3`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| FAM_CODE | COUNTER | False |
| FAM_NOM | VARCHAR | True |
| FAM_DESC | VARCHAR | True |

### Table `FiltreNiveau`

- Row count: `1`
- Columns: `5`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| idfiltre | COUNTER | False |
| parentid | INTEGER | True |
| idniveau | INTEGER | True |
| description | CHAR | True |
| Position | INTEGER | True |

### Table `fonts`

- Row count: `4`
- Columns: `3`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| Nom | CHAR | True |
| Id | INTEGER | True |
| Type | INTEGER | True |

### Table `levels`

- Row count: `26`
- Columns: `6`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| Id | INTEGER | True |
| nom | VARCHAR | True |
| pos | INTEGER | True |
| Couleur | INTEGER | True |
| Style | VARCHAR | True |
| Epaisseur | INTEGER | True |

### Table `version`

- Row count: `12`
- Columns: `3`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| Base | VARCHAR | True |
| Description | VARCHAR | True |
| Application | VARCHAR | True |

## Database: `C:\Users\killi\Documents\0 - Playground\ERAS-MCP\artifacts\work\eras_mdb\eauAss___e453a8a4b65c.mdb`

- ODBC driver: `Microsoft Access Driver (*.mdb, *.accdb)`
- pyodbc available: `True`
- Tables discovered: `0`

### Warnings

- ODBC schema read failed: 'utf-16-le' codec can't decode bytes in position 72-73: illegal UTF-16 surrogate

## Database: `C:\Users\killi\Documents\0 - Playground\ERAS-MCP\artifacts\work\eras_mdb\ext-champion-_eu-ep-250_dwg__6d31c8b523d2.mdb`

- ODBC driver: `Microsoft Access Driver (*.mdb, *.accdb)`
- pyodbc available: `True`
- Tables discovered: `0`

### Warnings

- ODBC schema read failed: 'utf-16-le' codec can't decode bytes in position 72-73: illegal UTF-16 surrogate

## Database: `C:\Users\killi\Documents\0 - Playground\ERAS-MCP\artifacts\work\eras_mdb\ENEDIS22__808ae9780ce5.mdb`

- ODBC driver: `Microsoft Access Driver (*.mdb, *.accdb)`
- pyodbc available: `True`
- Tables discovered: `6`

### Table `cells`

- Row count: `162`
- Columns: `2`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| Nom | VARCHAR | True |
| Id | INTEGER | True |

### Table `Famille`

- Row count: `1`
- Columns: `3`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| FAM_CODE | COUNTER | False |
| FAM_NOM | VARCHAR | True |
| FAM_DESC | VARCHAR | True |

### Table `FiltreNiveau`

- Row count: `133`
- Columns: `5`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| idfiltre | COUNTER | False |
| parentid | INTEGER | True |
| idniveau | INTEGER | True |
| description | CHAR | True |
| Position | INTEGER | True |

### Table `fonts`

- Row count: `16`
- Columns: `3`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| Nom | CHAR | True |
| Id | INTEGER | True |
| Type | INTEGER | True |

### Table `levels`

- Row count: `396`
- Columns: `6`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| Id | INTEGER | True |
| Nom | VARCHAR | True |
| pos | INTEGER | True |
| Couleur | INTEGER | True |
| Style | VARCHAR | True |
| Epaisseur | INTEGER | True |

### Table `version`

- Row count: `13`
- Columns: `3`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| Base | VARCHAR | True |
| Description | VARCHAR | True |
| Application | VARCHAR | True |

## Database: `C:\Users\killi\Documents\0 - Playground\ERAS-MCP\artifacts\work\eras_mdb\ENEDIS22___bfd60e9bb301.mdb`

- ODBC driver: `Microsoft Access Driver (*.mdb, *.accdb)`
- pyodbc available: `True`
- Tables discovered: `0`

### Warnings

- ODBC schema read failed: 'utf-16-le' codec can't decode bytes in position 72-73: illegal UTF-16 surrogate

## Database: `C:\Users\killi\Documents\0 - Playground\ERAS-MCP\artifacts\work\eras_mdb\ENEDIS23__b95c26b01fba.mdb`

- ODBC driver: `Microsoft Access Driver (*.mdb, *.accdb)`
- pyodbc available: `True`
- Tables discovered: `6`

### Table `cells`

- Row count: `201`
- Columns: `2`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| Nom | VARCHAR | True |
| Id | INTEGER | True |

### Table `Famille`

- Row count: `1`
- Columns: `3`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| FAM_CODE | COUNTER | False |
| FAM_NOM | VARCHAR | True |
| FAM_DESC | VARCHAR | True |

### Table `FiltreNiveau`

- Row count: `170`
- Columns: `5`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| idfiltre | COUNTER | False |
| parentid | INTEGER | True |
| idniveau | INTEGER | True |
| description | CHAR | True |
| Position | INTEGER | True |

### Table `fonts`

- Row count: `17`
- Columns: `3`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| Nom | CHAR | True |
| Id | INTEGER | True |
| Type | INTEGER | True |

### Table `levels`

- Row count: `397`
- Columns: `6`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| Id | INTEGER | True |
| Nom | VARCHAR | True |
| pos | INTEGER | True |
| Couleur | INTEGER | True |
| Style | VARCHAR | True |
| Epaisseur | INTEGER | True |

### Table `version`

- Row count: `13`
- Columns: `3`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| Base | VARCHAR | True |
| Description | VARCHAR | True |
| Application | VARCHAR | True |

## Database: `C:\Users\killi\Documents\0 - Playground\ERAS-MCP\artifacts\work\eras_mdb\ENEDIS23___87e0451d9168.mdb`

- ODBC driver: `Microsoft Access Driver (*.mdb, *.accdb)`
- pyodbc available: `True`
- Tables discovered: `0`

### Warnings

- ODBC schema read failed: 'utf-16-le' codec can't decode bytes in position 72-73: illegal UTF-16 surrogate

## Database: `C:\Users\killi\Documents\0 - Playground\ERAS-MCP\artifacts\work\eras_mdb\enedis__4374f351ac85.mdb`

- ODBC driver: `Microsoft Access Driver (*.mdb, *.accdb)`
- pyodbc available: `True`
- Tables discovered: `6`

### Table `cells`

- Row count: `104`
- Columns: `2`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| Nom | VARCHAR | True |
| Id | INTEGER | True |

### Table `Famille`

- Row count: `1`
- Columns: `3`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| FAM_CODE | COUNTER | False |
| FAM_NOM | VARCHAR | True |
| FAM_DESC | VARCHAR | True |

### Table `FiltreNiveau`

- Row count: `112`
- Columns: `5`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| idfiltre | COUNTER | False |
| parentid | INTEGER | True |
| idniveau | INTEGER | True |
| description | CHAR | True |
| Position | INTEGER | True |

### Table `fonts`

- Row count: `13`
- Columns: `3`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| Nom | CHAR | True |
| Id | INTEGER | True |
| Type | INTEGER | True |

### Table `levels`

- Row count: `360`
- Columns: `6`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| Id | INTEGER | True |
| Nom | VARCHAR | True |
| pos | INTEGER | True |
| Couleur | INTEGER | True |
| Style | VARCHAR | True |
| Epaisseur | INTEGER | True |

### Table `version`

- Row count: `13`
- Columns: `3`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| Base | VARCHAR | True |
| Description | VARCHAR | True |
| Application | VARCHAR | True |

## Database: `C:\Users\killi\Documents\0 - Playground\ERAS-MCP\artifacts\work\eras_mdb\enedis___34498a4ade44.mdb`

- ODBC driver: `Microsoft Access Driver (*.mdb, *.accdb)`
- pyodbc available: `True`
- Tables discovered: `0`

### Warnings

- ODBC schema read failed: 'utf-16-le' codec can't decode bytes in position 72-73: illegal UTF-16 surrogate

## Database: `C:\Users\killi\Documents\0 - Playground\ERAS-MCP\artifacts\work\eras_mdb\FTTH__bade89b41e5f.mdb`

- ODBC driver: `Microsoft Access Driver (*.mdb, *.accdb)`
- pyodbc available: `True`
- Tables discovered: `6`

### Table `cells`

- Row count: `138`
- Columns: `2`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| Nom | VARCHAR | True |
| Id | INTEGER | True |

### Table `Famille`

- Row count: `1`
- Columns: `3`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| FAM_CODE | COUNTER | False |
| FAM_NOM | VARCHAR | True |
| FAM_DESC | VARCHAR | True |

### Table `FiltreNiveau`

- Row count: `0`
- Columns: `5`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| idfiltre | COUNTER | False |
| parentid | INTEGER | True |
| idniveau | INTEGER | True |
| description | CHAR | True |
| Position | INTEGER | True |

### Table `fonts`

- Row count: `15`
- Columns: `3`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| Nom | CHAR | True |
| Id | INTEGER | True |
| Type | INTEGER | True |

### Table `levels`

- Row count: `264`
- Columns: `6`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| Id | INTEGER | True |
| Nom | VARCHAR | True |
| pos | INTEGER | True |
| Couleur | INTEGER | True |
| Style | VARCHAR | True |
| Epaisseur | INTEGER | True |

### Table `version`

- Row count: `12`
- Columns: `3`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| Base | VARCHAR | True |
| Description | VARCHAR | True |
| Application | VARCHAR | True |

## Database: `C:\Users\killi\Documents\0 - Playground\ERAS-MCP\artifacts\work\eras_mdb\FTTH___252d4cf5d6a9.mdb`

- ODBC driver: `Microsoft Access Driver (*.mdb, *.accdb)`
- pyodbc available: `True`
- Tables discovered: `0`

### Warnings

- ODBC schema read failed: 'utf-16-le' codec can't decode bytes in position 72-73: illegal UTF-16 surrogate

## Database: `C:\Users\killi\Documents\0 - Playground\ERAS-MCP\artifacts\work\eras_mdb\globlsys__8e174f2092c4.mdb`

- ODBC driver: `Microsoft Access Driver (*.mdb, *.accdb)`
- pyodbc available: `True`
- Tables discovered: `0`

### Warnings

- ODBC schema read failed: 'utf-16-le' codec can't decode bytes in position 72-73: illegal UTF-16 surrogate

## Database: `C:\Users\killi\Documents\0 - Playground\ERAS-MCP\artifacts\work\eras_mdb\SOURCE__10ea952fbd85.mdb`

- ODBC driver: `Microsoft Access Driver (*.mdb, *.accdb)`
- pyodbc available: `True`
- Tables discovered: `6`

### Table `cells`

- Row count: `8`
- Columns: `2`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| Nom | VARCHAR | True |
| Id | INTEGER | True |

### Table `Famille`

- Row count: `1`
- Columns: `3`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| FAM_CODE | COUNTER | False |
| FAM_NOM | VARCHAR | True |
| FAM_DESC | VARCHAR | True |

### Table `FiltreNiveau`

- Row count: `0`
- Columns: `5`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| idfiltre | COUNTER | False |
| parentid | INTEGER | True |
| idniveau | INTEGER | True |
| description | CHAR | True |
| Position | INTEGER | True |

### Table `fonts`

- Row count: `0`
- Columns: `3`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| Nom | CHAR | True |
| Id | INTEGER | True |
| Type | INTEGER | True |

### Table `levels`

- Row count: `9`
- Columns: `6`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| Id | INTEGER | True |
| Nom | VARCHAR | True |
| pos | INTEGER | True |
| Couleur | INTEGER | True |
| Style | VARCHAR | True |
| Epaisseur | INTEGER | True |

### Table `version`

- Row count: `12`
- Columns: `3`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| Base | VARCHAR | True |
| Description | VARCHAR | True |
| Application | VARCHAR | True |

## Database: `C:\Users\killi\Documents\0 - Playground\ERAS-MCP\artifacts\work\eras_mdb\SOURCE___16d297bcfca4.mdb`

- ODBC driver: `Microsoft Access Driver (*.mdb, *.accdb)`
- pyodbc available: `True`
- Tables discovered: `0`

### Warnings

- ODBC schema read failed: 'utf-16-le' codec can't decode bytes in position 72-73: illegal UTF-16 surrogate

## Database: `C:\Users\killi\Documents\0 - Playground\ERAS-MCP\artifacts\work\eras_mdb\SYSTEME__4de4eb1693b5.mdb`

- ODBC driver: `Microsoft Access Driver (*.mdb, *.accdb)`
- pyodbc available: `True`
- Tables discovered: `7`

### Table `cells`

- Row count: `5`
- Columns: `2`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| Nom | VARCHAR | True |
| Id | INTEGER | True |

### Table `Famille`

- Row count: `1`
- Columns: `3`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| FAM_CODE | COUNTER | False |
| FAM_NOM | VARCHAR | True |
| FAM_DESC | VARCHAR | True |

### Table `FiltreNiveau`

- Row count: `1`
- Columns: `5`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| idfiltre | COUNTER | False |
| parentid | INTEGER | True |
| idniveau | INTEGER | True |
| description | CHAR | True |
| Position | INTEGER | True |

### Table `FiltreNiveauGeneral`

- Row count: `0`
- Columns: `7`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| IDFILTRE | INTEGER | True |
| PARENTID | INTEGER | True |
| NOMNIVEAU | VARCHAR | True |
| DESCRIPTION | VARCHAR | True |
| ETATAFFICHE | INTEGER | True |
| POSITION | INTEGER | True |
| VALIDE | INTEGER | True |

### Table `fonts`

- Row count: `5`
- Columns: `3`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| Nom | CHAR | True |
| Id | INTEGER | True |
| Type | INTEGER | True |

### Table `levels`

- Row count: `12`
- Columns: `6`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| Id | INTEGER | True |
| nom | VARCHAR | True |
| pos | INTEGER | True |
| Couleur | INTEGER | True |
| Style | VARCHAR | True |
| Epaisseur | INTEGER | True |

### Table `version`

- Row count: `13`
- Columns: `3`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| Base | VARCHAR | True |
| Description | VARCHAR | True |
| Application | VARCHAR | True |

## Database: `C:\Users\killi\Documents\0 - Playground\ERAS-MCP\artifacts\work\eras_mdb\temp__a7dca48c38c2.mdb`

- ODBC driver: `Microsoft Access Driver (*.mdb, *.accdb)`
- pyodbc available: `True`
- Tables discovered: `9`

### Table `FEATURE`

- Row count: `0`
- Columns: `11`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| MSLINK | INTEGER | True |
| FCODE | VARCHAR | True |
| FNAME | VARCHAR | True |
| CATEGORY | INTEGER | True |
| TABLENAME | VARCHAR | True |
| FTYPE | INTEGER | True |
| FLEVEL | INTEGER | True |
| FSTYLE | INTEGER | True |
| FWEIGHT | INTEGER | True |
| FCOLOR | INTEGER | True |
| DIGCMD | VARCHAR | True |

### Table `INPUTFORMS`

- Row count: `0`
- Columns: `7`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| FORMID | INTEGER | True |
| FORMTITLE | VARCHAR | True |
| DELETE_FLAG | INTEGER | True |
| INSERT_FLAG | INTEGER | True |
| APP_TOLOAD | VARCHAR | True |
| RSC_FILENAME | VARCHAR | True |
| PDM_ID1 | INTEGER | True |

### Table `INPUTGADGETS`

- Row count: `0`
- Columns: `17`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| FORMID | INTEGER | True |
| GADGETID | INTEGER | True |
| COLUMN_PROMPT | VARCHAR | True |
| COLUMNNAME | VARCHAR | True |
| VALUE_REQUIRED | INTEGER | True |
| DISPLAYONLY | INTEGER | True |
| WITHLIST | INTEGER | True |
| SELECTSTMT | VARCHAR | True |
| VISIBLECHARS | INTEGER | True |
| MAXCHARS | INTEGER | True |
| FIELDTYPE | INTEGER | True |
| GADGET_FORMAT | VARCHAR | True |
| SUB_FORM | INTEGER | True |
| SUB_REF_ID | INTEGER | True |
| COLUMN_ID | INTEGER | True |
| GADGET_PICTURE | VARCHAR | True |
| SELECTSTMTID | INTEGER | True |

### Table `maps`

- Row count: `0`
- Columns: `3`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| mslink | COUNTER | False |
| category | INTEGER | True |
| mapname | VARCHAR | True |

### Table `MSCATALOG`

- Row count: `9`
- Columns: `9`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| TABLENAME | VARCHAR | True |
| ENTITYNUM | INTEGER | True |
| NEXTOCC | INTEGER | True |
| SCREENFORM | VARCHAR | True |
| REPORTTABLE | VARCHAR | True |
| SQLREVIEW | VARCHAR | True |
| FENCEFILTER | VARCHAR | True |
| DASTABLE | VARCHAR | True |
| TABLETYPE | VARCHAR | True |

### Table `PROJ_CAT`

- Row count: `18`
- Columns: `20`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| TABLENAME | VARCHAR | True |
| SHORTNAME | VARCHAR | True |
| ENTITYNUM | INTEGER | True |
| SCREENFORM | VARCHAR | True |
| REPORTTABLE | VARCHAR | True |
| SQLREVIEW | VARCHAR | True |
| FENCEFILTER | VARCHAR | True |
| DASTABLE | VARCHAR | True |
| TABLETYPE | VARCHAR | True |
| C_DESCRIPTION | VARCHAR | True |
| TAB_TYPE | VARCHAR | True |
| LOAD_FLAG | VARCHAR | True |
| FORMID | VARCHAR | True |
| LOCATE_FORMID | VARCHAR | True |
| IN_LOCATE_MENU | VARCHAR | True |
| LOCATE_MACRO | VARCHAR | True |
| MAIN_TABLE | VARCHAR | True |
| QUER_FORMID | VARCHAR | True |
| TAB_FLAG | VARCHAR | True |
| NEXTOCC | INTEGER | True |

### Table `PROJ_CAT_COL`

- Row count: `0`
- Columns: `19`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| ENTITYNUM | INTEGER | True |
| COLUMN_ID | INTEGER | True |
| COLUMN_NAME | VARCHAR | True |
| SHORTNAME | VARCHAR | True |
| CODE_COL_ID | INTEGER | True |
| COLUMN_PROMPT | VARCHAR | True |
| COLUMN_TYPE | INTEGER | True |
| COLUMN_LENGTH | INTEGER | True |
| COLUMN_NOTNULL | INTEGER | True |
| COLUMN_DISPONLY | INTEGER | True |
| COLUMN_FORMAT | VARCHAR | True |
| COLUMN_DEFAULT | VARCHAR | True |
| COLUMN_KEY | INTEGER | True |
| COLUMN_USAGE | INTEGER | True |
| COLUMN_VISIBLE | INTEGER | True |
| COLUMN_EVENTS | INTEGER | True |
| VALID_FOR_CATEGORY | INTEGER | True |
| COLUMN_PICTURE | VARCHAR | True |
| COLUMN_GEN | INTEGER | True |

### Table `SYMATTR`

- Row count: `0`
- Columns: `9`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| FEATUREID | INTEGER | True |
| FONT | INTEGER | True |
| TXHEIGHT | INTEGER | True |
| TXWIDTH | INTEGER | True |
| JUST | INTEGER | True |
| AA | VARCHAR | True |
| SYMBOL | INTEGER | True |
| SYMTABLE | VARCHAR | True |
| SCALETABLE | VARCHAR | True |

### Table `TEMPO_POUR_BMPV`

- Row count: `0`
- Columns: `1`
- Primary keys: `none detected`

| Column | Type | Nullable |
|---|---|---|
| N° | COUNTER | False |
