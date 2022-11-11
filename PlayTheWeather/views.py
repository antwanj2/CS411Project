from django.shortcuts import render
import requests
import json
from apikeys import openweather_key

# Create your views here.

#homepage view
def homepage(request):
#check whether or not the user is signed in
# if they're signed in forward them to the zipcode page
#if they're not display a page that will describe our app and prompt them to log in
#if they have never signed in before add them to the database with null as their zipcode
#once they log in direct them to the zipcode page
    return render(request, 'PlayTheWeather/homepage.html')

#zipcode view
def zipcode(request):
#if they have entered a zipcode before ask if they wanna keep it or change
#if not (zipcode == null) just ask to enter a zipcode
#then hit a button that will open a new view with the generate button playlist
    return render(request, 'PlayTheWeather/zipcode.html')

#generate button playlist view
def playlist(request):
#display weather
#call spotify API here and then open up the link to the spotify playlist
    return render(request, 'PlayTheWeather/playlist.html')

#settings view
def settings(request):
#not sure what settings we will have here but i bet we will need em
#definitely the option to log out
    return render(request, 'PlayTheWeather/settings.html')