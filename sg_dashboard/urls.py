from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='sg-dashboard'),
    path('historical', views.historical_empty, name='sg-historical-empty'),
    path('historical/<int:year>/<str:month>/',
         views.historical, name='sg-historical'),
    path('api/<int:year>/<str:month>/',
         views.historical_api, name='sg-historical-api'),
    path('land-suitability', views.land_suitability, name='sg-land-suitability'),
]
