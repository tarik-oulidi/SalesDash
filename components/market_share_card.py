import dash_bootstrap_components as dbc
from dash import html, dcc
from dash_iconify import DashIconify

def get_market_share_card(df_AY, df_PY):
    market = df_AY['Sales'].sum()
    df_AY_market = df_AY.groupby('Market')['Quantity'].sum().reset_index()
    df_AY_market = df_AY_market.sort_values('Market')
    print(df_AY_market)

    market_graph = dcc.Graph(
        figure={
            'data': [
                {   
                    'labels': df_AY_market['Market'].to_list(),
                    'values': df_AY_market['Quantity'].to_list(),
                    'type': 'pie',
                    'hole': 0.4,
                },
            ],
            'layout': {
                'autosize': True,
                'margin': dict(l=0, r=0, b=10, t=20),
                'height': 375,
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
                html.H2("Market share", className="card-title text-center"),
                market_graph
            ]
        ),
        style={"width": "35rem"},
        className="mx-auto px-0"
)
