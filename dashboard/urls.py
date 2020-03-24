"""dashboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() f unction: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path

from .views import welcome, choropleth, dashChartView, phrerView, scatterView
from dash_apps.finished_apps import dashChart, phrerMap, scatterMap

urlpatterns = [
    url(r'^admin/', admin.site.urls),       # Including admin url from django source code
    url(r'^', include('landingpage.urls')), # Including all urls from landingpage folder
    url(r'^', include('home.urls')),        # Including all urls from home  folder
    url(r'^$', welcome, name="dashboard_welcome"),  #including url corresponding to view from the dashboard folder
    url(r'^choropleth/$', choropleth, name='choropleth'),
    url(r'^charts/$', dashChartView, name='dashChart'),
    url(r'^phrer/$', phrerView, name='phrerMap'),
    url(r'^scatter/$', scatterView, name='scatterMap'),
    path('django_plotly_dash/', include('django_plotly_dash.urls')), #django import
]

print ( '-'*50)
print ( urlpatterns )
print ( '-'*50)