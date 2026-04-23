from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable


@dataclass(frozen=True)
class MdbTableStats:
    table_count: int = 0
    total_row_count: int = 0


@dataclass(frozen=True)
class MdbCandidateScore:
    rank: int
    score: int
    confidence: str
    source_path: str
    analysis_path: str
    file_size_bytes: int
    modified_utc: str
    hash_match: bool
    has_schema_warning: bool
    table_count: int
    total_row_count: int
    reasons: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        payload = asdict(self)
        payload["reasons"] = "; ".join(self.reasons)
        return payload


def _as_int(value: Any) -> int:
    if value is None or value == "":
        return 0
    try:
        return int(value)
    except (TypeError, ValueError):
        return 0


def _parse_datetime(value: str) -> datetime | None:
    if not value:
        return None
    normalized = value.replace("Z", "+00:00")
    try:
        parsed = datetime.fromisoformat(normalized)
    except ValueError:
        return None
    if parsed.tzinfo is None:
        return parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def _path_tokens(path: str) -> str:
    return path.replace("/", "\\").lower()


def _path_has_segment(path: str, segment: str) -> bool:
    token = f"\\{segment.lower()}\\"
    normalized = f"\\{_path_tokens(path)}\\"
    return token in normalized


def load_schema_warning_paths(schema_text: str) -> set[str]:
    warning_paths: set[str] = set()
    current_path: str | None = None
    for raw_line in schema_text.splitlines():
        line = raw_line.strip()
        if line.startswith("## Database: `") and line.endswith("`"):
            current_path = line.removeprefix("## Database: `").removesuffix("`")
            continue
        if "ODBC schema read failed" in line and current_path:
            warning_paths.add(current_path.lower())
    return warning_paths


def build_table_stats(table_rows: Iterable[dict[str, str]]) -> dict[str, MdbTableStats]:
    grouped: dict[str, list[dict[str, str]]] = {}
    for row in table_rows:
        database_path = row.get("database_path", "")
        if not database_path:
            continue
        grouped.setdefault(database_path.lower(), []).append(row)

    stats: dict[str, MdbTableStats] = {}
    for database_path, rows in grouped.items():
        total_row_count = sum(_as_int(row.get("row_count")) for row in rows)
        stats[database_path] = MdbTableStats(
            table_count=len(rows),
            total_row_count=total_row_count,
        )
    return stats


def score_mdb_candidate(
    discovery_row: dict[str, str],
    *,
    table_stats: MdbTableStats,
    has_schema_warning: bool,
    now_utc: datetime | None = None,
) -> tuple[int, str, list[str]]:
    now = now_utc or datetime.now(timezone.utc)
    source_path = discovery_row.get("source_path", "")
    analysis_path = discovery_row.get("analysis_path", "")
    combined_path = _path_tokens(f"{source_path}\\{analysis_path}")
    hash_match = str(discovery_row.get("hash_match", "")).lower() == "true"

    score = 0
    reasons: list[str] = []

    if hash_match:
        score += 20
        reasons.append("+20 hash match")
    else:
        reasons.append("+0 no hash match")

    if has_schema_warning:
        score -= 30
        reasons.append("-30 ODBC warning")

    if _path_has_segment(source_path, "client"):
        score += 20
        reasons.append("+20 CLIENT path")
    if _path_has_segment(source_path, "systeme"):
        score += 12
        reasons.append("+12 SYSTEME path")
    if _path_has_segment(source_path, "seed"):
        score -= 10
        reasons.append("-10 SEED path")

    for token in ("temp", "sample", "sheet"):
        if token in combined_path:
            score -= 20
            reasons.append(f"-20 {token} path/name")

    for token in ("modele", "dgn_sht"):
        if token in combined_path:
            score -= 10
            reasons.append(f"-10 {token} path/name")

    modified = _parse_datetime(discovery_row.get("modified_utc", ""))
    if modified:
        age_days = (now - modified).days
        if age_days <= 30:
            score += 15
            reasons.append("+15 modified within 30 days")
        elif age_days <= 365:
            score += 8
            reasons.append("+8 modified within 1 year")

    if table_stats.table_count >= 10:
        score += 15
        reasons.append("+15 >=10 tables extracted")
    elif table_stats.table_count >= 6:
        score += 8
        reasons.append("+8 >=6 tables extracted")
    elif table_stats.table_count == 0:
        score -= 20
        reasons.append("-20 no extracted tables")

    if table_stats.total_row_count >= 1000:
        score += 10
        reasons.append("+10 >=1000 total rows")

    confidence = "high"
    if has_schema_warning or table_stats.table_count == 0:
        confidence = "low"
    elif table_stats.table_count < 6:
        confidence = "medium"

    return score, confidence, reasons


def rank_mdb_candidates(
    discovery_rows: Iterable[dict[str, str]],
    table_rows: Iterable[dict[str, str]],
    schema_text: str,
    *,
    now_utc: datetime | None = None,
) -> list[MdbCandidateScore]:
    table_stats_by_analysis_path = build_table_stats(table_rows)
    warning_paths = load_schema_warning_paths(schema_text)
    scored: list[MdbCandidateScore] = []

    for row in discovery_rows:
        analysis_path = row.get("analysis_path", "")
        stats = table_stats_by_analysis_path.get(analysis_path.lower(), MdbTableStats())
        has_schema_warning = analysis_path.lower() in warning_paths
        score, confidence, reasons = score_mdb_candidate(
            row,
            table_stats=stats,
            has_schema_warning=has_schema_warning,
            now_utc=now_utc,
        )
        scored.append(
            MdbCandidateScore(
                rank=0,
                score=score,
                confidence=confidence,
                source_path=row.get("source_path", ""),
                analysis_path=analysis_path,
                file_size_bytes=_as_int(row.get("file_size_bytes")),
                modified_utc=row.get("modified_utc", ""),
                hash_match=str(row.get("hash_match", "")).lower() == "true",
                has_schema_warning=has_schema_warning,
                table_count=stats.table_count,
                total_row_count=stats.total_row_count,
                reasons=reasons,
            )
        )

    sorted_scores = sorted(
        scored,
        key=lambda item: (
            item.score,
            item.table_count,
            item.total_row_count,
            item.file_size_bytes,
            item.modified_utc,
        ),
        reverse=True,
    )

    return [
        MdbCandidateScore(
            rank=index,
            score=item.score,
            confidence=item.confidence,
            source_path=item.source_path,
            analysis_path=item.analysis_path,
            file_size_bytes=item.file_size_bytes,
            modified_utc=item.modified_utc,
            hash_match=item.hash_match,
            has_schema_warning=item.has_schema_warning,
            table_count=item.table_count,
            total_row_count=item.total_row_count,
            reasons=item.reasons,
        )
        for index, item in enumerate(sorted_scores, start=1)
    ]


def read_schema_text(path: Path) -> str:
    if not path.is_file():
        return ""
    return path.read_text(encoding="utf-8-sig")
