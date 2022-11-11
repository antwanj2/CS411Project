from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

#database for the spotify users?
class Spotify_User(models.Model):
    username = models.CharField(max_length=200)
    latest_zipcode = models.IntegerField()
    #???
    def __str__(self):
        return self.username
