# Security Guardrails v0.1

Last updated: 2026-04-23

## Facts Proved

- Project kickoff mandates read-only by default and non-destructive behavior in early phases.
- Production MDB modification is explicitly disallowed during initial discovery.

## Hypotheses

- The target environment may include sensitive paths, credentials, and operational data requiring redaction.

## Open Questions

- Which local compliance rules govern artifact retention and redaction?
- Are there host-level controls limiting script execution/log collection?

## Decisions

- Enforce copy-first and read-only workflow for MDB analysis.
- Treat all host scans as potentially sensitive; redact before sharing.
- Block any destructive capability unless explicitly approved in future phases.
- Keep raw MDB files, raw scans, logs, generated exports, and analysis copies out of Git.

## Guardrails (Mandatory)

1. Read-only defaults for all discovery and MDB tooling.
2. No direct write to source `.mdb`; only analysis on controlled copy.
3. No delete/modify operations against project/drawing assets in probe workflows.
4. Evidence logging required for every scan/probe execution.
5. Redaction of secrets, license keys, and personal identifiers in published reports.
6. MCP facade tools are artifact-backed by default and must not execute Bentley/OpenCities commands.
7. MCP responses include trace metadata: `read_only`, `source_artifact`, `generated_at_utc`, `warnings`, and `counts`.

## Verification Checklist (v0.1)

- [ ] A documented no-write assertion exists for MDB analysis workflows.
- [ ] A documented safe-action-only list exists for OpenCities probes.
- [ ] Evidence index references each control and its validation artifact.
- [ ] Risk register includes explicit risks for write/destructive behavior.
- [ ] `.gitignore` excludes Access DB files and raw/generated artifact directories.
- [ ] Unit tests assert read-only SQL guardrails and MCP response envelope metadata.

## Planned Evidence

- `docs/evidence/ev-004-security-guardrails.md`
- `docs/reports/security_control_checklist_v0_1.md`
- `artifacts/logs/guardrail_validation_*.log`
