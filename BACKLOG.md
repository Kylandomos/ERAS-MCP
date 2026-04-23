# Backlog v0.1 (Prioritized)

Last updated: 2026-04-23

## Facts Proved

- Kickoff requires scan-first execution before advanced automation.
- Security posture is read-only by default and evidence-driven.
- Cycle 1 delivered a read-only scanner, partial MDB schema extraction, and an artifact-backed MCP facade.
- Current MDB evidence: `54` candidates, `54/54` hash matches, `183` table rows across `20` databases, `32` ODBC warnings.
- Current PowerMap evidence: Python Manager was not found by read-only scan.

## Hypotheses

- Early automation value can be delivered from inventory and schema introspection alone.

## Open Questions

- Which tasks require elevated permissions on the target host?
- Which inventory outputs are mandatory for stakeholder sign-off?
- Which discovered MDB is authoritative for ERAS business workflows?
- Is Python Manager absent or just not discovered by the bounded read-only scan?

## Decisions

- Prioritize observability, traceability, and safety controls before active automation.

## Priority Queue

| ID | Priority | Item | Acceptance Criteria | Evidence Reference |
|---|---|---|---|---|
| BL-001 | P0 | Baseline Windows environment scan spec | `ENVIRONMENT_SCAN.md` and `WINDOWS_INVENTORY.md` define required fields, exclusions, and outputs | `EVIDENCE_INDEX.md#ev-001` |
| BL-002 | P0 | OpenCities automation surface discovery plan | `POWEMAP_AUTOMATION_SURFACE.md` lists probe categories, safe actions, and unknowns | `EVIDENCE_INDEX.md#ev-002` |
| BL-003 | P0 | ERAS MDB read-only schema plan | `ERAS_MDB_SCHEMA.md` defines copy-first and no-write schema workflow | `EVIDENCE_INDEX.md#ev-003` |
| BL-004 | P0 | Security guardrails baseline | `SECURITY_GUARDRAILS.md` contains enforceable controls and verification checks | `EVIDENCE_INDEX.md#ev-004` |
| BL-005 | P1 | Test strategy baseline | `TEST_STRATEGY.md` includes non-destructive gates and minimum test matrix | `EVIDENCE_INDEX.md#ev-005` |
| BL-006 | P1 | Risk register initialization | `RISK_REGISTER.md` documents top delivery and safety risks with mitigations | `EVIDENCE_INDEX.md#ev-006` |
| BL-007 | P2 | Evidence indexing and naming convention | `EVIDENCE_INDEX.md` defines IDs, naming rules, and status lifecycle | `EVIDENCE_INDEX.md#ev-007` |
| BL-008 | P1 | Verify initial install roots | Disk verification records both roots as existing directories (`Exists=True`) using safe checks (`Test-Path`, `Get-Item`) | `EVIDENCE_INDEX.md#ev-001` |
| BL-009 | P0 | Git baseline and ignore policy | Local repo on `main` with remote configured; raw MDBs, raw scans, logs, generated exports, and analysis copies ignored | `EVIDENCE_INDEX.md#ev-007` |
| BL-010 | P0 | Read-only MCP packaging | `eras-mcp-readonly env-status` and `eras-mcp-readonly build-gap-report` run without setting `PYTHONPATH` | `EVIDENCE_INDEX.md#ev-008` |
| BL-011 | P1 | MDB warning triage | 32 UTF-16 ODBC warning cases are classified by file/path and mitigation path | `EVIDENCE_INDEX.md#ev-003` |
| BL-012 | P1 | PowerMap Python Manager follow-up | Python Manager absence is manually confirmed or alternate install/config path is documented | `EVIDENCE_INDEX.md#ev-002` |
| BL-013 | P1 | Authoritative MDB selection | Candidate MDB priority rule or stakeholder decision identifies the ERAS MDB(s) to use for semantic modeling | `EVIDENCE_INDEX.md#ev-003` |

## Exit Criteria for Backlog v0.1

- Every P0 item has a documented owner, acceptance criteria, and planned evidence artifact.
- No P0 item assumes capabilities without linking to a planned/proved evidence source.
