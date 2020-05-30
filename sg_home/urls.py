from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='sg-home'),
    path('about', views.about, name='sg-about')
]
