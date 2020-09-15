# import pandas as pd
from numpy.random import randint
import threading

from sg_dashboard.models import Daily_records, Temperature

from .consumer import consumer_kafka

months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']


# Return the data of the selected month-year
def get_month_records(year, month: str):
    # Retrieve data from the DATABASE
    records = Daily_records.objects.filter(
        year=year, month=month)
    # Retrieve average data of the month from DATABASE
    averages = Temperature.objects.filter(
        year=year, month=month.lower()).values('min_temp', 'avg_temp', 'max_temp')
    # Structure days records on a list
    results = {
        'Data': {
            'province': 'Biskra',
            'country': 'Algeria',
            'month': month,
            'year': year,
        },
        'Days': [],
        'Month': list(averages)
    }
    for rec in records.values():
        results['Days'].append(rec)
    return results


# Get DATA api
a = 0.8


def get_data():
    data = {
        'temperature': {
            'datalabel': 'Temperature °C',
        },
        'humidity': {
            'datalabel': 'Humidity %',
            'bgcolors':
                f'rgba(33, 150, 243, {a})',


        },
        'moisture': {
            'datalabel': 'Soil Moisture %',
            'bgcolors':
                f'rgba(33, 150, 243, {a})',


        },
        'crops': {
            'labels': ['Tomato', 'Potato', 'Eggplant', 'Seeds'],
            'datalabel': 'Production %',
            'data': [randint(0, 100) for _ in range(4)],
            'bgcolors': [
                f'rgba(224, 53, 53, {a})',
                f'rgba(44, 141, 221, {a})',
                f'rgba(22, 221, 98, {a})',
                f'rgba(233, 239, 47, {a})'
            ]
        },
    }
    return data
