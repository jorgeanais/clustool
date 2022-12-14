from html.entities import html5
import plotly.express as px
from dash import Dash, dcc, html
from dash.dependencies import Input, Output, State

from src.components.dropdown_helper import to_dropdown_options

from ..data.source import DataSource
from . import ids


def render(app: Dash, source: DataSource) -> html.Div:
    @app.callback(
        Output(ids.SCATTER_GRAPH_R, "figure"),
        Input(ids.PLOT_BUTTON, "n_clicks"),
        State(ids.GRAPH_XAXIS_DROPDOWN_R, "value"),
        State(ids.GRAPH_YAXIS_DROPDOWN_R, "value"),
    )
    def update_graph(n_clicks: int, xcol: str, ycol: str) -> px.scatter:
        """Update the scatter graph with the new data"""
        df = source.get_data
        df = df[df.result != -2]  # Do not plot rows mark with -2 (missing data or non selected cluster)
        df["result"] = df["result"].astype(str)
        return px.scatter(
            df,
            x=xcol,
            y=ycol,
            color="result",
            opacity=0.7,
        )

    return html.Div(
        children=[
            dcc.Graph(
                id=ids.SCATTER_GRAPH_R,
                style={'width': '45vh', 'height': '45vh'},
                config= {'displaylogo': False}
            ),
            html.Div("Select axis"),
            dcc.Dropdown(
                id=ids.GRAPH_XAXIS_DROPDOWN_R,
                options=to_dropdown_options(source.all_columns),
                value=source.all_columns[2],
                multi=False,
                placeholder="Select X axis",
            ),
            dcc.Dropdown(
                id=ids.GRAPH_YAXIS_DROPDOWN_R,
                options=to_dropdown_options(source.all_columns),
                value=source.all_columns[4],
                multi=False,
                placeholder="Select Y axis",
            ),
        ]
    )
