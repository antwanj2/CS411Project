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
    return

#zipcode view
def zipcode(request):
#if they have entered a zipcode before ask if they wanna keep it or change
#if not just ask to enter a zipcode
#then hit a button that will open a new view with the generate button playlist
    return

#generate button playlist view
def playlist(request):
#display weather
#call spotify API here and then open up the link to the spotify playlist
    return

#settings view
def settings(requst):
#not sure what settings we will have here but i bet we will need em
#definitely the option to log out
    return