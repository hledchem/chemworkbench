from pathlib import Path

def read_uvvis(file_path: Path):
    """
    Minimal UV-Vis reader for CSV or JCAMP-like data.
    Returns wavelength (nm) and absorbance/absorbance units.
    """
    x_vals = []
    y_vals = []

    with open(file_path, "r", errors="ignore") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("##") or line.lower().startswith("wavelength"):
                continue
            if "," in line:
                try:
                    x, y = line.split(",")
                    x_vals.append(float(x))
                    y_vals.append(float(y))
                except ValueError:
                    pass

    return {
        "x": x_vals,
        "y": y_vals,
        "source": str(file_path)
    }
