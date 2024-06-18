from dash import html
import dash_bootstrap_components as dbc

cards = [
    dbc.Card(
        [
            html.H2(f"55", className="card-title"),
            html.P("Total duration", className="card-text"),
        ],
        body=True,
        color="light",
    ),
    dbc.Card(
        [
            html.H2(f"10", className="card-title"),
            html.P("Episodes", className="card-text"),
        ],
        body=True,
        color="success",
        inverse=True,
    ),
    dbc.Card(
        [
            html.H2(f"55", className="card-title"),
            html.P("Countires", className="card-text"),
        ],
        body=True,
        color="dark",
        inverse=True,
    ),
    dbc.Card(
        [
            html.H2("4", className="card-title"),
            html.P("Genres", className="card-text"),
        ],
        body=True,
        color="primary",
        inverse=True,
    ),
]