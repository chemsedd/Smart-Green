import calendar
import pandas as pd
from django.db import models


MONTHS = [(str(i), calendar.month_name[i]) for i in range(1, 13)]


class Temperature(models.Model):
    year = models.IntegerField(db_column='Year')
    month = models.CharField(max_length=20, choices=MONTHS)
    min_temp = models.IntegerField(db_column='Minimum')
    avg_temp = models.IntegerField(db_column='Average')
    max_temp = models.IntegerField(db_column='Maximum')

    # Converts the QuerySet object into a Dictionary
    def to_dict(self):
        return {
            'year': self.year,
            'month': self.month,
            'min_temp': self.min_temp,
            'avg_temp': self.avg_temp,
            'max_temp': self.max_temp
        }


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
class Monthly_records(models.Model):
    year = models.IntegerField(db_column='Year')
    month = models.CharField(max_length=20, choices=MONTHS)
    min_temp = models.FloatField(db_column='Min Temperature')
    avg_temp = models.FloatField(db_column='Avg Temperature')
    max_temp = models.FloatField(db_column='Max Temperature')
    avg_prec = models.FloatField(db_column='Avg Precipitation')
    avg_rel_humid = models.FloatField(db_column='Avg Relative Humidity')
    avg_pressure = models.FloatField(db_column='Avg Pressure')

    # Row representation
    def __str__(self):
        return f'{self.day} - {self.month} - {self.year}'
