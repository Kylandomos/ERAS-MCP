# ERAS / OpenCities MCP (Windows-First) - Read-Only MVP v0.1

Last updated: 2026-04-24

## Purpose

This repository hosts the controlled reverse-engineering and progressive industrialization effort for a local Windows MCP serving:

- OpenCities Map / MicroStation observability and safe probes
- ERAS MDB read-only analysis
- Evidence-driven reporting and governance

## Current Scope

This repository now contains the first read-only MVP baseline: reproducible inventory scripts, ERAS MDB copy-first analysis tooling, curated evidence reports, and an artifact-backed MCP facade.

## Facts Proved (Current State)

- `MASTER_PROMPT_Codex_Orchestrator.md` exists and defines orchestration/governance expectations.
- `ERAS_OpenCitiesMap_MCP_Kickoff.md` exists and defines kickoff scope, constraints, and target outputs.
- Two local roots are verified to exist as FileSystem directories (`Test-Path` + `Get-Item`):
  - `C:\AppSogelink\ERAS_Connect_2026`
  - `C:\Program Files\Bentley\OpenCities Map PowerView 2023\MapPowerView`
- Repository scaffold directories for `docs/`, `scripts/`, `src/`, `tests/`, and `artifacts/` are present.
- ERAS MDB discovery found `54` MDB/ACCDB candidates and created `54/54` hash-matching analysis copies.
- ERAS schema extraction is partial: `183` table rows across `20` databases, with `32` ODBC UTF-16 warnings.
- MDB candidate accounting is explicit: `54` discovered/scored candidate rows, `52` unique analysis path strings, and `51` normalized analysis keys.
- `CLIENT\client.mdb` is the top metadata-only candidate, but no authoritative MDB has been declared.
- The human decision artifact is initialized with `54` rows, all currently `needs_followup`.
- The latest read-only PowerMap inventory reports `2` executables, `2` workspace candidates, and one active gap: Python Manager was not found.
- The read-only MCP facade initializes with `mcp==1.27.0` and reads current artifacts without executing Bentley/OpenCities commands.

## Hypotheses (Not Yet Proved Here)

- The local OpenCities/MicroStation automation surface is sufficient for safe non-destructive probes.
- One of the discovered ERAS MDB files is the authoritative business database.

## Open Questions

- Exact Windows build, privileges, and endpoint hardening constraints?
- Exact install paths, workspace/workset configuration, and custom scripts/macros?
- Which MDB files are authoritative?
- Why do 32 MDB analyses return UTF-16 ODBC decode warnings?
- Is Python Manager absent, installed elsewhere, or hidden behind launcher/configuration state?

## Decisions

- Windows-first baseline.
- Read-only by default for environment and MDB workflows.
- Evidence-first delivery: no claim without traceable artifact path.
- Record root-path existence as a verified fact only; do not infer version or capability from path names.
- Keep raw scans, logs, generated exports, and MDB analysis copies out of Git; version curated docs under `docs/`.

## Repository Layout (Scaffold)

```text
.
|-- README.md
|-- ARCHITECTURE.md
|-- BACKLOG.md
|-- RISK_REGISTER.md
|-- TEST_STRATEGY.md
|-- SECURITY_GUARDRAILS.md
|-- EVIDENCE_INDEX.md
|-- ENVIRONMENT_SCAN.md
|-- WINDOWS_INVENTORY.md
|-- POWEMAP_AUTOMATION_SURFACE.md
|-- ERAS_MDB_SCHEMA.md
|-- docs/
|   |-- evidence/
|   |-- reports/
|   |-- reviews/
|   |-- scans/
|   `-- schemas/
|-- scripts/
|   |-- windows_scan/
|   |-- eras/
|   |-- powermap/
|   `-- reporting/
|-- src/
|   |-- mcp_server/
|   |-- adapters/
|   |   |-- eras_mdb/
|   |   `-- powermap/
|   |-- domain/
|   |-- services/
|   `-- utils/
|-- tests/
|   |-- unit/
|   |-- integration/
|   `-- fixtures/
`-- artifacts/
    |-- inventories/
    |-- snapshots/
    |-- logs/
    `-- exports/
