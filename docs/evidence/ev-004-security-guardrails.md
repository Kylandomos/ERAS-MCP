# EV-004 - Security Guardrails

Status: validated

## Claim Supported

The MVP read-only baseline excludes production writes, raw MDB versioning, and active Bentley/OpenCities command execution.

## Evidence

- Guardrails document: `SECURITY_GUARDRAILS.md`
- Git ignore policy: `.gitignore`
- MCP facade implementation: `src/mcp_server/facade.py`
- Read-only query guard tests: `tests/unit/test_eras_mdb_query_safety.py`

## Facts Proved

- `.gitignore` excludes Access files, raw inventories, logs, generated exports, and MDB analysis copies.
- Freeform ERAS SQL helper allows only read-only `SELECT`/`WITH` statements.
- MCP facade reads existing artifacts by default and does not rerun scans or execute Bentley commands.

