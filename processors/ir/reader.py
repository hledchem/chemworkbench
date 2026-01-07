from pathlib import Path

def read_ir(file_path: Path):
    """
    Minimal IR reader for JCAMP-DX or CSV-like data.
    Returns a dict with x (wavenumber cm^-1) and y (absorbance/transmittance).
    """
    x_vals = []
    y_vals = []

    with open(file_path, "r", errors="ignore") as f:
        for line in f:
            line = line.strip()
            # Skip empty lines and JCAMP metadata lines
            if not line or line.startswith("##"):
                continue

            # Accept comma or whitespace separated numeric pairs
            if "," in line:
                parts = line.split(",")
            else:
                parts = line.split()

            if len(parts) >= 2:
                try:
                    x = float(parts[0])
                    y = float(parts[1])
                    x_vals.append(x)
                    y_vals.append(y)
                except ValueError:
                    # ignore header lines or malformed rows
                    continue

    return {
        "x": x_vals,          # wavenumber (cm^-1)
        "y": y_vals,          # intensity (absorbance or %T)
        "source": str(file_path)
    }
