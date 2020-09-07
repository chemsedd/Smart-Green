from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from .models import Temperature
from .scripts.consumer import consumer_kafka
from .scripts.requestdata import get_data, get_month_records
from tensorflow.keras.models import load_model
from .scripts.prediction_model import make_prediction
from .forms import LandSuitabilityForm
import threading


#
#   dashboard index page
#
@login_required
def index(request):
    # start kafka thread for receiving data
    # kafka_thread = threading.Thread(target=consumer_kafka)
    # kafka_thread.start()
    # added new feautre
    nbr_pics = range(1, 8)
    return render(request, 'sg_dashboard/index.html', {'title': 'Dashboard', 'nbr_pics': nbr_pics})


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


PATH = 'D:\works\master-2\smart_green\sg_dashboard\scripts\lstm_model'
model = None


#
#   Method to handle land suitability prediction form
#
def handleForm(request):
    global model
    # Handling the land suitability form
    form = LandSuitabilityForm(request.POST)
    # check form validity
    if form.is_valid():
        # Precipitation  Relative  Humidity  Pressure  Temp_avg
        precipitation = form.cleaned_data['precipitation']
        humidity = form.cleaned_data['humidity']
        pressure = form.cleaned_data['pressure']
        temperature = form.cleaned_data['temperature']

        prediction = make_prediction(model,
                                     [precipitation, humidity, pressure, temperature])
        report = {
            'result': prediction
        }
        return render(request, 'sg_dashboard/land_suitability.html', {'report': report, 'form': form})


#
#   Get data about land suitability
#
@login_required
def land_suitability(request):
    global model
    # loading the LSTM model
    if model == None:
        model = load_model(PATH)
    # handle form
    if request.method == 'POST':
        return handleForm(request)
    else:
        # Create and render form
        form = LandSuitabilityForm()
        return render(request, 'sg_dashboard/land_suitability.html', {'form': form})
