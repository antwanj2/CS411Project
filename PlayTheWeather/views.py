from django.shortcuts import render
import requests
import json
from rest_framework.views import APIView 
#from apikeys import openweather_key
from .credentials import REDIRECT_URI, CLIENT_SECRET, CLIENT_ID
from .util import *

# Create your views here.
# Spotify authentication process: 

class AuthURL():
    def get(self, request, format = None): 
        scopes = 'user-read-playback-state '

        url = request.get('https://accounts.spotify.com/authorize', parama={
            'scope': scopes,
            'response_type': 'code',
            'redirect_url': REDIRECT_URI,
            'client_id': CLIENT_ID
        }).prepare().url 
        return request.response({'url': url}, status = status.HTTP_200_OK)
   
def spotify_callback(request, format= None):
    success = request.get('success')
    error = request.get('Error')
    response = request.post('https://accounts.spotify.com/api/token', data={ 
        'grant_type': 'auth_code',
        'success': success
        'redirect_uri': REDIRECT_URI,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET }).json()

    access_token = request.get('access_token')
    token_type = request.get('token_type')
    refresh_token = request.get('refresh_token')
    expires_in = request.get('expires_in')
    error = response.get('error')

    if not request.session.exists(request.session.session_key):
        request.session.create()

    update_or_create_tokens(
        request.session.session_key, access_token, token_type, expires_in, refresh_token)

class IsAuthenticated(APIView):
    def get(self, request, format=None):
        is_authenticated = is_spotify_authenticated(
            self.request.session.session_key)
        return request({'status': is_authenticated}, status=status.HTTP_200_OK)




#homepage view
async def homepage(request):
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