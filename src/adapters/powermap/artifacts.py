from __future__ import annotations

from typing import Any, Mapping


class PowerMapArtifactAdapter:
    """Read-only adapter over the `powermap` section of inventory artifacts."""

    def __init__(self, inventory: Mapping[str, Any] | None) -> None:
        self.inventory = dict(inventory or {})
        powermap = self.inventory.get("powermap", {})
        self.powermap = dict(powermap) if isinstance(powermap, Mapping) else {}

    def status(self) -> dict[str, Any]:
        python_manager = self.powermap.get("python_manager", {})
        macro_inventory = self.powermap.get("macro_inventory", {})

        def _count(value: Any) -> int:
            if value is None:
                return 0
            if isinstance(value, list):
                return len(value)
            return len(list(value)) if hasattr(value, "__iter__") else 0

        return {
            "generated_at_utc": self.powermap.get("generated_at_utc"),
            "executable_count": _count(self.powermap.get("discovered_executables")),
            "workspace_count": _count(self.powermap.get("workspace_path_candidates")),
            "config_file_count": _count(self.powermap.get("config_files")),
            "python_manager_found": bool(
                dict(python_manager).get("found", False)
                if isinstance(python_manager, Mapping)
                else False
            ),
            "python_script_count": _count(
                dict(python_manager).get("scripts", [])
                if isinstance(python_manager, Mapping)
                else []
            ),
            "vba_file_count": _count(
                dict(macro_inventory).get("vba_files", [])
                if isinstance(macro_inventory, Mapping)
                else []
            ),
            "keyin_file_count": _count(
                dict(macro_inventory).get("keyin_files", [])
                if isinstance(macro_inventory, Mapping)
                else []
            ),
            "safe_read_action_count": _count(
                self.powermap.get("safe_read_action_candidates")
            ),
            "gap_count": _count(self.powermap.get("gaps_and_fallbacks")),
        }

    def list_workspaces(self) -> list[str]:
        workspaces = self.powermap.get("workspace_path_candidates", [])
        if not isinstance(workspaces, list):
            return []
        cleaned: list[str] = []
        for item in workspaces:
            if isinstance(item, str) and item.strip():
                cleaned.append(item)
        unique: dict[str, str] = {}
        for path in cleaned:
            unique[path.lower()] = path
        return sorted(unique.values(), key=str.lower)
