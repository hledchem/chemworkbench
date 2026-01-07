from pathlib import Path
from core.base_processor import BaseProcessor
from core import registry
from .reader import read_uvvis
from .plotter import prepare_plot_data
from .writer import write_processed_data

class UVVisProcessor(BaseProcessor):
    id = "uvvis"
    name = "UV-Vis Spectroscopy"
    file_types = [".jdx", ".dx", ".csv", ".uv"]

    def read(self, file_path: Path):
        return read_uvvis(file_path)

    def plot(self, data):
        return prepare_plot_data(data)

    def write(self, data, output_path: Path):
        write_processed_data(data, output_path)

registry.register(UVVisProcessor)
