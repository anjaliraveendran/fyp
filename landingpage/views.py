from django.shortcuts import render, get_object_or_404
from django.core.serializers import serialize
from django.http import HttpRequest, HttpResponse
from .models import Avian14to17Data, EmpresDomesticWildHuman

##################### Create your views here (function-based views). ################################

def home(request):
    """ Renders home page """
    return render(request, "home.html", {
        'title': 'user_home',
    })

def avian14to17data_dataset(request):
    #Serialise our data into GeoJSON format
    avian14to17data = serialize('geojson', Avian14to17Data.objects.all())
    print ( 'Json serialised outbreak data - ' )

    return HttpResponse(avian14to17data, content_type='json')

# View function for our main outbreak map- home.html
def empresdomesticwildhuman_dataset(request):
    #Serialise our data into GeoJSON format
    empresdomesticwildhuman = serialize('geojson', EmpresDomesticWildHuman.objects.all())
    print ( 'Json serialised outbreak data - ' )
    print ( empresdomesticwildhuman[:100] )

    return HttpResponse(empresdomesticwildhuman, content_type='json')

