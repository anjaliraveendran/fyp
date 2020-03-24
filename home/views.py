from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect, get_object_or_404

from django.template import RequestContext
from datetime import datetime
from django.core.serializers import serialize

import pandas as pd
from django.contrib.auth.decorators import login_required


# # Create your views here.

@login_required
def home(request):

    # breakpoint()
    return render(request, "home/home.html",{
        'title':'user_home',
    })



