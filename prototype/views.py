from django.shortcuts import render
import requests
import json
from apikeys import openweather_key
from flask import Flask 
from flask import request 
from django.http import HttpResponse, HttpResponseNotFound
from .forms import ZipForm
 

def zip(request): #this just displays the form to submit the zipcode
    return render(request, 'prototype/post_list.html')

def zip_response(request): #this needs to take the response of the submit button in post_list.html and output the coords
    user_zip = request.POST.get('zipcode','') 
    response = requests.get('http://api.openweathermap.org/geo/1.0/zip?zip=%s,US&appid=d29579363a4d3c6b0eb89de9f488eb3c' % user_zip)
    zipdata = response.text
    zipdatajson = json.loads(zipdata)
    if response.status_code == 404:
      return render(request, 'prototype/error.html')
    else:
      return render(request, 'prototype/zipcode_display.html', {
      'zip': zipdatajson['zip'], #now this is where we get an error, i think it might be i am reading the json file wrong
      'name': zipdatajson['name'],
      'lat': zipdatajson['lat'],
      'lon': zipdatajson['lon'],
      'country': zipdatajson['country']
      })
      # lon = zipdatajson['lon']
      # lat = zipdatajson['lat']
      # weatherAPI = requests.get('https://api.openweathermap.org/data/2.5/weather?lat=%s&appid=d29579363a4d3c6b0eb89de9f488eb3c' + '{lat}&lon={lon}')
# Create your views here.
def post_list(request):
    return render(request, 'prototype/post_list.html', {}) #i changed this to say prototype instead of blog because my template is looking for blog not prototype
    
