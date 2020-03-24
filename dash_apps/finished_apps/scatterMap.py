from dash.dependencies import Input, Output, State
import plotly.express as px
import pandas as pd
import numpy as np
from django_plotly_dash import DjangoDash
import dash_core_components as dcc
import dash_html_components as html
import psycopg2
import pandas.io.sql as psql

conn = psycopg2.connect(database="avianinfluenza", user="fyp", password="breakfast123", host="localhost", port="5432")
cur = conn.cursor()
df_scatter = psql.read_sql("Select * from landingpage_empresdomesticwildhuman", conn)
df_scatter = df_scatter.fillna( 0 )

df_2004 = df_scatter[df_scatter.reportingYear==2004]
df_2005 = df_scatter[df_scatter.reportingYear==2005]

external_stylesheets = ['https://codepen.io/plotly/pen/EQZeaW.css']

app = DjangoDash('scatterMap', external_stylesheets=external_stylesheets)

# df_scatter = pd.read_excel('/Users/anjaliraveendran/Desktop/FYP/csv/empresfinaltry.xlsx')
# df_scatter = df_scatter.fillna( 0 )

YEARS = [ 2005, 2006, 2007, \
		2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]

BINS = ['0-2', '2.1-4', '4.1-6', '6.1-8', '8.1-10', '10.1-12', '12.1-14', \
		'14.1-16', '16.1-18', '18.1-20', '20.1-22', '22.1-24',  '24.1-26', \
		'26.1-28', '28.1-30', '>30']

DEFAULT_COLORSCALE = ["#2a4858", "#265465", "#1e6172", "#106e7c", "#007b84", \
	"#00898a", "#00968e", "#19a390", "#31b08f", "#4abd8c", "#64c988", \
	"#80d482", "#9cdf7c", "#bae976", "#d9f271", "#fafa6e"]

DEFAULT_OPACITY = 0.8

mapboxAccessToken = 'pk.eyJ1IjoiYW5qYWxpcmF2ZWVuZHJhbiIsImEiOiJjazgwZ3RjdG8wNTBxM2dtc2toZnU4bW8zIn0.cNgbDLku-qod0zbzncY4Rw',


app.layout = html.Div([
                html.Div([
                    dcc.Slider(
                        id='years-slider',
                        min=min(YEARS),
                        max=max(YEARS),
                        value=min(YEARS),
                        marks={str(year): str(year) for year in YEARS},
                               ),
                    ], style={'width':400, 'margin':25}),

                html.Div([
                    dcc.Graph(
                        id='scatter',
                        figure = px.scatter_mapbox(df_scatter,lat="latitude", lon="longitude", color="region",  size="sumCases",
                                  color_continuous_scale=px.colors.cyclical.Twilight, size_max=50, mapbox_style="open-street-map", height=700,
                                  zoom=2.5, width=1150,
                                )
                              )
                ]),

])


@app.callback(
		Output('scatter', 'figure'),
		[Input('years-slider', 'value')],
		[State('scatter', 'figure')])
def display_map(year, map_checklist, figure):
	cm = dict(zip(BINS))

#
#
# for bin in BINS:
#     geo_layer = dict(
#         sourcetype='geojson',
#         source=df_scatter + str(df_scatter.reportingYear==2004)
#     )
# layout['mapbox']['layers'].append(geo_layer)


