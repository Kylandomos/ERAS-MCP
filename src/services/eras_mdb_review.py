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


@dataclass(frozen=True)
class ReviewDecisionUpdateResult:
    success: bool
    changed: bool
    dry_run: bool
    message: str
    decision_status: str
    warnings: list[str]
    counts: dict[str, int]
    decisions: list[dict[str, str]]
    previous_row: dict[str, str] | None
    updated_row: dict[str, str] | None


def _path_key(value: str | None) -> str:
    return (value or "").replace("/", "\\").strip().lower()


def _row_value(row: dict[str, str], key: str) -> str:
    return str(row.get(key, "") or "").strip()


def _has_required_accept_fields(row: dict[str, str]) -> bool:
    return all(
        _row_value(row, key)
        for key in ("reviewer", "reviewed_at_utc", "decision_basis")
    )


def _sorted_by_rank(rows: Iterable[dict[str, str]]) -> list[dict[str, str]]:
    def sort_key(row: dict[str, str]) -> tuple[int, str]:
        try:
            rank = int(_row_value(row, "rank"))
        except ValueError:
            rank = 999999
        return (rank, _row_value(row, "source_path").lower())

    return sorted(rows, key=sort_key)


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


def apply_mdb_human_decision(
    *,
    scorecard_rows: Iterable[dict[str, str]],
    decision_rows: Iterable[dict[str, str]],
    decision_columns: Iterable[str],
    source_path: str,
    status: str,
    reviewer: str = "",
    decision_basis: str = "",
    notes: str = "",
    reviewed_at_utc: str = "",
    dry_run: bool = False,
) -> ReviewDecisionUpdateResult:
    scorecard = list(scorecard_rows)
    decisions = [dict(row) for row in decision_rows]
    columns = list(decision_columns)
    warnings: list[str] = []
    normalized_source_path = _path_key(source_path)
    normalized_status = (status or "").strip()
    reviewer_value = (reviewer or "").strip()
    basis_value = (decision_basis or "").strip()
    notes_value = (notes or "").strip()
    reviewed_at_value = (reviewed_at_utc or "").strip()

    if normalized_status not in ALLOWED_REVIEW_STATUSES:
        return ReviewDecisionUpdateResult(
            success=False,
            changed=False,
            dry_run=dry_run,
            message=f"Invalid review_status: {normalized_status or '<blank>'}",
            decision_status="human_review_in_progress",
            warnings=[f"Invalid review_status: {normalized_status or '<blank>'}"],
            counts={},
            decisions=decisions,
            previous_row=None,
            updated_row=None,
        )

    missing_columns = [
        column for column in DECISION_REQUIRED_COLUMNS if column not in columns
    ]
    if missing_columns:
        return ReviewDecisionUpdateResult(
            success=False,
            changed=False,
            dry_run=dry_run,
            message="Decision file is missing required columns.",
            decision_status="human_review_in_progress",
            warnings=[
                "Decision file is missing required columns: "
                + ", ".join(missing_columns)
            ],
            counts={},
            decisions=decisions,
            previous_row=None,
            updated_row=None,
        )

    scorecard_matches = [
        row for row in scorecard if _path_key(row.get("source_path")) == normalized_source_path
    ]
    if len(scorecard_matches) != 1:
        warnings.append(
            f"source_path matched {len(scorecard_matches)} scorecard rows; expected exactly 1."
        )

    decision_indexes = [
        index
        for index, row in enumerate(decisions)
        if _path_key(row.get("source_path")) == normalized_source_path
    ]
    if len(decision_indexes) != 1:
        warnings.append(
            f"source_path matched {len(decision_indexes)} decision rows; expected exactly 1."
        )

    if warnings:
        return ReviewDecisionUpdateResult(
            success=False,
            changed=False,
            dry_run=dry_run,
            message="Review decision was not applied.",
            decision_status="human_review_in_progress",
            warnings=warnings,
            counts={},
            decisions=decisions,
            previous_row=None,
            updated_row=None,
        )

    if normalized_status in {"accept_review", "reject_review"}:
        missing_fields = []
        if not reviewer_value:
            missing_fields.append("reviewer")
        if not basis_value:
            missing_fields.append("decision_basis")
        if missing_fields:
            return ReviewDecisionUpdateResult(
                success=False,
                changed=False,
                dry_run=dry_run,
                message=(
                    f"{normalized_status} requires: "
                    + ", ".join(missing_fields)
                ),
                decision_status="human_review_in_progress",
                warnings=[
                    f"{normalized_status} requires: " + ", ".join(missing_fields)
                ],
                counts={},
                decisions=decisions,
                previous_row=None,
                updated_row=None,
            )
        if not reviewed_at_value:
            return ReviewDecisionUpdateResult(
                success=False,
                changed=False,
                dry_run=dry_run,
                message=f"{normalized_status} requires reviewed_at_utc.",
                decision_status="human_review_in_progress",
                warnings=[f"{normalized_status} requires reviewed_at_utc."],
                counts={},
                decisions=decisions,
                previous_row=None,
                updated_row=None,
            )

    row_index = decision_indexes[0]
    previous_row = dict(decisions[row_index])
    updated_row = dict(previous_row)
    updated_row["review_status"] = normalized_status
    updated_row["reviewer"] = reviewer_value
    updated_row["decision_basis"] = basis_value
    updated_row["notes"] = notes_value
    updated_row["reviewed_at_utc"] = (
        reviewed_at_value
        if normalized_status in {"accept_review", "reject_review"}
        or reviewer_value
        or basis_value
        else ""
    )
    updated_decisions = [dict(row) for row in decisions]
    updated_decisions[row_index] = updated_row

    validation = validate_mdb_human_decisions(
        scorecard_rows=scorecard,
        decision_rows=updated_decisions,
        decision_columns=columns,
    )

    return ReviewDecisionUpdateResult(
        success=True,
        changed=previous_row != updated_row,
        dry_run=dry_run,
        message="Review decision validated; no files written." if dry_run else "Review decision applied.",
        decision_status=validation.decision_status,
        warnings=validation.warnings,
        counts=validation.counts,
        decisions=updated_decisions,
        previous_row=previous_row,
        updated_row=updated_row,
    )


