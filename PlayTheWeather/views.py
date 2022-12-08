from django.shortcuts import render
import requests
import json
from . import apikeys

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
#this should also have access to the settings page so we can log out
#have link to settings to change zipcode
#if not (zipcode == null) just ask to enter a zipcode
#then hit a button that will open a new view with the generate button playlist
    if request.zipcode == None:
        print("enter zipcode again")
        return 
    else:
        user_zip = request.POST.get('zipcode','') 
        response = requests.get('https://api.openweathermap.org/data/2.5/weather?zip=%s,us&appid=d29579363a4d3c6b0eb89de9f488eb3c', user_zip) 
        zipdata = response.text
        zipdatajson = json.loads(zipdata)
        if response.status_code == 404:
            return render(request, 'prototype/error.html')
        else:
            return render(request, 'PlayTheWeather/zipcode.html', {
            'temp': zipdatajson['main.temp'], #i'm not sure if this is the correct way to read JSON files -amelia
            'weather_id': zipdatajson['weather.id'], #this id we will use to determine which playlist to use
            'weather_desc': zipdatajson['weather.discription'] #we want to display the weather_desc to user because it's more specific
            })
    #weather_id meanings:
        #2XX = thunderstorm
        #3XX = drizzle
        #5XX = rain
        #6XX = Snow
        #7XX = random atmosphere
        #8XX = clear/cloudy


#generate button playlist view
def playlist(request):
#display weather
#call spotify API here and then open up the link to the spotify playlist
#link to settings page
    playlist_url = "https://api.spotify.com/v1/users/" + str(request.user_id) + "/playlists"
    access_token = request.access_token
   #based off of https://www.youtube.com/watch?v=c5sWvP9h3s8
    response = requests.post(
        playlist_url,
        headers={
             "Authorization": f"Bearer {request.access_token}"
        },
        json={
            "name": name,
            "public": public
        }
    )
    json_resp = response.json()
    
    return render(json_resp, 'PlayTheWeather/playlist.html')

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
#settings view
def settings(request):
#not sure what settings we will have here but i bet we will need em
#definitely the option to log out
#option to change zipcode
#this will need to call a function that can change the zipcode which will need to be added to models.py i believe
    return render(request, 'PlayTheWeather/settings.html')