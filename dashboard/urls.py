from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path

# Importing view functions of the choropleth map, dash charts and the PHRER visualisation
from .views import welcome, choropleth, dashchartView, phrerView

#Importing our plotly-dash apps: dashchart and phrerMap
from dash_apps.finished_apps import dashchart, phrerMap

urlpatterns = [
    url(r'^admin/', admin.site.urls),       # Including admin url from django source code
    url(r'^', include('landingpage.urls')), # Including all urls from landingpage folder
    url(r'^', include('home.urls')),        # Including all urls from home folder
    url(r'^$', welcome, name="dashboard_welcome"),  #including url corresponding to view from the dashboard folder
    url(r'^choropleth/$', choropleth, name='choropleth'), #URL of choropleth map's view function
    url(r'^charts/$', dashchartView, name='dashchart'), #URL of dashchartView function
    url(r'^phrer/$', phrerView, name='phrerMap'), #URL of phrerView function
    path('django_plotly_dash/', include('django_plotly_dash.urls')), #django-dash import
]
