from __future__ import annotations

import csv
from pathlib import Path
import sys
import unittest

REPO_ROOT = Path(__file__).resolve().parents[2]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from services.eras_mdb_review import (
    DECISION_REQUIRED_COLUMNS,
    initialize_decision_row,
    validate_mdb_human_decisions,
)


class TestErasMdbReview(unittest.TestCase):
    def test_pending_decisions_validate_with_standard_counts(self) -> None:
        scorecard = [
            {
                "rank": "1",
                "source_path": r"C:\App\CLIENT\a.mdb",
                "analysis_path": r"C:\work\a.mdb",
                "score": "10",
                "confidence": "high",
                "has_schema_warning": "False",
                "table_count": "6",
                "total_row_count": "100",
            }
        ]
        decisions = [initialize_decision_row(scorecard[0])]

        result = validate_mdb_human_decisions(
            scorecard_rows=scorecard,
            decision_rows=decisions,
            decision_columns=DECISION_REQUIRED_COLUMNS,
        )

        self.assertEqual(result.decision_status, "human_review_pending")
        self.assertEqual(result.counts["decision_count"], 1)
        self.assertEqual(result.counts["needs_followup_count"], 1)
        self.assertEqual(result.warnings, [])

    def test_invalid_status_produces_warning(self) -> None:
        scorecard = [{"source_path": r"C:\App\CLIENT\a.mdb"}]
        decisions = [
            {
                "source_path": r"C:\App\CLIENT\a.mdb",
                "review_status": "maybe",
            }
        ]

        result = validate_mdb_human_decisions(
            scorecard_rows=scorecard,
            decision_rows=decisions,
            decision_columns=DECISION_REQUIRED_COLUMNS,
        )

        self.assertEqual(result.counts["invalid_status_count"], 1)
        self.assertIn("Invalid review_status", result.warnings[0])

    def test_incomplete_accept_review_is_not_ready(self) -> None:
        scorecard = [{"source_path": r"C:\App\CLIENT\a.mdb"}]
        decisions = [
            {
                "source_path": r"C:\App\CLIENT\a.mdb",
                "review_status": "accept_review",
                "reviewer": "analyst",
                "reviewed_at_utc": "",
                "decision_basis": "",
            }
        ]

        result = validate_mdb_human_decisions(
            scorecard_rows=scorecard,
            decision_rows=decisions,
            decision_columns=DECISION_REQUIRED_COLUMNS,
        )

        self.assertEqual(result.decision_status, "human_review_in_progress")
        self.assertEqual(result.counts["incomplete_accept_review_count"], 1)
        self.assertIn("missing", result.warnings[0])

    def test_complete_accept_review_is_ready(self) -> None:
        scorecard = [{"source_path": r"C:\App\CLIENT\a.mdb"}]
        decisions = [
            {
                "source_path": r"C:\App\CLIENT\a.mdb",
                "review_status": "accept_review",
                "reviewer": "analyst",
                "reviewed_at_utc": "2026-04-24T10:00:00+00:00",
                "decision_basis": "manual review",
            }
        ]

        result = validate_mdb_human_decisions(
            scorecard_rows=scorecard,
            decision_rows=decisions,
            decision_columns=DECISION_REQUIRED_COLUMNS,
        )

        self.assertEqual(result.decision_status, "human_review_ready")
        self.assertEqual(result.counts["ready_accept_review_count"], 1)

    def test_path_mismatches_and_duplicates_are_reported(self) -> None:
        scorecard = [
            {"source_path": r"C:\App\CLIENT\a.mdb"},
            {"source_path": r"C:\App\CLIENT\b.mdb"},
        ]
        decisions = [
            {"source_path": r"C:\App\CLIENT\a.mdb", "review_status": "needs_followup"},
            {"source_path": r"C:\App\CLIENT\a.mdb", "review_status": "needs_followup"},
            {"source_path": r"C:\App\CLIENT\unknown.mdb", "review_status": "needs_followup"},
        ]

        result = validate_mdb_human_decisions(
            scorecard_rows=scorecard,
            decision_rows=decisions,
            decision_columns=DECISION_REQUIRED_COLUMNS,
        )

        self.assertEqual(result.counts["duplicate_source_path_count"], 1)
        self.assertEqual(result.counts["unknown_source_path_count"], 1)
        self.assertEqual(result.counts["missing_decision_count"], 1)
        self.assertTrue(
            any("Duplicate decision source_path" in warning for warning in result.warnings)
        )
        self.assertTrue(
            any("not found in scorecard" in warning for warning in result.warnings)
        )
        self.assertTrue(
            any("missing from decisions" in warning for warning in result.warnings)
        )

    def test_versioned_decisions_match_scorecard_candidates(self) -> None:
        scorecard_path = REPO_ROOT / "docs" / "schemas" / "ERAS_MDB_CANDIDATE_SCORECARD.csv"
        decisions_path = REPO_ROOT / "docs" / "reviews" / "ERAS_MDB_HUMAN_DECISIONS_20260424.csv"

        with scorecard_path.open("r", encoding="utf-8-sig", newline="") as handle:
            scorecard = list(csv.DictReader(handle))
        with decisions_path.open("r", encoding="utf-8-sig", newline="") as handle:
            decisions = list(csv.DictReader(handle))

        scorecard_paths = {row["source_path"].lower() for row in scorecard}
        decision_paths = {row["source_path"].lower() for row in decisions}

        self.assertEqual(len(decisions), 54)
        self.assertEqual(len(scorecard), 54)
        self.assertEqual(decision_paths, scorecard_paths)
        self.assertEqual({row["review_status"] for row in decisions}, {"needs_followup"})


if __name__ == "__main__":
    unittest.main()
