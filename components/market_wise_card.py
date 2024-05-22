import dash_bootstrap_components as dbc
from dash import html, dcc

def get_market_wise_card(df_AY, df_PY):
    df_AY.set_index('Ship Date', inplace=True)
    df_AY_quantity = df_AY.groupby('Market').resample('ME').agg({'Quantity': 'sum'}).reset_index()

    market_wise_graph = dcc.Graph(
        figure={
            'data': [
                {   
                    'y': df_AY_quantity[df_AY_quantity['Market'] == 'Africa']['Quantity'].to_list(),
                    'x': df_AY_quantity['Ship Date'].to_list(),
                    'type': 'line+markers',
                    'name': 'Africa',
                    'marker': {'size': 10},
                },
                {   
                    'y': df_AY_quantity[df_AY_quantity['Market'] == 'Asia Pacific']['Quantity'].to_list(),
                    'x': df_AY_quantity['Ship Date'].to_list(),
                    'type': 'line+markers',
                    'name': 'Asia Pacific',
                    'marker': {'size': 10},
                },
                {   
                    'y': df_AY_quantity[df_AY_quantity['Market'] == 'Europe']['Quantity'].to_list(),
                    'x': df_AY_quantity['Ship Date'].to_list(),
                    'type': 'line+markers',
                    'name': 'Europe',
                    'marker': {'size': 10},
                },
                {   
                    'y': df_AY_quantity[df_AY_quantity['Market'] == 'LATAM']['Quantity'].to_list(),
                    'x': df_AY_quantity['Ship Date'].to_list(),
                    'type': 'line+markers',
                    'name': 'LATAM',
                    'marker': {'size': 10},
                },
                {   
                    'y': df_AY_quantity[df_AY_quantity['Market'] == 'USCA']['Quantity'].to_list(),
                    'x': df_AY_quantity['Ship Date'].to_list(),
                    'type': 'line+markers',
                    'name': 'USCA',
                    'marker': {'size': 10},
                },
            ],
            'layout': {
                'autosize': True,
                'margin': dict(l=70, r=70, b=20, t=20),
                'height': 500,
                'plot_bgcolor': '#303030',
                'paper_bgcolor': '#303030',
                'font': {
                    'color': 'white',
                }
            }
        }
    )

    return dbc.Card(
        dbc.CardBody(
            [
                html.H2("Market wise customer acquisition", className="card-title text-center"),
                market_wise_graph
            ]
        ),
        style={"width": "75rem"},
        className="mx-auto px-0"
)
