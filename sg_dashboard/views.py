from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render

from .models import Temperature
from .scripts.requestdata import get_data, get_month_records


'''
    dashboard index page
'''


@login_required
def index(request):
    return render(request, 'sg_dashboard/index.html', {'title': 'Dashboard'})


"""
    
"""


@login_required
def historical_empty(request):
    # results = get_month_records(year, month)
    return render(request, 'sg_dashboard/historical_empty.html', {'title': 'Historical data'})


"""
    Get data from the database about the month and the year
"""


@login_required
def historical(request, year, month):
    return render(request, 'sg_dashboard/historical.html', context={'title': 'Historical', 'year': year, 'month': month})


"""
    Get data from the database about the month and the year and provide it for API requests
"""


def historical_api(reques, year, month):
    results = get_month_records(year, month)
    return JsonResponse(results)


'''
    Data page (for API)
'''


def data(request):
    response = get_data()
    return JsonResponse(response)


'''
    Get data about land suitability
'''


def land_suitability(request):
    suitability_infos = {}
    return render(request, 'sg_dashboard/land_suitability.html', context=suitability_infos)