def render_human_decision_status_report(
    *,
    validation: ReviewValidationResult,
    generated_date: str,
) -> str:
    pending_top = _sorted_by_rank(validation.pending_reviews)[:10]
    accepted = _sorted_by_rank(validation.accepted_reviews)
    rejected = _sorted_by_rank(validation.rejected_reviews)

    def table_rows(rows: Iterable[dict[str, str]], status_label: str) -> list[str]:
        rendered = []
        for row in rows:
            rendered.append(
                "| {rank} | {score} | {confidence} | `{source_path}` | {table_count} | {total_row_count} | {status} |".format(
                    rank=_row_value(row, "rank"),
                    score=_row_value(row, "score"),
                    confidence=_row_value(row, "confidence"),
                    source_path=_row_value(row, "source_path"),
                    table_count=_row_value(row, "table_count"),
                    total_row_count=_row_value(row, "total_row_count"),
                    status=status_label,
                )
            )
        return rendered

    lines = [
        "# ERAS MDB Human Decision Status",
        "",
        f"Generated: {generated_date}",
        "",
        "## Decision Status",
        "",
        f"- `{validation.decision_status}`",
        "- No authoritative MDB declared by automation.",
        "- The decision file is the source of truth for human review state.",
        "- Data policy: metadata only. No business row values or sample rows were read.",
        "",
        "## Sources",
        "",
        "- Human decisions: `docs/reviews/ERAS_MDB_HUMAN_DECISIONS_20260424.csv`",
        "- Scorecard: `docs/schemas/ERAS_MDB_CANDIDATE_SCORECARD.csv`",
        "- Review pack: `docs/reports/eras_mdb_candidate_review_20260423.md`",
        "- Evidence: `docs/evidence/ev-011-eras-mdb-human-decisions.md`",
        "- Decision intake evidence: `docs/evidence/ev-012-eras-mdb-decision-intake.md`",
        "",
        "## Summary",
        "",
        f"- Scorecard candidates: `{validation.counts.get('scorecard_candidate_count', 0)}`",
        f"- Decision rows: `{validation.counts.get('decision_count', 0)}`",
        f"- `needs_followup`: `{validation.counts.get('needs_followup_count', 0)}`",
        f"- `accept_review`: `{validation.counts.get('accept_review_count', 0)}`",
        f"- `reject_review`: `{validation.counts.get('reject_review_count', 0)}`",
        f"- Ready accepted reviews: `{validation.counts.get('ready_accept_review_count', 0)}`",
        f"- Incomplete accepted reviews: `{validation.counts.get('incomplete_accept_review_count', 0)}`",
        f"- Invalid statuses: `{validation.counts.get('invalid_status_count', 0)}`",
        f"- Duplicate source paths: `{validation.counts.get('duplicate_source_path_count', 0)}`",
        f"- Unknown source paths: `{validation.counts.get('unknown_source_path_count', 0)}`",
        f"- Missing decision rows: `{validation.counts.get('missing_decision_count', 0)}`",
        "",
        "## Top Candidates Still Pending",
        "",
        "| Rank | Score | Confidence | Source path | Tables | Rows | Current status |",
        "|---:|---:|---|---|---:|---:|---|",
    ]
    lines.extend(table_rows(pending_top, "needs_followup") or ["| - | - | - | None | - | - | - |"])
    lines.extend(
        [
            "",
            "## Accepted Reviews",
            "",
            "| Rank | Score | Confidence | Source path | Tables | Rows | Current status |",
            "|---:|---:|---|---|---:|---:|---|",
        ]
    )
    lines.extend(table_rows(accepted, "accept_review") or ["| - | - | - | None | - | - | - |"])
    lines.extend(
        [
            "",
            "## Rejected Reviews",
            "",
            "| Rank | Score | Confidence | Source path | Tables | Rows | Current status |",
            "|---:|---:|---|---|---:|---:|---|",
        ]
    )
    lines.extend(table_rows(rejected, "reject_review") or ["| - | - | - | None | - | - | - |"])
    lines.extend(
        [
            "",
            "## Required Human Fields",
            "",
            "An `accept_review` decision is not considered ready unless it includes:",
            "",
            "- `reviewer`",
            "- `reviewed_at_utc`",
            "- `decision_basis`",
            "",
            "The validation tool reports missing fields as warnings and keeps the global status out of `human_review_ready`.",
        ]
    )
    return "\n".join(lines) + "\n"
