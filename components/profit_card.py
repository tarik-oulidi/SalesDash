import dash_bootstrap_components as dbc
from dash import html, dcc
from dash_iconify import DashIconify
from services.format_number import format_number

def get_profit_card(df_AY, df_PY):
    profit_sum_AY = df_AY['Profit'].sum()
    profit_sum_PY = df_PY['Profit'].sum()
    profit_diff = ((profit_sum_AY - profit_sum_PY) / profit_sum_PY) * 100

    df_AY_profit = df_AY.resample('ME', on='Ship Date').agg({'Profit': 'sum'}).reset_index()

    profit_graph = dcc.Graph(
        figure={
            'data': [
                {'x': df_AY_profit['Ship Date'].to_list(), 'y': df_AY_profit['Profit'].to_list(), 'type': 'line'},
            ],
            'layout': {
                'title': 'Monthly Profit Trend',
                'autosize': True,
                'margin': dict(l=35, r=35, b=35, t=50),
                'height': 250,
                'plot_bgcolor': '#303030',
                'paper_bgcolor': '#303030',
                'font': {
                    'color': 'white',
                },
            }
        }
    )

    return dbc.Card(
        dbc.CardBody(
            [
                html.H2("Profit", className="card-title text-center"),
                html.H1(f"{format_number(profit_sum_AY)}$", className="card-text text-center text-success my-3"),
                html.H4([
                    DashIconify(icon='ph:triangle-fill', className="text-success", style={"fontSize": "20px"}),
                    f"  {profit_diff:.2f}% vs PY"
                ], className="card-text text-center my-3"),
                profit_graph
            ]
        ),
        style={"width": "35rem"},
        className="mx-auto px-0"
)
