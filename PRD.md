# PRD - ERAS/OpenCities Local MCP (v0)

## 1) Document Control
- Version: `0.1-draft`
- Date: `2026-04-23`
- Owner: `Worker D`
- Source inputs:
  - `MASTER_PROMPT_Codex_Orchestrator.md`
  - `ERAS_OpenCitiesMap_MCP_Kickoff.md`

## 2) Evidence Status (Truth Policy)
### 2.1 Proven Facts (Document-backed + locally verified)
- [FACT-DOC] Project intent is to build a **local Windows MCP** for OpenCities Map 2025 + ERAS.
- [FACT-DOC] First priority is **reverse-engineering and observability** before intrusive automation.
- [FACT-DOC] Security baseline requires **read-only by default**, especially for ERAS MDB.
- [FACT-DOC] Expected work includes environment scan, MDB analysis, automation-surface inventory, PRD/plan generation, and MVP skeleton.
- [FACT-DOC] Candidate MCP tools are already proposed in kickoff docs (environment, MDB, and powermap probes).
- [FACT-LOCAL] ERAS root exists as a directory: `C:\AppSogelink\ERAS_Connect_2026` (verified via `Test-Path` => `True`, provider `FileSystem`, type `Directory`).
- [FACT-LOCAL] MapPowerView root exists as a directory: `C:\Program Files\Bentley\OpenCities Map PowerView 2023\MapPowerView` (verified via `Test-Path` => `True`, provider `FileSystem`, type `Directory`).

### 2.2 Hypotheses (To validate during scan)
- [HYP] OpenCities Map 2025 is present and actively used on the target workstation.
- [HYP] ERAS is installed with at least one active `.mdb` database.
- [HYP] Local scripts/macros/configuration artifacts exist and can be inventoried.
- [HYP] Safe read-only probes are feasible for both Bentley and ERAS data layers.

### 2.3 Open Questions
- [Q] Exact Windows version/build, privileges, and enterprise hardening constraints?
- [Q] Exact OpenCities/MicroStation automation channels available (Python Manager, key-ins, VBA, COM)?
- [Q] Number/location/size/locking mode of ERAS MDB files in production?
- [Q] Data sensitivity class and redaction obligations for evidence artifacts?
- [Q] Execution model for MCP service (manual, scheduled, service account)?

### 2.4 Initial Decisions
- [DEC-001] Treat all environment-specific statements as unverified until scan artifacts exist.
- [DEC-002] Keep all ERAS DB access read-only in MVP; no write path in first release.
- [DEC-003] Ship an evidence-first MCP: every tool call should produce traceable logs/artifacts.
- [DEC-004] Keep dangerous/active automation capabilities disabled by default and feature-gated.

## 3) Product Goal
Deliver a local Windows MCP that lets an LLM safely inspect the OpenCities/ERAS environment, query ERAS MDB data in read-only mode, and generate auditable evidence for controlled automation planning.

## 4) Target Users
- GIS/CAD operations engineers working with OpenCities Map / MicroStation.
- ERAS business/application owners needing schema visibility and controlled data inspection.
- Automation engineers building MCP-driven workflows on top of validated local capabilities.
- Project orchestrator/reviewers who need reproducible evidence, risk visibility, and traceability.

## 5) Context
This project starts from a real production-like workstation context. The priority is to understand the existing stack (software, paths, configs, scripts, data stores) before introducing any automation that can mutate state.

## 6) Scope (v0 to MVP)
### In Scope
- Windows-first environment scanning and inventory.
- Use verified starting scan roots for cycle 1: `C:\AppSogelink\ERAS_Connect_2026` and `C:\Program Files\Bentley\OpenCities Map PowerView 2023\MapPowerView`.
- Discovery/indexing of relevant artifacts (Bentley, ERAS, scripts, configs, logs).
- ERAS MDB copy-and-analyze workflow (schema, table metadata, row counts, safe sampling).
- OpenCities/MicroStation automation-surface discovery with safe read probes only.
- MCP server skeleton exposing environment + ERAS read-only + powermap capability tools.
- Evidence and report generation with timestamps and trace links.
- Core documentation: PRD/PLAN/risks/test strategy/security guardrails.

### Out of Scope (MVP)
- Any direct write/update/delete in production MDB.
- Unbounded raw SQL execution against unknown DBs in production context.
- Destructive or stateful automation in OpenCities/MicroStation.
- Full business-rule automation and deep drawing-to-data consistency engine.
- Enterprise rollout concerns (HA, multi-host orchestration, centralized secrets platform).

## 7) Technical Constraints
- Windows-first operation.
- Reproducible scripts and deterministic outputs where practical.
- Local filesystem and installed software are treated as the source of truth after scan.
- Clear logging, timestamping, and artifact indexing for every meaningful action.
- Avoid obscure dependencies without explicit justification.

## 8) Functional Architecture (Proposed)
1. `Environment Scanner`
   - Collects OS/runtime/process/service/path/config evidence.
2. `Artifact Discovery Service`
   - Finds project-relevant files (`.mdb`, `.dgn`, `.cfg`, scripts, logs, exports).
3. `ERAS MDB Adapter (Read-only)`
   - Metadata extraction, schema reports, safe samples, named readonly queries.
