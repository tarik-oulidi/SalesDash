import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
import pandas as pd # look for polars

from components.sales_card import get_sales_card
from components.profit_card import get_profit_card
from components.quantity_card import get_quantity_card
from components.market_share_card import get_market_share_card
from components.category_card import get_category_card
from components.market_wise_card import get_market_wise_card

df = pd.read_csv('data/superstore.csv')
df = df.sort_values('Ship Date')
df['Order Date'] = pd.to_datetime(df['Order Date'], format="%d-%m-%Y")
df['Ship Date'] = pd.to_datetime(df['Ship Date'], format="%d-%m-%Y")

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Home", href="#")),
        dbc.DropdownMenu(
            nav=True,
            in_navbar=True,
            label="Menu",
            children=[
                dbc.DropdownMenuItem("Entry 1"),
                dbc.DropdownMenuItem("Entry 2"),
                dbc.DropdownMenuItem(divider=True),
                dbc.DropdownMenuItem("Entry 3"),
            ],
        ),
    ],
    brand="Sales Dashboard",
    brand_href="#",
    color="secondary",
    dark=True,
    className="mb-5"
)

df_AY = df[df['Ship Date'].dt.year == 2015]
df_PY = df[df['Ship Date'].dt.year == 2014]

sales_card = get_sales_card(df_AY, df_PY)
profit_card = get_profit_card(df_AY, df_PY)
quantity_card = get_quantity_card(df_AY, df_PY)
market_share_card = get_market_share_card(df_AY, df_PY)

category_card = get_category_card(df_AY, df_PY)
market_wise_card = get_market_wise_card(df_AY, df_PY)

app.layout = html.Div([
    navbar,
    dbc.Row([
        dbc.Col(sales_card),
        dbc.Col(profit_card),
        dbc.Col(quantity_card),
        dbc.Col(market_share_card),
    ], className="w-100 my-3"),
    dbc.Row([
        dbc.Col(category_card),
        dbc.Col(market_wise_card),
    ], className="w-100 my-3"),
], style={"zoom": "0.75"})

if __name__ == '__main__':
    app.run_server(debug=False)
