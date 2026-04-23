# EV-008 - Read-Only MCP Facade

Status: validated

## Claim Supported

The MVP exposes a read-only artifact-backed MCP facade and CLI.

## Evidence

- Facade implementation: `src/mcp_server/facade.py`
- MCP stdio registration: `src/mcp_server/server.py`
- CLI entry point: `pyproject.toml`
- Unit tests: `tests/unit/test_mcp_facade_readonly.py`

## Facts Proved

- `create_mcp_stdio_server()` returns a `FastMCP` object when dependencies are installed.
- CLI commands `env-status` and `build-gap-report` run against current artifacts.
- Tool responses include standard metadata: `read_only`, `source_artifact`, `generated_at_utc`, `warnings`, and `counts`.

