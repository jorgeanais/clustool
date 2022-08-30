from dash import Dash
from dash_bootstrap_components.themes import BOOTSTRAP

from src.components.layout import create_layout
from src.data.loader import load_input_data
from src.data.source import DataSource

DATA_PATH = "./data/sample_data.csv"


def main() -> None:
    
    # load the data and create the data manager
    data = load_input_data(DATA_PATH)
    data = DataSource(data)

    app = Dash(external_stylesheets=[BOOTSTRAP])
    app.title = "Clustering tool"
    app.layout = create_layout(app, data)
    app.run()

if __name__ == "__main__":
    main()