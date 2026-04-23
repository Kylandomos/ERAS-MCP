# PLAN - ERAS/OpenCities MCP Delivery Plan (v0)

## 1) Planning Baseline
- Version: `0.1-draft`
- Date: `2026-04-23`
- Scope of this plan: Windows-first reverse-engineering to safe MVP.
- Inputs:
  - `MASTER_PROMPT_Codex_Orchestrator.md`
  - `ERAS_OpenCitiesMap_MCP_Kickoff.md`

## 2) Planning Assumptions
- [FACT-DOC] Priority order is: understand -> document -> secure -> structure -> develop.
- [DEC] No production writes in MVP for ERAS MDB or OpenCities automation.
- [FACT-LOCAL] Verified starting ERAS scan root exists: `C:\AppSogelink\ERAS_Connect_2026` (`Test-Path` returned `True` / `FileSystem` directory).
- [FACT-LOCAL] Verified starting MapPowerView scan root exists: `C:\Program Files\Bentley\OpenCities Map PowerView 2023\MapPowerView` (`Test-Path` returned `True` / `FileSystem` directory).
- [HYP] Required access rights will permit non-destructive host inventory and local file discovery.
- [Q] Final scan boundaries and data-retention policies remain to be confirmed.

## 2.1) Delivered Baseline After Cycle 1
- [FACT-LOCAL] Read-only Windows/PowerMap inventory tooling exists and has produced bounded scan artifacts.
- [FACT-LOCAL] ERAS MDB discovery found `54` MDB/ACCDB candidates under `C:\AppSogelink\ERAS_Connect_2026`.
- [FACT-LOCAL] Copy-first MDB analysis produced `54/54` hash-matching analysis copies.
- [FACT-LOCAL] MDB schema extraction is partial: `183` table rows across `20` databases, with `32` ODBC UTF-16 warnings.
- [FACT-LOCAL] Read-only MCP facade and CLI exist under `src/mcp_server/`, with `mcp==1.27.0` and `pyodbc==5.3.0`.
- [FACT-LOCAL] Unit test suite currently covers `13` read-only safety/facade behaviors.
- [DEC] Raw scans, logs, generated exports, and MDB analysis copies remain local-only; curated docs under `docs/` are versioned.

## 3) Recommended Execution Order
1. Documentation/security baseline
2. Windows/environment inventory
3. ERAS MDB readonly analysis
4. OpenCities automation-surface discovery
5. MCP skeleton and tool contracts
6. Hardening, validation, and MVP sign-off

## 4) Phase Plan
## Phase 0 - Foundation and Guardrails
- Objective: establish controlled project baseline and review criteria.
- Dependencies: kickoff/master docs only.
- Work packages:
  - WP0.1 Draft PRD/PLAN/risk/test/security docs
  - WP0.2 Define evidence naming and traceability IDs
  - WP0.3 Define safety policy (readonly/default-deny for dangerous ops)
- Acceptance criteria:
  - baseline docs exist and are internally consistent
  - truth labeling (fact/hyp/question/decision) is present
  - initial review checklist is agreed
- Risks:
  - ambiguity in policy details delaying next phases

## Phase 1 - Windows and Artifact Inventory
- Objective: produce reproducible environment map of target workstation.
- Dependencies: Phase 0 guardrails/output schema + availability of verified starting roots.
- Work packages:
  - WP1.0 Initialize scan roots from verified local directories: `C:\AppSogelink\ERAS_Connect_2026` and `C:\Program Files\Bentley\OpenCities Map PowerView 2023\MapPowerView`
  - WP1.1 Windows version/user/rights/software/process/service inventory
  - WP1.2 Registry/environment variable and workspace/config discovery
  - WP1.3 Artifact search for MDB/DGN/scripts/config/log/export files
  - WP1.4 Normalize outputs into evidence manifests and reports
- Acceptance criteria:
  - at least one full inventory run archived with timestamp
  - artifacts index generated with verified starting roots plus explicitly added roots/patterns
  - sensitive fields redaction path validated
- Risks:
  - permission-denied paths and enterprise hardening
  - noisy scans requiring scope tightening

## Phase 2 - ERAS MDB Readonly Reverse Engineering
- Objective: extract trustworthy structural visibility from MDB without writes.
- Dependencies: Phase 1 artifact discovery and DB candidate paths.
- Work packages:
  - WP2.1 Identify MDB candidates and produce file fingerprints
  - WP2.2 Create analysis copy workflow
  - WP2.3 Extract tables/fields/indexes/row counts
  - WP2.4 Generate schema, dictionary, relationships, sample query docs
- Acceptance criteria:
  - schema outputs generated from at least one MDB copy
  - no write operation executed against source DB
  - uncertain inferences explicitly labeled
- Risks:
  - locked/corrupted DBs
  - unsupported providers/drivers in target environment

