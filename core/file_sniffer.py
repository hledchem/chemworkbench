from pathlib import Path
from .registry import get_all

def sniff_file(file_path: Path):
    """Return processors that can handle this file based on extension."""
    ext = file_path.suffix.lower()
    candidates = []

    for proc_cls in get_all():
        if ext in proc_cls.file_types:
            candidates.append(proc_cls)

    return candidates

