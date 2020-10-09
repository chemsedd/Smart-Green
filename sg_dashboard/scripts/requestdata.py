# import pandas as pd
from numpy.random import randint
import threading
from sg_dashboard.models import Daily_records, Monthly_records_stats
from .consumer import consumer_kafka

months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']


# Return the data of the selected month-year
def get_month_records(year, month: str):
    """Returns the data of the selected month-year

    Args:
        year (int): Year (2009 - 2019)
        month (str): Month (Janvuary - December)

    Returns:
        dict: A dict that contains data retrieved from the database
    """
    # Retrieve data from the DATABASE
    records = Daily_records.objects.filter(
        year=year, month=month)
    stats = Monthly_records_stats.objects.filter(
        year=year, month=month).values()[0]

    results = {
        'Data': {
            'province': 'Biskra',
            'country': 'Algeria',
            'month': month,
            'year': year,
        },
        'Days': [rec for rec in records.values()],
        'Stats': stats
    }

    return results
