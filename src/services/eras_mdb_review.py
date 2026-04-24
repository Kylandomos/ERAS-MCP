from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Iterable


DECISION_REQUIRED_COLUMNS = [
    "rank",
    "source_path",
    "analysis_path",
    "score",
    "confidence",
    "has_schema_warning",
    "table_count",
    "total_row_count",
    "review_status",
    "reviewer",
    "reviewed_at_utc",
    "decision_basis",
    "notes",
]

ALLOWED_REVIEW_STATUSES = {"needs_followup", "accept_review", "reject_review"}


@dataclass(frozen=True)
class ReviewValidationResult:
    decision_status: str
    warnings: list[str]
    counts: dict[str, int]
    decisions: list[dict[str, str]]
    accepted_reviews: list[dict[str, str]]
    rejected_reviews: list[dict[str, str]]
    pending_reviews: list[dict[str, str]]


def _path_key(value: str | None) -> str:
    return (value or "").replace("/", "\\").strip().lower()


def _row_value(row: dict[str, str], key: str) -> str:
    return str(row.get(key, "") or "").strip()


def _has_required_accept_fields(row: dict[str, str]) -> bool:
    return all(
        _row_value(row, key)
        for key in ("reviewer", "reviewed_at_utc", "decision_basis")
    )


def validate_mdb_human_decisions(
    *,
    scorecard_rows: Iterable[dict[str, str]],
    decision_rows: Iterable[dict[str, str]],
    decision_columns: Iterable[str],
) -> ReviewValidationResult:
    scorecard = list(scorecard_rows)
    decisions = list(decision_rows)
    columns = list(decision_columns)
    scorecard_paths = {_path_key(row.get("source_path")) for row in scorecard}
    decision_paths = [_path_key(row.get("source_path")) for row in decisions]
    decision_path_set = set(decision_paths)

    warnings: list[str] = []
    missing_columns = [
        column for column in DECISION_REQUIRED_COLUMNS if column not in columns
    ]
    if missing_columns:
        warnings.append(
            "Decision file is missing required columns: "
            + ", ".join(missing_columns)
        )

    duplicate_paths = sorted(
        path for path in decision_path_set if path and decision_paths.count(path) > 1
    )
    for path in duplicate_paths:
        warnings.append(f"Duplicate decision source_path: {path}")

    unknown_paths = sorted(path for path in decision_path_set if path not in scorecard_paths)
    for path in unknown_paths:
        warnings.append(f"Decision source_path not found in scorecard: {path}")

    missing_decisions = sorted(path for path in scorecard_paths if path not in decision_path_set)
    for path in missing_decisions:
        warnings.append(f"Scorecard source_path missing from decisions: {path}")

    invalid_status_count = 0
    incomplete_accept_count = 0
    ready_accept_count = 0
    status_counts = {status: 0 for status in ALLOWED_REVIEW_STATUSES}
    accepted_reviews: list[dict[str, str]] = []
    rejected_reviews: list[dict[str, str]] = []
    pending_reviews: list[dict[str, str]] = []

    for row in decisions:
        status = _row_value(row, "review_status")
        source_path = _row_value(row, "source_path")
        if status not in ALLOWED_REVIEW_STATUSES:
            invalid_status_count += 1
            warnings.append(
                f"Invalid review_status for {source_path or '<missing source_path>'}: {status or '<blank>'}"
            )
            continue

        status_counts[status] += 1
        if status == "accept_review":
            accepted_reviews.append(row)
            if _has_required_accept_fields(row):
                ready_accept_count += 1
            else:
                incomplete_accept_count += 1
                missing_fields = [
                    key
                    for key in ("reviewer", "reviewed_at_utc", "decision_basis")
                    if not _row_value(row, key)
                ]
                warnings.append(
                    f"accept_review for {source_path} is missing: "
                    + ", ".join(missing_fields)
                )
        elif status == "reject_review":
            rejected_reviews.append(row)
        else:
            pending_reviews.append(row)

    if ready_accept_count:
        decision_status = "human_review_ready"
    elif status_counts["accept_review"] or status_counts["reject_review"]:
        decision_status = "human_review_in_progress"
    else:
        decision_status = "human_review_pending"

    counts = {
        "scorecard_candidate_count": len(scorecard),
        "decision_count": len(decisions),
        "needs_followup_count": status_counts["needs_followup"],
        "accept_review_count": status_counts["accept_review"],
        "reject_review_count": status_counts["reject_review"],
        "ready_accept_review_count": ready_accept_count,
        "incomplete_accept_review_count": incomplete_accept_count,
        "invalid_status_count": invalid_status_count,
        "duplicate_source_path_count": len(duplicate_paths),
        "unknown_source_path_count": len(unknown_paths),
        "missing_decision_count": len(missing_decisions),
    }

    return ReviewValidationResult(
        decision_status=decision_status,
        warnings=warnings,
        counts=counts,
        decisions=decisions,
        accepted_reviews=accepted_reviews,
        rejected_reviews=rejected_reviews,
        pending_reviews=pending_reviews,
    )


def initialize_decision_row(scorecard_row: dict[str, str]) -> dict[str, str]:
    return {
        "rank": _row_value(scorecard_row, "rank"),
        "source_path": _row_value(scorecard_row, "source_path"),
        "analysis_path": _row_value(scorecard_row, "analysis_path"),
        "score": _row_value(scorecard_row, "score"),
        "confidence": _row_value(scorecard_row, "confidence"),
        "has_schema_warning": _row_value(scorecard_row, "has_schema_warning"),
        "table_count": _row_value(scorecard_row, "table_count"),
        "total_row_count": _row_value(scorecard_row, "total_row_count"),
        "review_status": "needs_followup",
        "reviewer": "",
        "reviewed_at_utc": "",
        "decision_basis": "",
        "notes": "",
    }
