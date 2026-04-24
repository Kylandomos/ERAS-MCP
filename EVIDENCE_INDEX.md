# Evidence Index v0.1

Last updated: 2026-04-24

## Facts Proved

- Evidence traceability is a hard requirement from kickoff documents.
- Artifact directories for inventories, logs, snapshots, exports, and docs evidence are scaffolded.
- `EV-001` confirms both provided roots exist as FileSystem directories (`Exists=True` via `Test-Path` and `Get-Item`).
- Curated MVP evidence reports now exist under `docs/reports/` and `docs/schemas/`.
- Raw/generated artifacts remain local-only by Git ignore policy.
- ERAS MDB candidate ranking is tracked as candidate-only evidence, not an authoritative decision.
- ERAS MDB human review and ODBC warning triage are tracked without promoting rank `1` to an authoritative decision.
- ERAS MDB human decisions are initialized in a versioned CSV and validated by a read-only MCP/CLI tool.
- ERAS MDB decision intake can preview or write review decisions while keeping MDB files untouched.

## Hypotheses

- A lightweight evidence ID convention is sufficient for early-phase governance.

## Open Questions

- Should evidence metadata also be mirrored in machine-readable JSON/CSV?
- What retention policy should be applied to large raw scan artifacts?
- Should raw redacted inventory JSON ever be promoted into curated docs, or remain local-only?

## Decisions

- Use stable IDs (`EV-###`) and map each one to claim, source path, and status.
- Track evidence lifecycle with `planned`, `collected`, `validated`, `superseded`.

## Naming Convention

- Evidence markdown summary: `docs/evidence/ev-###-short-title.md`
- Raw scan artifacts: `artifacts/<type>/<name>_<YYYYMMDD_HHMMSS>.<ext>`
- Report derivatives: `docs/reports/<topic>_<YYYYMMDD>.md`

## Evidence Register

| ID | Claim Supported | Planned Artifact Path | Status | Owner |
|---|---|---|---|---|
| EV-001 | Baseline install roots exist on local disk as directories | `docs/evidence/ev-001-windows-scan-baseline.md` | validated | Worker A (recorded from orchestrator verification) |
| EV-002 | PowerMap automation surface is documented from observation | `docs/evidence/ev-002-powermap-surface.md` | validated | Current cycle |
| EV-003 | ERAS MDB schema derived via read-only workflow | `docs/evidence/ev-003-eras-mdb-schema.md` | validated-partial | Current cycle |
| EV-004 | Security guardrails are defined and checked | `docs/evidence/ev-004-security-guardrails.md` | validated | Current cycle |
| EV-005 | Test strategy includes guardrail verification | `docs/evidence/ev-005-test-strategy-validation.md` | validated | Current cycle |
| EV-006 | Risk register reflects active threats and mitigations | `docs/evidence/ev-006-risk-review.md` | validated | Current cycle |
| EV-007 | Evidence indexing process is consistently applied | `docs/evidence/ev-007-evidence-process-audit.md` | validated | Current cycle |
| EV-008 | Read-only MCP facade exposes artifact-backed inspection tools | `docs/evidence/ev-008-mcp-facade.md` | validated | Current cycle |
| EV-009 | ERAS MDB authoritative candidates are ranked from metadata-only evidence | `docs/evidence/ev-009-eras-authoritative-candidates.md` | validated-candidate-ranking | Current cycle |
| EV-010 | ERAS MDB candidate ranking is packaged for human review and ODBC warning triage | `docs/evidence/ev-010-eras-mdb-human-review-pack.md` | validated-review-pack | Current cycle |
| EV-011 | ERAS MDB human decision artifact is initialized and validated | `docs/evidence/ev-011-eras-mdb-human-decisions.md` | validated-decision-artifact-initialized | Current cycle |
| EV-012 | ERAS MDB human decision intake can validate and record review decisions | `docs/evidence/ev-012-eras-mdb-decision-intake.md` | validated-decision-intake | Current cycle |

## Latest Evidence Note

- `EV-001`:
  - `C:\AppSogelink\ERAS_Connect_2026` -> Exists=True, ItemType=Directory
  - `C:\Program Files\Bentley\OpenCities Map PowerView 2023\MapPowerView` -> Exists=True, ItemType=Directory
- `EV-003`:
  - MDB/ACCDB candidates: `54`
  - Hash-matching analysis copies: `54/54`
  - Extracted table rows: `183`
  - Databases with extracted tables: `20`
  - ODBC warning cases: `32`
- `EV-008`:
  - Unit tests: `39` passing
  - MCP stdio server factory initializes with `mcp==1.27.0`
  - CLI output envelope includes `read_only`, `source_artifact`, `generated_at_utc`, `warnings`, and `counts`
- `EV-009`:
  - Candidates ranked: `54`
  - Top-ranked candidate: `C:\AppSogelink\ERAS_Connect_2026\CLIENT\client.mdb`
  - Decision status: `candidate_ranking_only`
- `EV-010`:
  - Human review pack: `docs/reports/eras_mdb_candidate_review_20260423.md`
  - ODBC warning triage: `docs/reports/eras_mdb_odbc_warning_triage_20260423.md`
  - Candidate rows retained for review: `54`
  - Unique analysis path strings: `52`
  - Unique normalized analysis keys: `51`
  - Explanation CLI/API: `eras-explain-database`
- `EV-011`:
  - Human decision artifact: `docs/reviews/ERAS_MDB_HUMAN_DECISIONS_20260424.csv`
  - Decision status report: `docs/reports/eras_mdb_human_decision_status_20260424.md`
  - Decision rows: `54`
  - Default status: `needs_followup`
  - Validation CLI/API: `eras-review-status`
  - Current global status: `human_review_pending`
- `EV-012`:
  - Decision intake CLI/API: `eras-set-review-decision`
  - Dry-run preview: available through `--dry-run`
  - Write scope: decision CSV and decision status report only
  - Current global status remains: `human_review_pending`

## Acceptance Criteria (v0.1)

- Every governance/backlog item references at least one evidence ID.
- No factual claim in root docs is left without either a proved state or a planned evidence path.
