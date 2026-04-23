from __future__ import annotations

import hashlib
import shutil
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

from .models import AnalysisCopy, DatabaseCandidate

_TARGET_EXTENSIONS = {".mdb", ".accdb"}
_BUFFER_SIZE = 1024 * 1024


def _iter_candidate_paths(roots: Iterable[Path]) -> Iterable[Path]:
    for root in roots:
        if not root.exists():
            continue
        if root.is_file():
            if root.suffix.lower() in _TARGET_EXTENSIONS:
                yield root
            continue
        for extension in _TARGET_EXTENSIONS:
            yield from root.rglob(f"*{extension}")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while True:
            chunk = handle.read(_BUFFER_SIZE)
            if not chunk:
                break
            digest.update(chunk)
    return digest.hexdigest()


def collect_database_candidates(roots: Iterable[str | Path]) -> list[DatabaseCandidate]:
    normalized_roots = [Path(root).expanduser().resolve() for root in roots]
    candidates: list[DatabaseCandidate] = []
    seen_paths: set[Path] = set()

    for path in _iter_candidate_paths(normalized_roots):
        resolved = path.resolve()
        if resolved in seen_paths:
            continue
        seen_paths.add(resolved)
        if not resolved.is_file():
            continue
        stats = resolved.stat()
        modified_utc = datetime.fromtimestamp(
            stats.st_mtime, tz=timezone.utc
        ).isoformat()
        candidates.append(
            DatabaseCandidate(
                source_path=resolved,
                extension=resolved.suffix.lower(),
                file_size_bytes=stats.st_size,
                modified_utc=modified_utc,
                sha256=sha256_file(resolved),
            )
        )

    return sorted(candidates, key=lambda item: str(item.source_path).lower())


def copy_candidates_for_analysis(
    candidates: Iterable[DatabaseCandidate], work_dir: str | Path
) -> list[AnalysisCopy]:
    target_root = Path(work_dir).expanduser().resolve()
    target_root.mkdir(parents=True, exist_ok=True)
    copies: list[AnalysisCopy] = []

    for candidate in candidates:
        safe_stem = "".join(
            char if char.isalnum() or char in ("-", "_") else "_"
            for char in candidate.source_path.stem
        )
        destination_name = (
            f"{safe_stem}__{candidate.sha256[:12]}{candidate.source_path.suffix.lower()}"
        )
        destination_path = target_root / destination_name
        suffix_counter = 1
        while destination_path.exists():
            existing_hash = sha256_file(destination_path)
            if existing_hash == candidate.sha256:
                break
            destination_path = (
                target_root
                / f"{safe_stem}__{candidate.sha256[:12]}__dup{suffix_counter}{candidate.source_path.suffix.lower()}"
            )
            suffix_counter += 1
        if not destination_path.exists():
            shutil.copy2(candidate.source_path, destination_path)
        copied_hash = sha256_file(destination_path)
        copies.append(
            AnalysisCopy(
                source_path=candidate.source_path,
                analysis_path=destination_path,
                source_sha256=candidate.sha256,
                analysis_sha256=copied_hash,
            )
        )

    return copies
