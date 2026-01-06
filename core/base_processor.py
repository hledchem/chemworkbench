
from abc import ABC, abstractmethod
from pathlib import Path

class BaseProcessor(ABC):
    """Standard interface for all spectroscopy processors."""

    id: str = "base"
    name: str = "Base Processor"
    file_types: list[str] = []

    @abstractmethod
    def read(self, file_path: Path):
        """Load raw data from a file."""
        ...

    @abstractmethod
    def plot(self, data):
        """Return plot-ready data or a plot object."""
        ...

    @abstractmethod
    def write(self, data, output_path: Path):
        """Export processed data."""
        ...
