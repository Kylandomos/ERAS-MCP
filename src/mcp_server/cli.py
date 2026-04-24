from __future__ import annotations

import argparse
import json
import sys
from typing import Any

from .facade import MCPFacade
from .server import run_mcp_stdio_server


def _dump_json(payload: dict[str, Any]) -> None:
    print(json.dumps(payload, indent=2, ensure_ascii=False, default=str))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="eras-mcp-readonly",
        description="Read-only facade over ERAS/OpenCities scanner artifacts.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("env-status", help="Summarize environment/artifact status.")

    env_inventory_parser = subparsers.add_parser(
        "env-inventory", help="Load latest or list inventory snapshots."
    )
    env_inventory_parser.add_argument(
        "--all",
        action="store_true",
        help="List inventory summaries instead of returning latest payload.",
    )

    find_artifacts_parser = subparsers.add_parser(
        "find-artifacts", help="Safe bounded artifact search."
    )
    find_artifacts_parser.add_argument(
        "--patterns",
        nargs="*",
        default=None,
        help="Glob patterns (e.g., *.mdb *.cfg).",
    )
    find_artifacts_parser.add_argument(
        "--roots",
        nargs="*",
        default=None,
        help="Optional roots. Requests outside allowed bounds are rejected.",
    )

    subparsers.add_parser("eras-list-databases", help="List discovered ERAS databases.")
    eras_list_tables_parser = subparsers.add_parser(
        "eras-list-tables", help="List ERAS table rows from export artifact."
    )
    eras_list_tables_parser.add_argument(
        "--database-filter",
        default=None,
        help="Case-insensitive substring filter on database path.",
    )
    eras_rank_parser = subparsers.add_parser(
        "eras-rank-databases",
        help="Rank ERAS MDB candidates using metadata-only scoring.",
    )
    eras_rank_parser.add_argument(
        "--limit",
        type=int,
        default=10,
        help="Maximum ranked candidates to return when --all is not set.",
    )
    eras_rank_parser.add_argument(
        "--all",
        action="store_true",
        help="Return every ranked candidate.",
    )
    eras_explain_parser = subparsers.add_parser(
        "eras-explain-database",
        help="Explain one ranked ERAS MDB candidate using metadata only.",
    )
    eras_explain_parser.add_argument(
        "--path",
        required=True,
        help="Full source_path or analysis_path of the MDB candidate to explain.",
    )
    subparsers.add_parser(
        "eras-review-status",
        help="Validate ERAS MDB human review decisions.",
    )
    set_review_parser = subparsers.add_parser(
        "eras-set-review-decision",
        help="Set one ERAS MDB human review decision in the versioned CSV.",
    )
    set_review_parser.add_argument(
        "--source-path",
        required=True,
        help="Exact source_path from the human decision CSV.",
    )
    set_review_parser.add_argument(
        "--status",
        required=True,
        choices=["needs_followup", "accept_review", "reject_review"],
        help="Human review status to set.",
    )
    set_review_parser.add_argument(
        "--reviewer",
        default="",
        help="Reviewer identity. Required for accept_review and reject_review.",
    )
    set_review_parser.add_argument(
        "--decision-basis",
        default="",
        help="Human decision basis. Required for accept_review and reject_review.",
    )
    set_review_parser.add_argument(
        "--notes",
        default="",
        help="Optional reviewer notes.",
    )
    set_review_parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Validate and show the planned change without writing files.",
    )
    subparsers.add_parser("powermap-status", help="Summarize PowerMap inventory status.")
    subparsers.add_parser(
        "powermap-list-workspaces", help="List PowerMap workspace path candidates."
    )
    subparsers.add_parser("build-gap-report", help="Build consolidated artifact gap report.")
    subparsers.add_parser(
        "serve-mcp",
        help="Run MCP stdio server if optional `mcp` dependency is installed.",
    )

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    facade = MCPFacade()

    if args.command == "env-status":
        _dump_json(facade.env_status())
        return 0
    if args.command == "env-inventory":
        _dump_json(facade.env_inventory(latest=not args.all))
        return 0
    if args.command == "find-artifacts":
        _dump_json(facade.find_artifacts(patterns=args.patterns, roots=args.roots))
        return 0
    if args.command == "eras-list-databases":
        _dump_json(facade.eras_list_databases())
        return 0
    if args.command == "eras-list-tables":
        _dump_json(facade.eras_list_tables(database_filter=args.database_filter))
        return 0
    if args.command == "eras-rank-databases":
        _dump_json(facade.eras_rank_databases(limit=args.limit, include_all=args.all))
        return 0
    if args.command == "eras-explain-database":
        _dump_json(facade.eras_explain_database(database_path=args.path))
        return 0
    if args.command == "eras-review-status":
        _dump_json(facade.eras_review_status())
        return 0
    if args.command == "eras-set-review-decision":
        result = facade.eras_set_review_decision(
            source_path=args.source_path,
            status=args.status,
            reviewer=args.reviewer,
            decision_basis=args.decision_basis,
            notes=args.notes,
            dry_run=args.dry_run,
        )
        _dump_json(result)
        return 0 if result.get("success") else 1
    if args.command == "powermap-status":
        _dump_json(facade.powermap_status())
        return 0
    if args.command == "powermap-list-workspaces":
        _dump_json(facade.powermap_list_workspaces())
        return 0
    if args.command == "build-gap-report":
        _dump_json(facade.build_gap_report())
        return 0
    if args.command == "serve-mcp":
        try:
            run_mcp_stdio_server(facade=facade)
        except RuntimeError as exc:
            print(str(exc), file=sys.stderr)
            return 2
        return 0

    parser.print_help()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
