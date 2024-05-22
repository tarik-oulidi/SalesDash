import dash_bootstrap_components as dbc
from dash import html, dcc

def get_category_card(df_AY, df_PY):
    df_AY_market = df_AY.groupby('Sub-Category')['Sales'].sum().reset_index()
    df_AY_market = df_AY_market.sort_values('Sales', ascending=True)

    category_graph = dcc.Graph(
        figure={
            'data': [
                {   
                    'y': df_AY_market['Sub-Category'].to_list(),
                    'x': df_AY_market['Sales'].to_list(),
                    'type': 'bar',
                    'orientation': 'h'
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
                },
                'annotations': [
                    dict(
                        x=xi,
                        y=yi,
                        text=str(xi),
                        xanchor='center',
                        yanchor='center',
                        showarrow=False,
                    ) for xi, yi in zip(df_AY_market['Sales'], df_AY_market['Sub-Category'])
                ]
            }
        }
    )

    return dbc.Card(
        dbc.CardBody(
            [
                html.H2("Category YTD Sales", className="card-title text-center"),
                category_graph
            ]
        ),
        style={"width": "75rem"},
        className="mx-auto px-0"
)
