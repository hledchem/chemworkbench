def prepare_plot_data(data):
    return {
        "type": "uvvis",
        "x": data["x"],
        "y": data["y"],
        "metadata": {
            "source": data.get("source", "")
        }
    }
