import plotly.express as px
import pandas as pd
import numpy as np
from plotly.offline import plot
from django_plotly_dash import DjangoDash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = DjangoDash('phrerMap', external_stylesheets=external_stylesheets)

df_phrer = pd.read_excel('/Users/anjaliraveendran/Desktop/FYP/csv_analysis/phrerHtml.xlsx')

# df = px.data.gapminder().query("year==2007")
# fig = px.scatter_geo(df_phrer, locations="iso_alpha", color="country",
#                      hover_name="country", size="phrer2", animation_frame="year",
#                      projection="natural earth")
# fig.show()



app.layout = html.Div([
    dcc.Graph(
        id='phrer',
        figure=px.scatter_geo(df_phrer, locations="iso_alpha", color="country",
                           hover_name="country", size="phrer2", animation_frame="year",
                           projection="natural earth", title="PUBLIC HEALTH RESPONSE EFFECTIVENESS"
                           )
    )
])

# "One of `'equirectangular'`, `'mercator'`, `'orthographic'`, `'natural earth'`, `'kavrayskiy7'`, `'miller'`, `'robinson'`, `'eckert4'`, `'azimuthal equal area'`, `'azimuthal equidistant'`, `'conic equal area'`, `'conic conformal'`, `'conic equidistant'`, `'gnomonic'`, `'stereographic'`, `'mollweide'`, `'hammer'`, `'transverse mercator'`, `'albers usa'`, `'winkel tripel'`, `'aitoff'`, or `'sinusoidal'`"
