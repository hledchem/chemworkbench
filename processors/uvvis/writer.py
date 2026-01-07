from pathlib import Path

def write_processed_data(data, output_path: Path):
    with open(output_path, "w") as f:
        f.write("wavelength_nm,intensity\n")
        for x, y in zip(data["x"], data["y"]):
            f.write(f"{x},{y}\n")
