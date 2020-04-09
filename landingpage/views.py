# imports for new csv upload method
import csv, io
from django.contrib import messages
from django.contrib.auth.decorators import permission_required

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.core.serializers import serialize
from django.http import HttpRequest, HttpResponse
from .models import Avian14to17Data, EmpresDomesticWildHuman
import pandas as pd
import landingpage.admin


##################### Create your views here. ################################

def home(request):
    """ Renders home page """
    return render(request, "home.html", { #used to be  '/home/home.html'
        'title': 'user_home',
    })

def avian14to17data_dataset(request):

    avian14to17data = serialize('geojson', Avian14to17Data.objects.all())
    print ( 'Json serialised outbreak data - ' )
    print ( avian14to17data[:100] )

    return HttpResponse(avian14to17data, content_type='json')

def empresdomesticwildhuman_dataset(request):

    empresdomesticwildhuman = serialize('geojson', EmpresDomesticWildHuman.objects.all())
    print ( 'Json serialised outbreak data - ' )
    print ( empresdomesticwildhuman[:100] )

    return HttpResponse(empresdomesticwildhuman, content_type='json')

#
# @permission_required('admin.can_add_log_entry')
# def dataset_upload(request):
#     template = "dataset_upload.html"
#
#     prompt = {
#         'order': 'Order of CSV should be '
#     }
#
