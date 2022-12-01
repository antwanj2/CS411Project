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
#if they have entered a zipcode before ask if they wanna keep it or change
#if not (zipcode == null) just ask to enter a zipcode
#then hit a button that will open a new view with the generate button playlist
    # username = [ENTER USERNAME]
    # access_token = [GET USERS ACCESS TOKEN]
    # playlist_url = [the url + username + token]
    # def generate_playlist(username, private): #based off of https://www.youtube.com/watch?v=c5sWvP9h3s8
    #     reponse = requests.post(
    #         playlist_url,
    #         headers={
    #             "Authorization": f"Bearer {access_token}"
    #         }
    #         json={
    #             "name": name,
    #             "public": public
    #         }
    #     )
    #     json_resp = response.json()
    #     return json_resp
    return render(request, 'PlayTheWeather/zipcode.html')

#generate button playlist view
def playlist(request):
#display weather
#call spotify API here and then open up the link to the spotify playlist
#link to settings page
    return render(request, 'PlayTheWeather/playlist.html')

#settings view
def settings(request):
#not sure what settings we will have here but i bet we will need em
#definitely the option to log out
    return render(request, 'PlayTheWeather/settings.html')