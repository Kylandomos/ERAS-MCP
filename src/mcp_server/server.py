from __future__ import annotations

from typing import Any

from .facade import MCPFacade


def create_mcp_stdio_server(
    facade: MCPFacade | None = None,
) -> tuple[Any | None, str | None]:
    """Create an MCP stdio server when the `mcp` package is available."""

    try:
        from mcp.server.fastmcp import FastMCP  # type: ignore[import-not-found]
    except Exception as exc:
        return None, (
            "Optional dependency `mcp` is not installed; "
            "MCP stdio server mode is unavailable. "
            f"Import error: {exc}"
        )

    active_facade = facade or MCPFacade()
    server = FastMCP("eras-opencities-readonly")

    @server.tool()
    def env_status() -> dict[str, Any]:
        return active_facade.env_status()

    @server.tool()
    def env_inventory(latest: bool = True) -> dict[str, Any]:
        return active_facade.env_inventory(latest=latest)

    @server.tool()
    def find_artifacts(
        patterns: list[str] | None = None,
        roots: list[str] | None = None,
    ) -> dict[str, Any]:
        return active_facade.find_artifacts(patterns=patterns, roots=roots)

    @server.tool()
    def eras_list_databases() -> dict[str, Any]:
        return active_facade.eras_list_databases()

    @server.tool()
    def eras_list_tables(database_filter: str | None = None) -> dict[str, Any]:
        return active_facade.eras_list_tables(database_filter=database_filter)

    @server.tool()
    def eras_rank_databases(
        limit: int = 10, include_all: bool = False
    ) -> dict[str, Any]:
        return active_facade.eras_rank_databases(
            limit=limit,
            include_all=include_all,
        )

    @server.tool()
    def eras_explain_database(source_path: str) -> dict[str, Any]:
        return active_facade.eras_explain_database(database_path=source_path)

    @server.tool()
    def eras_review_status() -> dict[str, Any]:
        return active_facade.eras_review_status()

    @server.tool()
    def eras_set_review_decision(
        source_path: str,
        status: str,
        reviewer: str = "",
        decision_basis: str = "",
        notes: str = "",
        dry_run: bool = False,
    ) -> dict[str, Any]:
        return active_facade.eras_set_review_decision(
            source_path=source_path,
            status=status,
            reviewer=reviewer,
            decision_basis=decision_basis,
            notes=notes,
            dry_run=dry_run,
        )

    @server.tool()
    def powermap_status() -> dict[str, Any]:
        return active_facade.powermap_status()

    @server.tool()
    def powermap_list_workspaces() -> dict[str, Any]:
        return active_facade.powermap_list_workspaces()

    @server.tool()
    def build_gap_report() -> dict[str, Any]:
        return active_facade.build_gap_report()

    return server, None


def run_mcp_stdio_server(facade: MCPFacade | None = None) -> None:
    server, error = create_mcp_stdio_server(facade=facade)
    if server is None:
        raise RuntimeError(error or "Failed to initialize MCP stdio server.")

    try:
        server.run(transport="stdio")
    except TypeError:
        server.run()
