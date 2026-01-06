from pathlib import Path

def write_processed_data(data, output_path: Path):
    """
    Write processed NMR data to CSV.
    """
    with open(output_path, "w") as f:
        f.write("ppm,intensity\n")
        for x, y in zip(data["x"], data["y"]):
            f.write(f"{x},{y}\n")
