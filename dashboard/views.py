from django.shortcuts import render, redirect

def welcome(request):
    # if request.user.is_authenticated:
        return redirect('user_home')
    # else:
        # return render(request, 'dashboard/welcome.html')

def choropleth(request):
    return render(request, "choropleth.html", {
        'title': 'choropleth',
    })

def dashchartView(request):
    return render(request, "charts.html", {
        'title': 'dashchart',
    })

def phrerView(request):
    return render(request, "phrer.html", {
        'title': 'phrerMap',
    })

# def scatterView(request):
#     return render(request, "scatter.html", {
#         'title': 'scatterMap',
#     })