import dash_bootstrap_components as dbc
from dash import html, dcc
from dash_iconify import DashIconify

def get_quantity_card(df_AY, df_PY):
    quantity_sum_AY = df_AY['Quantity'].sum()
    quantity_sum_PY = df_PY['Quantity'].sum()
    quantity_diff = ((quantity_sum_AY - quantity_sum_PY) / quantity_sum_PY) * 100

    df_AY_quantity = df_AY.resample('ME', on='Ship Date').agg({'Quantity': 'sum'}).reset_index()
    print(df_AY_quantity)

    quantity_graph = dcc.Graph(
        figure={
            'data': [
                {'x': df_AY_quantity['Ship Date'].to_list(), 'y': df_AY_quantity['Quantity'].to_list(), 'type': 'line'},
            ],
            'layout': {
                'title': 'Monthly Quantity Trend',
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
                html.H2("Order Quantity", className="card-title text-center"),
                html.H1(f"{quantity_sum_AY}", className="card-text text-center text-success my-3"),
                html.H4([
                    DashIconify(icon='ph:triangle-fill', className="text-success", style={"fontSize": "20px"}),
                    f"  {quantity_diff:.2f}% vs PY"
                ], className="card-text text-center my-3"),
                quantity_graph
            ]
        ),
        style={"width": "35rem"},
        className="mx-auto px-0"
)
