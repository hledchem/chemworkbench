# core/base_processor.py
from __future__ import annotations
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any, Dict

class BaseProcessor(ABC):
    """Standard interface for all spectroscopy processors."""

    id: str = "base"
    name: str = "Base Processor"
    file_types: list[str] = []

    @abstractmethod
    def read(self, file_path: Path) -> Any:
        """Load raw data from a file and return a raw-data object."""
        ...

    @abstractmethod
    def plot(self, data: Any) -> Dict[str, Any]:
        """Return plot-ready data or a plot object (serializable dict)."""
        ...

    @abstractmethod
    def write(self, data: Any, output_path: Path) -> None:
        """Export processed data to output_path."""
        ...
