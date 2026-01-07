def prepare_plot_data(data):
    """
    Convert raw IR data into a UI-friendly payload.
    The UI decides rendering (e.g., invert x-axis for wavenumber).
    """
    return {
        "type": "ir",
        "x": data["x"],
        "y": data["y"],
        "metadata": {
            "source": data.get("source", "")
        }
    }
