def prepare_plot_data(data):
    """
    Convert raw NMR data into a UI-friendly structure.
    The UI can later decide how to render it.
    """
    return {
        "type": "nmr",
        "x": data["x"],
        "y": data["y"],
        "metadata": {
            "source": data.get("source", "")
        }
    }
