# Risk Register v0.1

Last updated: 2026-04-24

## Facts Proved

- Safety constraints require read-only behavior by default.
- The project starts with incomplete knowledge of the target workstation.
- Current MVP baseline has partial MDB extraction and one active PowerMap gap.
- Current MDB ranking is candidate-only and must not be treated as an authoritative decision.
- Current human review pack keeps all MDB decisions in `candidate_ranking_only` state until reviewer input is recorded.
- Current decision workflow requires reviewer, UTC date, and decision basis before any accepted review is considered ready.
- Current decision intake writes only versioned review artifacts and leaves MDB files untouched.

## Hypotheses

- Primary delivery risk in early phases is incorrect assumptions about local environment/tooling.

## Open Questions

- Are there policy constraints blocking registry/process/service inventory commands?
- Are there proprietary plugins/macros requiring special handling?
- Which discovered ERAS MDB is authoritative?

## Decisions

- Maintain this register as a living artifact and link each risk to mitigation evidence.

## Active Risks

| ID | Level | Risk | Trigger | Mitigation | Acceptance / Exit | Evidence |
|---|---|---|---|---|---|---|
| R-001 | High | Environment assumptions are wrong | Scan findings contradict kickoff assumptions | Treat kickoff items as hypotheses until observed on host | Verified inventory report reviewed | `EVIDENCE_INDEX.md#ev-001` |
| R-002 | High | Accidental write to production MDB | Any workflow connects directly with write-capable mode | Copy-first workflow and read-only connection enforcement | Logged checks prove no-write operations | `EVIDENCE_INDEX.md#ev-003` |
| R-003 | High | Destructive OpenCities automation side effects | Probe actions mutate project/drawing state | Restrict to safe read probes and explicit denylist | Probe evidence contains only non-mutating operations | `EVIDENCE_INDEX.md#ev-002` |
| R-004 | Medium | Incomplete evidence traceability | Findings cannot be linked to reproducible artifact | Enforce evidence ID and path convention | All key claims map to evidence IDs | `EVIDENCE_INDEX.md#ev-007` |
| R-005 | Medium | Test blind spots in guardrails | Safety controls exist but are untested | Add dedicated guardrail verification in test plan | Guardrail checks pass in CI/local validation | `EVIDENCE_INDEX.md#ev-005` |
| R-006 | Medium | Parallel work causes scope collision | Multiple workers edit overlapping files | Define ownership and avoid touching out-of-scope files | No merge conflicts in owned doc set | `artifacts/logs/` (planned) |
| R-007 | Medium | Raw MDB or generated evidence is committed | Git status shows MDB/raw artifacts staged | `.gitignore` excludes raw artifacts and Access DB files; run ignored-file checks before commit | `git status --ignored --short` shows raw artifacts ignored, not staged | `EVIDENCE_INDEX.md#ev-007` |
| R-008 | Medium | MDB schema extraction is incomplete | ODBC UTF-16 warnings remain on 32 analyses | Treat as P1 triage, not MVP blocker; document partial extraction limits | Warning cases classified or remediated | `EVIDENCE_INDEX.md#ev-003` |
| R-009 | Medium | Python Manager capability is missed | Read-only scan does not find Python Manager | Manual check of launcher/install media and additional roots | Presence/absence confirmed with evidence | `EVIDENCE_INDEX.md#ev-002` |
| R-010 | Medium | MCP output contract drift | Tool responses omit envelope metadata | Tests assert `read_only`, `source_artifact`, `generated_at_utc`, `warnings`, and `counts` | Unit tests pass | `EVIDENCE_INDEX.md#ev-008` |
| R-011 | Medium | Candidate score is mistaken for authoritative selection | Downstream code treats rank 1 as final truth | Add `decision_status=candidate_ranking_only` and keep validation backlog item open | Reports and API clearly label candidate-only status | `EVIDENCE_INDEX.md#ev-009` |
| R-012 | Medium | Metadata-only ranking misses business semantics | High score comes from path/table metadata but not actual workflow usage | Require human validation before semantic modeling or cross-domain checks | Top candidates reviewed with stakeholder/process evidence | `EVIDENCE_INDEX.md#ev-009` |
| R-013 | Medium | Human review pack becomes stale | New scans or exports are generated after the review pack date | Regenerate review pack from current scorecard before using decisions | Review pack date and source artifacts match current cycle | `EVIDENCE_INDEX.md#ev-010` |
| R-014 | Medium | Ambiguous MDB counts create false exclusions | Unique analysis path/key counts are mistaken for total candidates | Expose `eras_candidate_count`, `eras_unique_analysis_path_count`, and `eras_unique_analysis_key_count`; retain 54 source candidate rows in review docs | CLI/API and docs show all counts explicitly | `EVIDENCE_INDEX.md#ev-010` |
| R-015 | Medium | Human decision file contains incomplete acceptances | A row is changed to `accept_review` without reviewer, date, or basis | `eras-review-status` warns and keeps global state out of `human_review_ready` | Incomplete accepted rows are rejected by validation counts | `EVIDENCE_INDEX.md#ev-011` |
| R-016 | Medium | Decision intake accidentally records the wrong candidate | Reviewer supplies an incorrect but valid `source_path` | Support `--dry-run`, echo previous/updated rows, and keep write scope limited to review artifacts | Dry-run can preview the exact row before write | `EVIDENCE_INDEX.md#ev-012` |

## Review Cadence

- Minimum: once per delivery cycle.
- Mandatory updates when new evidence invalidates or confirms assumptions.
