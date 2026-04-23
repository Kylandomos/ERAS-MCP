from __future__ import annotations

from datetime import datetime, timezone
import unittest

from services.eras_mdb_ranking import (
    MdbTableStats,
    load_schema_warning_paths,
    rank_mdb_candidates,
    score_mdb_candidate,
)


NOW = datetime(2026, 4, 23, tzinfo=timezone.utc)


class TestErasMdbRanking(unittest.TestCase):
    def test_hash_match_and_warning_change_score(self) -> None:
        row = {
            "source_path": r"C:\AppSogelink\ERAS_Connect_2026\CLIENT\candidate.mdb",
            "analysis_path": r"C:\work\candidate.mdb",
            "modified_utc": "2026-04-20T00:00:00+00:00",
            "hash_match": "True",
        }

        clean_score, _, clean_reasons = score_mdb_candidate(
            row,
            table_stats=MdbTableStats(table_count=10, total_row_count=1000),
            has_schema_warning=False,
            now_utc=NOW,
        )
        warning_score, _, warning_reasons = score_mdb_candidate(
            row,
            table_stats=MdbTableStats(table_count=10, total_row_count=1000),
            has_schema_warning=True,
            now_utc=NOW,
        )

        self.assertEqual(clean_score - warning_score, 30)
        self.assertIn("+20 hash match", clean_reasons)
        self.assertIn("-30 ODBC warning", warning_reasons)

    def test_path_tokens_apply_expected_weights(self) -> None:
        row = {
            "source_path": r"C:\AppSogelink\ERAS_Connect_2026\SYSTEME\SEED\temp_modele_dgn_sht.mdb",
            "analysis_path": r"C:\work\temp_modele_dgn_sht.mdb",
            "modified_utc": "2020-12-01T00:00:00+00:00",
            "hash_match": "False",
        }

        score, confidence, reasons = score_mdb_candidate(
            row,
            table_stats=MdbTableStats(table_count=0, total_row_count=0),
            has_schema_warning=False,
            now_utc=NOW,
        )

        self.assertEqual(score, -58)
        self.assertEqual(confidence, "low")
        self.assertIn("+12 SYSTEME path", reasons)
        self.assertIn("-10 SEED path", reasons)
        self.assertIn("-20 temp path/name", reasons)
        self.assertIn("-10 modele path/name", reasons)
        self.assertIn("-10 dgn_sht path/name", reasons)
        self.assertIn("-20 no extracted tables", reasons)

    def test_zero_table_candidates_are_ranked_but_incomplete(self) -> None:
        discovery_rows = [
            {
                "source_path": r"C:\AppSogelink\ERAS_Connect_2026\CLIENT\empty.mdb",
                "analysis_path": r"C:\work\empty.mdb",
                "file_size_bytes": "100",
                "modified_utc": "2026-04-20T00:00:00+00:00",
                "hash_match": "True",
            }
        ]

        ranked = rank_mdb_candidates(
            discovery_rows,
            table_rows=[],
            schema_text="",
            now_utc=NOW,
        )

        self.assertEqual(len(ranked), 1)
        self.assertEqual(ranked[0].table_count, 0)
        self.assertEqual(ranked[0].confidence, "low")
        self.assertIn("-20 no extracted tables", ranked[0].reasons)

    def test_schema_warning_paths_are_loaded_from_markdown(self) -> None:
        schema_text = "\n".join(
            [
                r"## Database: `C:\work\a.mdb`",
                "- Tables discovered: `0`",
                "- ODBC schema read failed: example",
                r"## Database: `C:\work\b.mdb`",
                "- Tables discovered: `1`",
            ]
        )

        self.assertEqual(load_schema_warning_paths(schema_text), {r"c:\work\a.mdb"})


if __name__ == "__main__":
    unittest.main()
