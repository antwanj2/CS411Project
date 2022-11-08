from django.shortcuts import render
import requests
from apikeys import openweather_key

# Create your views here.
def post_list(request):
    return render(request, 'prototype/post_list.html', {}) #i changed this to say prototype instead of blog because my template is looking for blog not prototype

def zip(request): #function to turn zipcodes into lat/lon? idk how to test it yet it does not work
    user_zip = request.META.get('wtf idk what this means', '')
    response = requests.get('http://api.openweathermap.org/geo/1.0/zip?zip=%s,US&appid=%s' % user_zip % openweather_key)
    zipdata = response.json()
    return render(request, 'prototype/post_list.html', {
  "zip": zipdata['zip'],
  "name": zipdata['name'],
  "lat": zipdata['lat'],
  "lon": zipdata['lon'],
  "country": zipdata['country']
})
    