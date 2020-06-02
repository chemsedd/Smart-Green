# import pandas as pd
from numpy.random import randint

from sg_dashboard.models import Historical_records, Temperature

months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']


# Return the data of the selected month-year
def get_month_records(year, month: str):
    # Retrieve data from the DATABASE
    records = Historical_records.objects.filter(
        year=year, month=month)
    # Retrieve average data of the month from DATABASE
    averages = Temperature.objects.filter(
        year=year, month=month.lower()).values('min_temp', 'avg_temp', 'max_temp')
    # Struceture days records on a list
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
    # Return results
    return results


# Get DATA api
a = 0.8
def get_data():
    data = {
        'temperature': {
            'labels': months,
            'datalabel': 'Temperature °C',
            'data': [randint(20, 30) for _ in range(12)],
            # 'bgcolors': [
            #     f'rgba(230, 242, 62, {a})',
            # ]
        },
        'humidity': {
            'labels': months,
            'datalabel': 'Humidity %',
            'data': [randint(14, 40) for _ in range(12)],
            'bgcolors':
                f'rgba(33, 150, 243, {a})',


        },
        'moisture': {
            'labels': months,
            'datalabel': 'Soil Moisture %',
            'data': [randint(14, 40) for _ in range(12)],
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
