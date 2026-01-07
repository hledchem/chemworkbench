from pathlib import Path
from core.base_processor import BaseProcessor
from core import registry
from .reader import read_ir
from .plotter import prepare_plot_data
from .writer import write_processed_data

class IRProcessor(BaseProcessor):
    id = "ir"
    name = "Infrared Spectroscopy"
    file_types = [".jdx", ".dx", ".csv", ".ir"]

    def read(self, file_path: Path):
        """Load IR data from JCAMP-DX or CSV-like files."""
        return read_ir(file_path)

    def plot(self, data):
        """Return plot-ready structure for the UI."""
        return prepare_plot_data(data)

    def write(self, data, output_path: Path):
        """Export processed IR data."""
        write_processed_data(data, output_path)

# Register the processor so the registry and sniffer can find it
registry.register(IRProcessor)
