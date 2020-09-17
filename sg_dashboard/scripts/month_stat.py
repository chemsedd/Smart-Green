import pandas as pd
from ..models import Monthly_records_stats

#df = pd.read_csv('D:\works\master-2\smart_green\sg_dashboard\scripts\\all-data.csv')


def get_describe(df):
    res = pd.DataFrame()
    for group in df.groupby(['Year', 'Month']):
        month = group[1].iloc[:, 3:].describe()
        print(month)


def get_month_stats(df: pd.DataFrame):
    """ Returns DataFrame contains monthly statistics 

    Args:
        df (pd.DataFrame): Historical data of the farming field
    """
    res = pd.DataFrame()
    for group in df.groupby(['Year', 'Month']):
        mr = Monthly_records_stats()
        # Get month stats
        month = group[1].iloc[:, 3:].describe()

        # Date
        mr.month = group[0][1]
        mr.year = group[0][0]

        # Temperature
        mr.min_temp = month.loc['min', 'Temp_min']
        mr.avg_temp = month.loc['mean', 'Temp_avg']
        mr.max_temp = month.loc['max', 'Temp_max']

        # Humidity
        mr.min_rel_humid = month.loc['min', 'Relative Humidity']
        mr.avg_rel_humid = month.loc['mean', 'Relative Humidity']
        mr.max_rel_humid = month.loc['max', 'Relative Humidity']

        # Precipitation
        mr.min_prec = month.loc['min', 'Precipitation']
        mr.avg_prec = month.loc['mean', 'Precipitation']
        mr.max_prec = month.loc['max', 'Precipitation']

        # Pressure
        mr.min_pressure = month.loc['min', 'Pressure']
        mr.avg_pressure = month.loc['mean', 'Pressure']
        mr.max_pressure = month.loc['max', 'Pressure']
        mr.save()
