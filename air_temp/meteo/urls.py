from django.urls import path
from meteo.views import temp_here, temp_somewhere

urlpatterns = [
    path('meteo/', temp_here, name='temp_here'),
    path('meteo/discover', temp_somewhere, name='temp_somewhere'),
]
