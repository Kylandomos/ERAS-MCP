# ERAS MDB Risks

_Generated (UTC): 2026-04-23T10:50:35.644548+00:00_

## Current Risks

- ODBC schema read failed: 'utf-16-le' codec can't decode bytes in position 72-73: illegal UTF-16 surrogate

## Safety Guarantees

- Source databases are copied before analysis.
- SQL helpers are restricted to read-only SELECT/WITH queries.
- No compact/repair/migration operation is performed.
