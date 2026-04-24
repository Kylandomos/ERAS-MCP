"""Read-only MCP skeleton/facade for ERAS/OpenCities artifacts."""

from .facade import (
    MCPFacade,
    build_gap_report,
    env_inventory,
    env_status,
    eras_explain_database,
    eras_list_databases,
    eras_rank_databases,
    eras_review_status,
    eras_list_tables,
    find_artifacts,
    powermap_list_workspaces,
    powermap_status,
)
from .server import create_mcp_stdio_server, run_mcp_stdio_server

__all__ = [
    "MCPFacade",
    "build_gap_report",
    "create_mcp_stdio_server",
    "env_inventory",
    "env_status",
    "eras_explain_database",
    "eras_list_databases",
    "eras_rank_databases",
    "eras_review_status",
    "eras_list_tables",
    "find_artifacts",
    "powermap_list_workspaces",
    "powermap_status",
    "run_mcp_stdio_server",
]
