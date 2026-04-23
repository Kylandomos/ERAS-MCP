# MVP Gap Report

Generated: 2026-04-23

## Facts Proved

- The read-only MCP facade reports one active gap from current artifacts.
- The gap is artifact-derived from the latest PowerMap inventory.

## Active Gaps

| Area | Gap | Suggested action | Priority |
|---|---|---|---|
| PowerMap | Python Manager executable not found by read-only scan. | Inspect OpenCities installation media or app launcher settings manually. | P1 |
| ERAS MDB | 32 MDB schema analyses reported UTF-16 ODBC decode warnings. | Investigate driver/encoding behavior and identify authoritative databases before deeper semantic modeling. | P1 |

## Non-Blocking MVP Decision

- The MVP read-only baseline is not blocked by these gaps because core inventory, MDB discovery, partial schema extraction, and MCP artifact tools are functional.
- No write operation or active Bentley/OpenCities automation is introduced to work around these gaps.

