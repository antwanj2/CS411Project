from django.shortcuts import render
import requests
import json
from apikeys import openweather_key

# Create your views here.
#homepage view
#check whether or not the user is signed in
# if they're signed in forward them to the zipcode page
#if they're not display a page that will describe our app and prompt them to log in

#zipcode view
#if they have entered a zipcode before ask if they wanna keep it or change
#if not just ask to enter a zipcode
#then hit a button that will open a new view with the generate button playlist

#generate button playlist view
#display weather
#call spotify API here and then open up the link to the spotify playlist