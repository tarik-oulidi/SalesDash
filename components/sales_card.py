import dash_bootstrap_components as dbc
from dash import html, dcc
from dash_iconify import DashIconify
from services.format_number import format_number

def get_sales_card(df_AY, df_PY):
    sales_sum_AY = df_AY['Sales'].sum()
    sales_sum_PY = df_PY['Sales'].sum()
    sales_diff = ((sales_sum_AY - sales_sum_PY) / sales_sum_PY) * 100

    df_AY_sales = df_AY.resample('ME', on='Ship Date').agg({'Sales': 'sum'}).reset_index()

    sales_graph = dcc.Graph(
        figure={
            'data': [
                {'x': df_AY_sales['Ship Date'].to_list(), 'y': df_AY_sales['Sales'].to_list(), 'type': 'line'},
            ],
            'layout': {
                'title': 'Monthly Sales Trend',
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
                html.H2("Sales", className="card-title text-center"),
                html.H1(f"{format_number(sales_sum_AY)}$", className="card-text text-center text-success my-3"),
                html.H4([
                    DashIconify(icon='ph:triangle-fill', className="text-success", style={"fontSize": "20px"}),
                    f"  {sales_diff:.2f}% vs PY"
                ], className="card-text text-center my-3"),
                sales_graph
            ]
        ),
        style={"width": "35rem"},
        className="mx-auto px-0"
    )
