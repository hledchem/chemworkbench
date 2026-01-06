from pathlib import Path
from core.base_processor import BaseProcessor
from core import registry
from .reader import read_jcamp
from .plotter import prepare_plot_data
from .writer import write_processed_data

class NMRProcessor(BaseProcessor):
    id = "nmr"
    name = "NMR Spectroscopy"
    file_types = [".jdx", ".dx", ".nmredata", ".csv"]

    def read(self, file_path: Path):
        """Load NMR data from JCAMP-DX or CSV."""
        return read_jcamp(file_path)

    def plot(self, data):
        """Return plot-ready arrays for the UI."""
        return prepare_plot_data(data)

    def write(self, data, output_path: Path):
        """Export processed NMR data."""
        write_processed_data(data, output_path)

# Register with the global processor registry
registry.register(NMRProcessor)# NMR processor placeholder
