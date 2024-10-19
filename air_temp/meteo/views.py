from datetime import datetime

import geocoder
import requests
from django.http import HttpResponse
from django.template import loader

from meteo.models import WorldCity


def temp_here(request):
    lat, lng = geocoder.ip('me').latlng
    temp = get_temp(lat, lng)
    template = loader.get_template('index.html')
    context = {
        'temp': temp,
        'city': 'Your location',
    }
    return HttpResponse(template.render(context, request))

def temp_somewhere(request):
    random_item = WorldCity.objects.all().order_by('?').first()
    temp = get_temp(random_item.lat, random_item.lng)
    template = loader.get_template("index.html")
    context = {
        'country': random_item.country,
        'city': random_item.city,
        'temp': temp
    }
    return HttpResponse(template.render(context, request))

def get_temp(latitude, longitude):
    endpoint = "https://api.open-meteo.com/v1/forecast"
    api_request = f"{endpoint}?latitude={latitude}&longitude={longitude}&hourly=temperature_2m"
    now = datetime.now()
    meteo_data = requests.get(api_request).json()
    return meteo_data['hourly']['temperature_2m'][now.hour]