4. `OpenCities/PowerMap Adapter (Safe Probes)`
   - Capability detection, workspace/script inventory, non-destructive probe execution.
5. `Evidence Engine`
   - Normalized logging, artifact hashing, run manifests, report generation.
6. `MCP Server Layer`
   - Exposes tools with guardrails, validation, and structured outputs.
7. `Test Harness`
   - Unit + integration tests with fixtures/mocks and safety checks.

## 9) Adapter Definitions
### 9.1 ERAS MDB Adapter
- Purpose: expose deterministic read-only access to ERAS database structure and selected data samples.
- Required capabilities:
  - list databases/candidates
  - describe MDB schema (tables/fields/indexes)
  - row counts per table
  - safe row sampling
  - named query execution (whitelisted)
- Safety:
  - no DDL/DML
  - optional execution only on copied analysis DB by default
  - query allowlist and parameter validation

### 9.2 OpenCities/PowerMap Adapter
- Purpose: inspect available automation channels without mutating project state.
- Required capabilities:
  - status/version/workspace discovery
  - script and tool inventory
  - safe probe execution with explicit allowlist
- Safety:
  - no destructive commands
  - dry-run style probes where possible
  - explicit blocklist for unsafe operations

## 10) MCP Tool Surface (Initial Proposal)
### Environment & Evidence
- `env_status()`
- `env_inventory()`
- `find_artifacts(patterns, roots)`
- `snapshot_environment()`

### ERAS MDB (Read-only)
- `eras_list_databases()`
- `eras_describe_mdb(path)`
- `eras_list_tables(path)`
- `eras_describe_table(path, table)`
- `eras_sample_rows(path, table, limit)`
- `eras_run_readonly_query(path, query_name, params)`

### OpenCities/PowerMap (Safe)
- `powermap_status()`
- `powermap_list_workspaces()`
- `powermap_list_scripts()`
- `powermap_run_safe_probe(probe_name, params)`
- `powermap_collect_capabilities()`

### Cross-domain Reporting
- `compare_eras_to_powermap(context)`
- `build_gap_report()`

## 11) Security Guardrails
- Read-only by default across the whole stack.
- No production MDB writes in MVP.
- Work on copied analysis artifacts for database inspection.
- Strict input validation for tool parameters and file paths.
- Redaction policy for secrets/credentials/licenses/sensitive paths in shareable reports.
- Audit trail per MCP tool call: who/when/inputs/output artifact refs.
- Feature flags for any capability beyond safe probes.

## 12) Traceability Requirements
- Every requirement gets an ID (`REQ-*`) and links to:
  1) source statement in kickoff/master docs,
  2) implementing component/tool,
  3) verification artifact/test.
- Every run produces a manifest with:
  - timestamp, host fingerprint, script/tool version, output artifact paths, hash summary.
- Suggested minimum requirement map:
  - `REQ-ENV-001` environment inventory
  - `REQ-ART-001` artifact discovery
  - `REQ-MDB-001` MDB schema extraction
  - `REQ-PWM-001` automation surface inventory
  - `REQ-SEC-001` read-only default
  - `REQ-TRC-001` evidence indexing

## 13) Test Strategy (Initial)
- Unit tests:
  - path validation, query allowlist enforcement, parser/report formatters, redaction functions.
- Integration tests:
  - scanner runs on fixture directories
  - MDB adapter on fixture/sample DB
  - MCP tool contract tests (input/output schema + safety behavior)
- Safety tests:
  - assert blocked dangerous commands
  - assert no write operation available in MVP route map
- Replayability checks:
  - compare expected artifact structure across repeated runs.

## 14) Delivery Plan (High-Level)
1. Phase 0: project skeleton + baseline docs + security/test conventions.
2. Phase 1: Windows and artifact inventory pipeline.
3. Phase 2: ERAS MDB readonly extraction/reporting.
4. Phase 3: OpenCities automation-surface discovery and safe probes.
5. Phase 4: MCP integration + tool contracts + evidence engine.
6. Phase 5: MVP hardening, acceptance review, and handoff.

## 15) Risks (Initial)
- Incomplete visibility due to enterprise restrictions or missing permissions.
- Unknown/undocumented automation channels in OpenCities stack.
- MDB locking/corruption/compatibility issues during read-only analysis.
- Overly broad artifact scans causing noise or sensitive leakage in reports.
- Scope creep into write automation before guardrails and evidence maturity.

## 16) Dependencies
- Access to target Windows workstation and execution rights for non-destructive inventory scripts.
- Availability/licensing of OpenCities Map / MicroStation environment.
- Availability of ERAS MDB files (or approved copies) for analysis.
- Python/runtime and OS-level tooling required for scanner and adapter scripts.
- Agreement on security/redaction policy for stored evidence artifacts.

## 17) Open Questions for Next Review
- Which additional directories should be included/excluded beyond the two verified starting roots?
- Which identity/account should run scan tooling in production-like conditions?
- Should MDB analysis be limited to copied DB only, always?
- What is the approval workflow for enabling any non-read-only capability later?
- What is the expected artifact retention period and storage location policy?

## 18) Acceptance Criteria for This PRD Draft
- Contains required sections from kickoff/master asks.
- Distinguishes facts vs hypotheses vs questions vs decisions.
- Avoids claiming unverified environment facts.
- Provides implementable architecture/tool/guardrail direction for first cycles.
