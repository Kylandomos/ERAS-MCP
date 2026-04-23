from __future__ import annotations

import csv
import json
import re
from pathlib import Path
from typing import Any

_INVENTORY_DIR_RE = re.compile(r"^windows_scan_(\d{8}_\d{6})$")


class ArtifactStore:
    """Read-only helper for loading generated inventory and export artifacts."""

    def __init__(self, repo_root: str | Path | None = None) -> None:
        if repo_root is None:
            repo_root = Path(__file__).resolve().parents[2]
        self.repo_root = Path(repo_root).expanduser().resolve()
        self.artifacts_root = self.repo_root / "artifacts"
        self.inventories_root = self.artifacts_root / "inventories"
        self.exports_root = self.artifacts_root / "exports"

    def _inventory_sort_key(self, path: Path) -> tuple[int, str]:
        match = _INVENTORY_DIR_RE.match(path.name)
        if not match:
            return (0, path.name)
        return (1, match.group(1))

    def inventory_directories(self) -> list[Path]:
        if not self.inventories_root.exists():
            return []
        directories = [
            item
            for item in self.inventories_root.iterdir()
            if item.is_dir() and _INVENTORY_DIR_RE.match(item.name)
        ]
        return sorted(directories, key=self._inventory_sort_key)

    def inventory_paths(self) -> list[Path]:
        return [
            directory / "inventory.json"
            for directory in self.inventory_directories()
            if (directory / "inventory.json").is_file()
        ]

    def latest_inventory_path(self) -> Path | None:
        paths = self.inventory_paths()
        return paths[-1] if paths else None

    def load_inventory(
        self, *, latest: bool = True, inventory_path: str | Path | None = None
    ) -> dict[str, Any] | None:
        if inventory_path is not None:
            path = Path(inventory_path).expanduser().resolve()
        else:
            if latest:
                path = self.latest_inventory_path()
            else:
                paths = self.inventory_paths()
                path = paths[-1] if paths else None
        if path is None or not path.is_file():
            return None
        with path.open("r", encoding="utf-8-sig") as handle:
            return json.load(handle)

    def load_inventory_summaries(self) -> list[dict[str, Any]]:
        summaries: list[dict[str, Any]] = []
        for path in self.inventory_paths():
            try:
                with path.open("r", encoding="utf-8-sig") as handle:
                    inventory = json.load(handle)
                metadata = inventory.get("metadata", {})
                summaries.append(
                    {
                        "inventory_path": str(path),
                        "scan_id": metadata.get("scan_id"),
                        "generated_at_utc": metadata.get("generated_at_utc"),
                        "read_only": metadata.get("read_only"),
                    }
                )
            except Exception as exc:
                summaries.append(
                    {
                        "inventory_path": str(path),
                        "error": str(exc),
                    }
                )
        return summaries

    def read_csv_rows(self, csv_path: Path) -> list[dict[str, str]]:
        if not csv_path.is_file():
            return []
        with csv_path.open("r", encoding="utf-8-sig", newline="") as handle:
            return [dict(row) for row in csv.DictReader(handle)]

    def read_export_csv(self, filename: str) -> list[dict[str, str]]:
        return self.read_csv_rows(self.exports_root / filename)

    def known_scan_roots(
        self, inventory: dict[str, Any] | None = None
    ) -> list[Path]:
        if inventory is None:
            inventory = self.load_inventory(latest=True)
        if not inventory:
            return []
        scan_roots = inventory.get("scan_roots", [])
        resolved: list[Path] = []
        for item in scan_roots:
            if not isinstance(item, dict):
                continue
            if not item.get("exists"):
                continue
            raw_path = item.get("path")
            if not isinstance(raw_path, str) or not raw_path.strip():
                continue
            candidate = Path(raw_path).expanduser()
            try:
                candidate = candidate.resolve()
            except Exception:
                continue
            resolved.append(candidate)
        unique: dict[str, Path] = {}
        for root in resolved:
            unique[str(root).lower()] = root
        return sorted(unique.values(), key=lambda value: str(value).lower())
