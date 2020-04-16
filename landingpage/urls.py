
from django.conf.urls import url  #include

from .views import home, avian14to17data_dataset, empresdomesticwildhuman_dataset

urlpatterns = [
     url(r'^/home$', home, name= "user_home"), #url correpsonding to landingpage directory home
     url(r'^avian14to17data/$', avian14to17data_dataset, name = 'avian14to17data' ),    #url correpsonding to landingpage directory avian14to17data_dataset's view
     url(r'^empresdomesticwildhuman/$', empresdomesticwildhuman_dataset, name='empresdomesticwildhuman'),   #url correpsonding to landingpage directory empresdomesticwildhuman_dataset's view
]