```

## Acceptance Criteria for This Scaffold

- Required governance docs exist and are non-empty with actionable v0 content.
- Every root governance doc distinguishes facts, hypotheses, open questions, and decisions.
- Read-only scripts and MCP facade are testable from a clean local checkout.
- No destructive operation and no production-data write path introduced.
- Raw MDB files and generated raw artifacts are excluded from Git.

## Read-Only MVP Usage

Install direct dependencies:

```powershell
python -m pip install -r requirements.txt
```

Run the artifact-backed CLI from the repo:

```powershell
python -m pip install -e .
eras-mcp-readonly env-status
eras-mcp-readonly build-gap-report
```

If the Python user scripts directory is not on `PATH`, use:

```powershell
python -m mcp_server env-status
python -m mcp_server build-gap-report
python -m mcp_server eras-rank-databases --limit 10
python -m mcp_server eras-explain-database --path "C:\AppSogelink\ERAS_Connect_2026\CLIENT\client.mdb"
python -m mcp_server eras-review-status
python -m mcp_server eras-set-review-decision --source-path "C:\AppSogelink\ERAS_Connect_2026\CLIENT\client.mdb" --status accept_review --reviewer analyst --decision-basis "manual review" --dry-run
```

The CLI and MCP facade read existing artifacts by default. They do not rerun scans, write MDB files, or execute Bentley/OpenCities commands.

## ERAS MDB Candidate Ranking

- `eras-rank-databases` ranks MDB candidates using metadata only.
- `eras-explain-database` explains one candidate using score reasons and table metadata only.
- `eras-review-status` validates the human decision artifact without reading MDB row values.
- `eras-set-review-decision` updates only the versioned review CSV and regenerated status report; use `--dry-run` to preview without writing.
- The ranking is a review aid, not an authoritative database declaration.
- Curated outputs:
  - `docs/reports/eras_mdb_authoritative_candidates_20260423.md`
  - `docs/reports/eras_mdb_candidate_review_20260423.md`
  - `docs/reports/eras_mdb_odbc_warning_triage_20260423.md`
  - `docs/reports/eras_mdb_human_decision_status_20260424.md`
  - `docs/schemas/ERAS_MDB_CANDIDATE_SCORECARD.csv`
  - `docs/reviews/ERAS_MDB_HUMAN_DECISIONS_20260424.csv`
  - `docs/evidence/ev-009-eras-authoritative-candidates.md`
  - `docs/evidence/ev-010-eras-mdb-human-review-pack.md`
  - `docs/evidence/ev-011-eras-mdb-human-decisions.md`
  - `docs/evidence/ev-012-eras-mdb-decision-intake.md`

## Next Links

- Governance: `SECURITY_GUARDRAILS.md`, `RISK_REGISTER.md`, `TEST_STRATEGY.md`
- Discovery: `ENVIRONMENT_SCAN.md`, `WINDOWS_INVENTORY.md`, `POWEMAP_AUTOMATION_SURFACE.md`, `ERAS_MDB_SCHEMA.md`
- Evidence map: `EVIDENCE_INDEX.md`
- MVP baseline: `docs/reports/mvp_readonly_baseline_20260423.md`
- Current gaps: `docs/reports/mvp_gap_report_20260423.md`
- ERAS MDB ranking: `docs/reports/eras_mdb_authoritative_candidates_20260423.md`
- ERAS MDB human review: `docs/reports/eras_mdb_candidate_review_20260423.md`
- ERAS MDB human decisions: `docs/reports/eras_mdb_human_decision_status_20260424.md`
- ERAS MDB warning triage: `docs/reports/eras_mdb_odbc_warning_triage_20260423.md`

## Read-Only MCP Facade Notes (Worker E)

- The project now includes a read-only MCP facade/CLI under `src/mcp_server/`.
- Current dependency baseline for this facade is:
  - `mcp` (stdio server registration path)
  - `pyodbc` (ERAS MDB adapter/runtime path)
- With `mcp` installed, `create_mcp_stdio_server()` initializes successfully and read-only tools can be served over stdio.
- Guardrails remain unchanged: no Bentley/OpenCities command execution from this facade, and no write operations against production MDBs.