## Phase 3 - OpenCities/MicroStation Automation Surface Discovery
- Objective: map practical safe automation capabilities on real host.
- Dependencies: Phase 1 environment evidence.
- Work packages:
  - WP3.1 Detect installation/version/workspace/workset paths
  - WP3.2 Inventory Python scripts, examples, macros, key-ins, extensions
  - WP3.3 Execute safe probes (non-destructive) and capture proof outputs
  - WP3.4 Document gaps and fallback options
- Acceptance criteria:
  - capability matrix produced with evidence references
  - safe probe list curated and validated
  - blocked/unknown capabilities clearly documented
- Risks:
  - automation APIs partially unavailable
  - headless execution constraints

## Phase 4 - MCP Core Skeleton and Tool Wiring
- Objective: expose core readonly/inspection capabilities via MCP.
- Dependencies: validated outputs from Phases 1-3.
- Work packages:
  - WP4.1 Implement MCP server scaffold and tool contracts
  - WP4.2 Connect environment scanner and artifact discovery tools
  - WP4.3 Connect ERAS readonly adapter tools
  - WP4.4 Connect powermap capability/probe tools
  - WP4.5 Integrate evidence engine and standardized result envelopes
- Acceptance criteria:
  - core tool list callable end-to-end
  - structured outputs + logs produced per invocation
  - safety controls enforce readonly/default-deny
- Risks:
  - contract drift between adapters and MCP schemas

## Phase 5 - MVP Validation and Handoff
- Objective: package and validate MVP against acceptance criteria.
- Dependencies: operational Phase 4 build.
- Work packages:
  - WP5.1 Unit/integration/safety test pass
  - WP5.2 Traceability matrix completion
  - WP5.3 Risk register and known-limits refresh
  - WP5.4 Reviewer walkthrough and go/no-go
- Acceptance criteria:
  - MVP criteria from kickoff satisfied
  - test evidence attached
  - unresolved risks/questions explicitly tracked
- Risks:
  - hidden environment constraints discovered late

## 5) Next-Cycle Tasks (Actionable Now)
1. Initialize Git baseline on branch `main` and configure remote `https://github.com/Kylandomos/ERAS-MCP`.
2. Commit code, docs, tests, requirements, and curated evidence reports only.
3. Keep `.gitignore` blocking raw MDBs, raw inventories, logs, generated exports, and analysis copies.
4. Validate packaging with `eras-mcp-readonly env-status` and `eras-mcp-readonly build-gap-report`.
5. Promote the two non-blocking gaps to P1 work: MDB UTF-16 warnings and Python Manager discovery.

## 6) Review Gates
### Gate G0 (after Phase 0)
- Docs baseline complete (`PRD`, `PLAN`, risk/test/security scaffolds).
- Truth labeling and non-claim policy enforced.
- Approval to run non-destructive scans.

### Gate G1 (after Phase 1)
- Environment inventory evidence is reproducible and timestamped.
- Artifact index quality reviewed; scan scope tuned.
- Approval to proceed with MDB copy-and-analyze workflow.

### Gate G2 (after Phase 2)
- MDB analysis outputs generated from copy and reviewed.
- No write-path observed; readonly policy verified.
- Approval to integrate DB adapter behavior into MCP contracts.

### Gate G3 (after Phase 3)
- OpenCities capability map reviewed with proof links.
- Safe probe list approved; unsafe ops explicitly blocked.
- Approval for MCP integration/hardening.

### Gate G4 (after Phase 5)
- MVP acceptance criteria met with test evidence.
- Known limits and next-step backlog accepted.

## 7) Dependencies Matrix (Condensed)
- Phase 1 depends on: Phase 0 policies and templates.
- Phase 2 depends on: Phase 1 discovered MDB paths and access.
- Phase 3 depends on: Phase 1 discovered OpenCities artifacts.
- Phase 4 depends on: Phase 2 and Phase 3 stable interfaces.
- Phase 5 depends on: Phase 4 integrated toolchain and tests.

## 8) Quick Wins
- Standardize evidence manifest format early.
- Ship readonly MDB table/column listing as first useful capability.
- Expose `env_status()` and `env_inventory()` early for immediate value.
- Produce initial capability matrix even if partial, with explicit gaps.
- Package the read-only CLI so it can run without setting `PYTHONPATH`.
- Lock the current evidence baseline in Git without committing raw MDB data.

## 9) MVP Definition
MVP = usable local MCP that can:
- inventory Windows/OpenCities/ERAS environment,
- analyze at least one ERAS MDB in readonly mode,
- expose core MCP inspection tools with logs and guardrails,
- produce traceable evidence artifacts for human review.

## 10) Post-MVP Priorities
1. Add richer cross-domain checks (drawing/data consistency).
2. Add guided, approval-gated write operations (if and only if approved).
3. Improve performance and incremental scans.
4. Expand test fixtures and regression suite.
5. Add operational packaging/deployment conventions for wider rollout.

## 11) Known Planning Limits (Current Draft)
- Only directory existence, read-only artifact inventory, and current extracted counts are validated.
- Python Manager absence is a scan finding, not proof that the feature is unavailable in the product.
- MDB schema extraction is partial until the 32 ODBC warning cases are resolved or classified.
- Final authoritative ERAS MDB selection remains open.
