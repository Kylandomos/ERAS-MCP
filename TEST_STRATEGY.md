# Test Strategy v0.1 (Windows-First, Read-Only by Default)

Last updated: 2026-04-23

## Facts Proved

- Early project phases prioritize inventory, schema introspection, and documentation.
- Safety and traceability are mandatory acceptance dimensions.
- Current unit suite has `13` passing tests for SQL safety, artifact selection, bounded search, PowerMap artifact reading, and MCP response envelopes.

## Hypotheses

- Most early failures will come from environment variability, not business logic complexity.

## Open Questions

- Which tests can run on developer machines without target software installed?
- What minimal fixture set is needed for MDB schema validation?

## Decisions

- Test plan emphasizes guardrails and reproducibility before feature breadth.
- Packaging smoke tests are required for `eras-mcp-readonly env-status` and `eras-mcp-readonly build-gap-report`.

## Test Levels

1. Unit tests (`tests/unit`): path handling, output schema normalization, guardrail helpers.
2. Integration tests (`tests/integration`): scanner/adapters against safe fixtures and mock responses.
3. Smoke checks (manual + scripted): verify no destructive operations are exposed by default.

## Critical Safety Assertions

- No write-capable MDB calls in default configuration.
- No mutating OpenCities probe exposed in default tool surface.
- Every report output includes timestamp and evidence reference.
- MCP facade responses include `read_only`, `source_artifact`, `generated_at_utc`, `warnings`, and `counts`.
- Git safety checks confirm raw Access databases and raw/generated artifacts are ignored before commit.

## Minimum Acceptance Criteria (v0.1)

- Test inventory includes at least one explicit guardrail assertion per critical area (Windows scan, MDB, PowerMap).
- Failure outputs clearly indicate violated safety rule.
- Evidence-producing paths are deterministic and documented.
- `python -m unittest discover -s tests/unit -p "test_*.py"` passes.
- PowerShell parser checks pass for both read-only inventory scripts.

## Planned Evidence Links

- `docs/reports/test_matrix_v0_1.md` (planned)
- `artifacts/logs/test_run_*.log` (planned)
- `docs/evidence/ev-005-test-strategy-validation.md` (validated)
