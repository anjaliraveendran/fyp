import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from django_plotly_dash import DjangoDash
import plotly.express as px


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = DjangoDash('dashchart', external_stylesheets=external_stylesheets)
df = pd.read_excel('/Users/anjaliraveendran/Desktop/FYP/csv_analysis/scatterPlotTry4.xlsx')



app.layout = html.Div([
    dcc.Graph(
        id='scatter-plot',
        figure={
            'data': [
                go.Scatter(
                    x=df[df['country'] == i]['reportingYear'],
                    y=df[df['country'] == i]['humansAffected'],
                    text=df[df['country'] == i]['region'],
                    mode='markers',
                    opacity=0.8,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name=i
                ) for i in df.country.unique()
            ],
            'layout': go.Layout(
                xaxis={'type': 'log', 'title': 'Years'},
                yaxis={'title': 'Humans Affected'},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 0},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            )
        }
    ),
    # GRAPH 2:-
    dcc.Graph(
        id='scatter-plot',
        figure={
            'data': [
                go.Scatter(
                    x=df[df['country'] == i]['reportingYear'],
                    y=df[df['country'] == i]['humansDeaths'],
                    text=df[df['country'] == i]['region'],
                    mode='markers',
                    opacity=0.8,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name=i
                ) for i in df.country.unique()
            ],
            'layout': go.Layout(
                xaxis={'type': 'log', 'title': 'Years'},
                yaxis={'title': 'Humans Deaths'},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 0},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            )
        }
    )
])
