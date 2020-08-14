from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from .models import Temperature
from .scripts.requestdata import get_data, get_month_records
from .forms import LandSuitabilityForm
import threading
# kafka function
from .scripts.consumer import consumer_kafka


#
#   dashboard index page
#
@login_required
def index(request):
    # start kafka thread for receiving data
    threading.Thread(target=consumer_kafka).start()
    return render(request, 'sg_dashboard/index.html', {'title': 'Dashboard'})


#
#
#
@login_required
def historical_empty(request):
    return render(request, 'sg_dashboard/historical_empty.html', {'title': 'Historical data'})


#
# Get data from the database about the month and the year
#
@login_required
def historical(request, year, month):
    return render(request, 'sg_dashboard/historical.html', context={'title': 'Historical', 'year': year, 'month': month})


#
# Get data from the database about the month and the year and provide it for API requests
#
def historical_api(reques, year, month):
    results = get_month_records(year, month)
    return JsonResponse(results)


#
#   Data page (for API)
#
def data(request):
    response = get_data()
    return JsonResponse(response)


#
#   Method to handle land suitability prediction form
#
def handleForm(request):
    # Handling the land suitability form
    form = LandSuitabilityForm(request.POST)
    # check form validity
    if form.is_valid():
        temperature = form.cleaned_data['temperature']
        humidity = form.cleaned_data['humidity']

        print(f'{temperature=}')
        print(f'{humidity=}')

        return render(request, 'sg_dashboard/historical_empty.html', {'title': 'Historical data'})


#
#   Get data about land suitability
#
@login_required
def land_suitability(request):
    # handle form
    if request.method == 'POST':
        return handleForm(request)
    else:
        # Create and render form
        form = LandSuitabilityForm()
        return render(request, 'sg_dashboard/land_suitability.html', {'form': form})
