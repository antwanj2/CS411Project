from django.shortcuts import render
from rest_framework.views import APIView
from requests import Request, post
from rest_framework import status
from rest_framework.response import Response
from .util import *
import urllib.request
from api.models import Room
import json 
from .credentials import api_key

# Create your views here.
def index(request):

    if request.method == 'POST':
        city = request.POST['city']

        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' +
                                        city + '&units=metric&appid=<YOUR API KEY>').read()
        list_of_data = json.loads(source)

        data = {
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ', '
            + str(list_of_data['coord']['lat']),

            "temp": str(list_of_data['main']['temp']) + ' °C',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
            'main': str(list_of_data['weather'][0]['main']),
            'description': str(list_of_data['weather'][0]['description']),
            'icon': list_of_data['weather'][0]['icon'],
        }
        print(data)
    else:
        data = {}

    return render(request, "./frontend/index.html ", data)
    #weather_id meanings:
        #2XX = thunderstorm
        #3XX = drizzle
        #5XX = rain
        #6XX = Snow
        #7XX = random atmosphere
        #8XX = clear/cloudy

def no_api_playlist(request):
    #I used official spotify playlists for all of the general weather conditions
    if int(weather_id) >= 800: #cloudy/clear
        playlist_url = 'https://open.spotify.com/playlist/37i9dQZF1DX1BzILRveYHb?si=525261fed6aa4496'
    elif int(weather_id) >= 700: #random atmosphere
        playlist_url = 'https://open.spotify.com/playlist/37i9dQZF1EIgdrHtsTSmGq?si=9120e366c25242c6'
    elif int(weather_id) >= 600: #snow
        playlist_url = 'https://open.spotify.com/playlist/37i9dQZF1DX64iwDddhmfW?si=655e2968a213472b'
    elif int(weather_id) >= 500: #rain
        playlist_url = 'https://open.spotify.com/playlist/37i9dQZF1EIelivQWnxTte?si=07d0b268ef894ab3'
    elif int(weather_id) >= 300: #drizzle
        playlist_url = 'https://open.spotify.com/playlist/37i9dQZF1DX2mFmJUZg4Mp?si=fdbf5e472cfa4058'
    else: #thunder
        playlist_url = 'https://open.spotify.com/playlist/37i9dQZF1DWXKbJeFbii64?si=8df0d8fa5f664b15'
    return render(request, 'PlayTheWeather/playlist.html', {playlist_url})
