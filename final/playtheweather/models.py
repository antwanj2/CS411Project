from django.db import models
from api.models import Room

class UserLocation(models.Model):
    zip = models.CharField(max_length=5)
    lon = models.CharField(max_length = 100)
    lat = models.CharField(max_length = 100)
    city =  models.CharField(max_length = 20)
    country =  models.CharField(max_length = 20)
    time = models.DateTimeField(auto_now_add=True)


