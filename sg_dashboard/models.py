import calendar
from django.db import models

MONTHS = [(str(i), calendar.month_name[i]) for i in range(1, 13)]

# MONTHS = ['january','february','march','april','may','juin','juily','august','september','october','november','december']


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


#
class Historical_records(models.Model):
    year = models.IntegerField(db_column='Year')
    month = models.CharField(max_length=20, choices=MONTHS)
    day = models.IntegerField(db_column='Day')
    min_temp = models.FloatField(db_column='Min Temperature')
    avg_temp = models.FloatField(db_column='Avg Temperature')
    max_temp = models.FloatField(db_column='Max Temperature')
    prec = models.FloatField(db_column='Precipitation')
    rel_humid = models.FloatField(db_column='Relative Humidity')
    pressure = models.FloatField(db_column='Pressure')
