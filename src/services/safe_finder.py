from __future__ import annotations

from dataclasses import asdict, dataclass
from fnmatch import fnmatch
from pathlib import Path
from typing import Any, Iterable


@dataclass(frozen=True)
class SearchBounds:
    max_roots: int = 16
    max_files_scanned: int = 20_000
    max_results: int = 500


def _path_is_within(path: Path, base: Path) -> bool:
    if path == base:
        return True
    return base in path.parents


def _is_allowed_root(path: Path, allowed_roots: Iterable[Path]) -> bool:
    return any(_path_is_within(path, allowed) for allowed in allowed_roots)


def _iter_files(root: Path):
    if root.is_file():
        yield root
        return
    for file_path in root.rglob("*"):
        if file_path.is_file():
            yield file_path


def _matches(file_path: Path, patterns: list[str]) -> bool:
    name = file_path.name
    full_path = str(file_path)
    return any(fnmatch(name, pattern) or fnmatch(full_path, pattern) for pattern in patterns)


def find_artifacts_safe(
    *,
    patterns: list[str],
    roots: list[Path],
    allowed_roots: list[Path],
    bounds: SearchBounds,
) -> dict[str, Any]:
    accepted_roots: list[Path] = []
    rejected_roots: list[dict[str, str]] = []

    unique_roots: dict[str, Path] = {}
    for root in roots:
        key = str(root).lower()
        if key not in unique_roots:
            unique_roots[key] = root

    for root in list(unique_roots.values())[: bounds.max_roots]:
        if not root.exists():
            rejected_roots.append({"root": str(root), "reason": "root_not_found"})
            continue
        if allowed_roots and not _is_allowed_root(root, allowed_roots):
            rejected_roots.append({"root": str(root), "reason": "outside_allowed_bounds"})
            continue
        accepted_roots.append(root)

    matches: list[dict[str, Any]] = []
    files_scanned = 0
    stopped_by_limits = False

    for root in accepted_roots:
        for file_path in _iter_files(root):
            if files_scanned >= bounds.max_files_scanned:
                stopped_by_limits = True
                break
            files_scanned += 1
            if not _matches(file_path, patterns):
                continue
            matches.append(
                {
                    "name": file_path.name,
                    "path": str(file_path),
                    "extension": file_path.suffix.lower(),
                    "size_bytes": file_path.stat().st_size,
                    "root": str(root),
                }
            )
            if len(matches) >= bounds.max_results:
                stopped_by_limits = True
                break
        if stopped_by_limits:
            break

    return {
        "patterns": patterns,
        "accepted_roots": [str(root) for root in accepted_roots],
        "rejected_roots": rejected_roots,
        "files_scanned": files_scanned,
        "matches": matches,
        "bounds": asdict(bounds),
        "stopped_by_limits": stopped_by_limits,
    }
