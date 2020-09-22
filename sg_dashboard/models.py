import calendar
import pandas as pd
from django.db import models


MONTHS = [(str(i), calendar.month_name[i]) for i in range(1, 13)]


# Daily values recorded from the raspberry pi
class Daily_real_time(models.Model):
    date = models.DateTimeField(db_column='Date', auto_now=True)
    temperature = models.IntegerField(db_column='Temperature')
    #pressure = models.FloatField(db_column='Pressure')
    humidity = models.FloatField(db_column='Humidity')
    #pH = models.FloatField(db_column='pH')
    moisture = models.FloatField(db_column='Moisture')

    # Row representation
    def __str__(self):
        s = f'----------------------------\n'
        for k, v in self.__dict__.items():
            s += f'> {k:15} : {str(v):15} \n'
        s += f'----------------------------\n'
        return s


# Data for each day
class Daily_records(models.Model):
    year = models.IntegerField(db_column='Year')
    month = models.CharField(max_length=20, choices=MONTHS)
    day = models.IntegerField(db_column='Day')
    min_temp = models.FloatField(db_column='Min Temperature')
    avg_temp = models.FloatField(db_column='Avg Temperature')
    max_temp = models.FloatField(db_column='Max Temperature')
    prec = models.FloatField(db_column='Precipitation')
    rel_humid = models.FloatField(db_column='Relative Humidity')
    pressure = models.FloatField(db_column='Pressure')

    # Row representation
    def __str__(self):
        return f'{self.day} - {self.month} - {self.year}'


# Data for each month
class Monthly_records_stats(models.Model):
    year = models.IntegerField(db_column='Year')
    month = models.CharField(max_length=20, choices=MONTHS)

    min_temp = models.FloatField(db_column='min_temp')
    avg_temp = models.FloatField(db_column='avg_temp')
    max_temp = models.FloatField(db_column='max_temp')

    min_prec = models.FloatField(db_column='min_prec')
    avg_prec = models.FloatField(db_column='avg_prec')
    max_prec = models.FloatField(db_column='max_prec')

    min_rel_humid = models.FloatField(db_column='min_rel_humid')
    avg_rel_humid = models.FloatField(db_column='avg_rel_humid')
    max_rel_humid = models.FloatField(db_column='max_rel_humid')

    min_pressure = models.FloatField(db_column='min_Pressure')
    avg_pressure = models.FloatField(db_column='avg_Pressure')
    max_pressure = models.FloatField(db_column='max_Pressure')

    # Row representation

    def __str__(self):
        s = f'----------------------------\n'
        for k, v in self.__dict__.items():
            s += f'> {k:15} : {str(v):15} \n'
        s += f'----------------------------\n'
        return s
