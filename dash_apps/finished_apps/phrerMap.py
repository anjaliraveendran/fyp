#import matplotlib.pyplot as plt
import numpy as np
from django_plotly_dash import DjangoDash

import pandas as pd
import plotly.express as px
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go

my_dpi=96

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = DjangoDash('phrerMap', external_stylesheets=external_stylesheets)

app.css.append_css({"external_url": "https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"})

df_phrer = pd.read_excel('/Users/anjaliraveendran/Desktop/FYP/csv_analysis/phrerHtmlNew.xlsx')


app.layout = html.Div([
    # dcc.Graph(
    #     id='phrer',
    #     figure=px.scatter_geo(df_phrer, locations="iso_alpha", color="country",
    #                        hover_name="country", size="phrer2", animation_frame="year",
    #                        projection="natural earth", title="PUBLIC HEALTH RESPONSE EFFECTIVENESS"
    #                        )
    # ),
    dcc.Graph(
        id='phrer-data',
        figure=go.Figure(
        data=[
            go.Bar(name= 'Cambodia', x=df_phrer['year'], y=[5,2,1,1,1,1,8,3,26,9,0,0,0,0] ),
            go.Bar(name='China', x=df_phrer['year'], y=[7,14,6,3,8,1,0,3,2,2,5,1,0,0]),
            go.Bar(name='Egypt', x=df_phrer['year'], y=[0, 18, 23, 10, 39, 25, 43, 12, 4, 26, 147, 10, 3, 0]),
            go.Bar(name='Indonesia', x=df_phrer['year'], y=[16, 59, 42, 23, 23, 9, 11, 10, 3, 1, 2, 0, 1, 0]),
            go.Bar(name='Thailand', x=df_phrer['year'], y=[7, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
            go.Bar(name='Viet Nam', x=df_phrer['year'], y=[35, 0, 8, 5, 6, 7, 0, 4, 2, 2, 0, 0, 0, 0]),
        ],
        layout = go.Layout(barmode='stack',
                           xaxis={'type': 'log', 'title': 'Years'},
                           yaxis={'title': 'Number of Humans Affected by H5N1'},
                           hovermode='closest'
                           )

        ) )
],  style={'width': '100%', 'height':'50%', 'bottom':'0', 'display': 'inline-block'})


# "One of `'equirectangular'`, `'mercator'`, `'orthographic'`, `'natural earth'`, `'kavrayskiy7'`, `'miller'`, `'robinson'`, `'eckert4'`, `'azimuthal equal area'`, `'azimuthal equidistant'`, `'conic equal area'`, `'conic conformal'`, `'conic equidistant'`, `'gnomonic'`, `'stereographic'`, `'mollweide'`, `'hammer'`, `'transverse mercator'`, `'albers usa'`, `'winkel tripel'`, `'aitoff'`, or `'sinusoidal'`"
