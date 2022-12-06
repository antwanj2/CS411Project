from django.shortcuts import render
import requests
import json
from . import apikeys
from requests_oauthlib import OAuth2Session
from requests.auth import HTTPBasicAuth


# Create your views here.
openweathermap_key = apikeys.openweathermap_key
spotify_base_address = "https://api.spotify.com"
Client_ID = apikeys.Client_ID
Client_Secret = apikeys.Client_Secret
authorization_base_url = "https://accounts.spotify.com/authorize"
token_url = "https://accounts.spotify.com/api/token"
scope = ["user-read-email","playlist-modify-public"]
redirect_uri = "PlayTheWeather/zipcode" #what is it?
#homepage view
def homepage(request):
#check whether or not the user is signed in
# if they're signed in forward them to the zipcode page
#if they're not display a page that will describe our app and prompt them to log in
#if they have never signed in before add them to the database with null as their zipcode
#once they log in direct them to the zipcode page
    #this code is mostly from https://github.com/requests/requests-oauthlib/blob/master/docs/examples/spotify.rst
    spotify = OAuth2Session(Client_ID, scope=scope, redirect_uri=redirect_uri)
    authorization_url, state = spotify.authorization_url(authorization_base_url)
    print('Please go here and authorize: ', authorization_url)
    redirect_response = input('\n\nPaste the full redirect URL here: ') #not sure what the redirect url is
    auth = HTTPBasicAuth(Client_ID, Slient_Secret)
    token = spotify.fetch_token(token_url, auth=auth, authorization_response=redirect_response)
    #add the token to models.py
    r = spotify.get('https://api.spotify.com/v1/me')
    return render(request, 'PlayTheWeather/homepage.html')

#zipcode view
def zipcode(request):
#this should also have access to the settings page so we can log out
#have link to settings to change zipcode
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
#option to change zipcode
#this will need to call a function that can change the zipcode which will need to be added to models.py i believe
    return render(request, 'PlayTheWeather/settings.html')