import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State


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

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = dbc.Container(
    dbc.Row([dbc.Col(card, width=3) for card in cards]), fluid=True, id="page-content"
)

if __name__ == "__main__":
    app.run_server(debug=True)
