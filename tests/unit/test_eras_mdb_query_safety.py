from __future__ import annotations

import sys
from pathlib import Path
import unittest

REPO_ROOT = Path(__file__).resolve().parents[2]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from adapters.eras_mdb.query_safety import assert_read_only_query, validate_read_only_query


class TestErasMdbQuerySafety(unittest.TestCase):
    def test_select_query_is_allowed(self) -> None:
        result = validate_read_only_query("SELECT * FROM Assets")
        self.assertTrue(result.is_valid)

    def test_with_cte_query_is_allowed(self) -> None:
        query = """
        WITH recent_assets AS (
            SELECT TOP 10 * FROM Assets
        )
        SELECT * FROM recent_assets;
        """
        result = validate_read_only_query(query)
        self.assertTrue(result.is_valid)

    def test_update_query_is_blocked(self) -> None:
        result = validate_read_only_query("UPDATE Assets SET name = 'x'")
        self.assertFalse(result.is_valid)
        self.assertIn("Only SELECT or WITH", result.reason)

    def test_select_into_is_blocked(self) -> None:
        result = validate_read_only_query(
            "SELECT asset_id INTO NewAssetTable FROM Assets"
        )
        self.assertFalse(result.is_valid)
        self.assertIn("INTO", result.reason)

    def test_comment_prefixed_delete_is_blocked(self) -> None:
        result = validate_read_only_query("-- note\nDELETE FROM Assets")
        self.assertFalse(result.is_valid)

    def test_multiple_statements_are_blocked(self) -> None:
        result = validate_read_only_query("SELECT * FROM Assets; SELECT * FROM Sites;")
        self.assertFalse(result.is_valid)
        self.assertIn("Multiple SQL statements", result.reason)

    def test_keywords_inside_literals_do_not_trigger_block(self) -> None:
        result = validate_read_only_query(
            "SELECT 'DROP TABLE x' AS sample_value FROM Assets"
        )
        self.assertTrue(result.is_valid)

    def test_assert_raises_for_forbidden_query(self) -> None:
        with self.assertRaises(ValueError):
            assert_read_only_query("INSERT INTO Assets(name) VALUES ('x')")


if __name__ == "__main__":
    unittest.main()
