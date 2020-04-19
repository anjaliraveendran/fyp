from django.shortcuts import render, redirect

# View for homepage- Main outbreak map
def welcome(request):
        return redirect('user_home')

# View for choropleth map
def choropleth(request):
    return render(request, "choropleth.html", {
        'title': 'choropleth',
    })

# View for plotly dash scatter charts
def dashchartView(request):
    return render(request, "charts.html", {
        'title': 'dashchart',
    })

# View for the PHRER(public health response effectiveness) map
def phrerView(request):
    return render(request, "phrer.html", {
        'title': 'phrerMap',
    })
