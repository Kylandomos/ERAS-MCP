# Architecture Baseline v0.1

Last updated: 2026-04-23

## Facts Proved (Current State)

- The kickoff documents define a target architecture with scanner, adapters, MCP server, and evidence/reporting outputs.
- The repository contains directory placeholders for the intended layers (`scripts`, `src`, `tests`, `artifacts`, `docs`).
- The MVP read-only facade is implemented under `src/mcp_server/` and reads existing artifacts by default.
- The CLI entry point is packaged as `eras-mcp-readonly`.

## Hypotheses

- OpenCities/MicroStation and ERAS integration can be represented through separate adapters with a shared evidence service.
- A read-only-first contract can be enforced consistently across tools.

## Open Questions

- Which local APIs/automation hooks are actually available for OpenCities Map on this workstation?
- Which MDB access technology is most stable on this environment (ODBC/OLEDB/Access engine)?
- What minimum MCP toolset is feasible for MVP without elevated privileges?
- Which response schema should be frozen for downstream MCP clients after the MVP baseline?

## Decisions

- Keep architecture modular and testable from day one.
- Separate discovery/probing from any future write-capable workflows.
- Treat evidence generation as a first-class cross-cutting concern.

## Target Logical Components

1. Environment Scanner (`scripts/windows_scan`, `src/services`): reproducible host discovery.
2. OpenCities/PowerMap Adapter (`src/adapters/powermap`): safe capability inspection and probes.
3. ERAS MDB Adapter (`src/adapters/eras_mdb`): read-only schema and sample data access.
4. Evidence Service (`src/services` + `artifacts` + `docs/evidence`): traceable outputs and indexing.
5. MCP Server (`src/mcp_server`): tool exposure, guardrails, and standardized responses.
6. Test Suite (`tests`): unit and integration gates for read-only safety and output quality.

## MVP Response Envelope

Read-only MCP facade responses include these common fields:

- `read_only`
- `source_artifact`
- `generated_at_utc`
- `warnings`
- `counts`

Tool-specific payload fields remain present for backward compatibility.

## Proposed Interaction Flow (v0)

1. Inventory host and application surface.
2. Persist raw outputs in `artifacts/`.
3. Normalize key findings in `docs/reports/`.
4. Update evidence index with references.
5. Expose selected findings via MCP tools.

## Evidence Targets

- `artifacts/inventories/windows_scan_*/inventory.json` (local-only raw evidence)
- `artifacts/snapshots/environment_snapshot_*.json` (local-only raw evidence)
- `docs/reports/powermap_capabilities_*.md`
- `docs/schemas/eras_mdb_schema_*.json`
- `docs/evidence/*.md` (trace records)

## Acceptance Criteria (v0.1 Architecture)

- Clear component boundaries documented for scanner, adapters, MCP server, and evidence.
- Explicit read-only safety boundary documented for MDB and PowerMap interactions.
- Identified unknowns listed as open questions, not represented as facts.
