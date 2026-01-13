# processors/simple_props.py
from __future__ import annotations
from pathlib import Path
import json
from typing import Any, Dict

from core.base_processor import BaseProcessor

class SimplePropsProcessor(BaseProcessor):
    id = "simple_props"
    name = "Simple Properties Processor"
    file_types = ["json"]

    def read(self, file_path: Path) -> Any:
        """Load a molecule JSON file and return the parsed dict."""
        text = file_path.read_text(encoding="utf-8")
        return json.loads(text)

    def plot(self, data: Any) -> Dict[str, Any]:
        """Return a serializable summary suitable for simple plotting or API responses."""
        atom_count = len(data.get("atoms", []))
        bond_count = len(data.get("bonds", []))
        return {"atom_count": atom_count, "bond_count": bond_count}

    def write(self, data: Any, output_path: Path) -> None:
        """Write processed/derived data to a JSON file."""
        output_path.write_text(json.dumps(data, indent=2), encoding="utf-8")
