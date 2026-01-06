from pathlib import Path

def read_jcamp(file_path: Path):
    """
    Minimal JCAMP-DX reader for NMR.
    Returns a dict with x (ppm) and y (intensity).
    """
    x_vals = []
    y_vals = []

    with open(file_path, "r", errors="ignore") as f:
        for line in f:
            line = line.strip()

            # Skip metadata lines
            if not line or line.startswith("##"):
                continue

            # Data lines: "x, y"
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
