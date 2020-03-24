
from django.conf.urls import url, include

from .views import home, avian14to17data_dataset, empresdomesticwildhuman_dataset  # dataCharts


urlpatterns = [
     url(r'^/home$', home, name= "user_home"),                         #url correpsonding to landingpage directory home
     # url(r'^datacharts/$', dataCharts, name='datacharts'),  # url correpsonding to data charts page
     url(r'^avian14to17data/$', avian14to17data_dataset, name = 'avian14to17data' ),    #url correpsonding to landingpage directory outbreakdata_dataset view
     url(r'^empresdomesticwildhuman/$', empresdomesticwildhuman_dataset, name='empresdomesticwildhuman'),

]

print ( '-'*10)
print ( urlpatterns )
print ( '-'*10)