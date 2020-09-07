import pandas as pd
from ..models import Monthly_records

#df = pd.read_csv('D:\works\master-2\smart_green\sg_dashboard\scripts\\all-data.csv')


def get_month_stat(df: pd.DataFrame):
    res = pd.DataFrame()
    for group in df.groupby(['Year', 'Month']):
        mr = Monthly_records()

        month = group[1].iloc[:, 3:].describe()
        print(month)
        mr.min_temp = month.loc['min', 'Temp_min']
        mr.avg_temp = month.loc['mean', 'Temp_avg']
        mr.max_temp = month.loc['max', 'Temp_max']

        mr.min_rel_humid = month.loc['min', 'Relative Humidity']
        mr.avg_rel_humid = month.loc['mean', 'Relative Humidity']
        mr.max_temp = month.loc['max', 'Relative Humidity']

        mr.min_prec = month.loc['min', 'Precipitation']
        mr.avg_prec = month.loc['mean', 'Precipitation']
        mr.max_prec = month.loc['max', 'Precipitation']

        mr.min_pressure = month.loc['min', 'Pressure']
        mr.avg_pressure = month.loc['mean', 'Pressure']
        mr.max_pressure = month.loc['max', 'Pressure']
        break
