from pathlib import Path

def write_processed_data(data, output_path: Path):
    """
    Write processed IR data to CSV with header wavenumber,intensity.
    """
    with open(output_path, "w") as f:
        f.write("wavenumber_cm-1,intensity\n")
        for x, y in zip(data["x"], data["y"]):
            f.write(f"{x},{y}\n")
