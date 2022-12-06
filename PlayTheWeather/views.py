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
#this should also have access to the settings page so we can log out
#have link to settings to change zipcode
#if not (zipcode == null) just ask to enter a zipcode
#then hit a button that will open a new view with the generate button playlist
    if request.zipcode == None:
        print("enter zipcode again")
        return
    else:
        return render(request, 'PlayTheWeather/zipcode.html')


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

#settings view
def settings(request):
#not sure what settings we will have here but i bet we will need em
#definitely the option to log out
#option to change zipcode
#this will need to call a function that can change the zipcode which will need to be added to models.py i believe
    return render(request, 'PlayTheWeather/settings.html')