from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

#database for the spotify users?

#I need a function to be able to change the zipcode
    #do i need to change anything else?
#need to use the authorization api
#what else do i need?

## important data needed to 
class SpotifyToken(models.Model):
    user = models.CharField(max_Length = 50, unique = True)
    created_at = models.DateTimeField(auto_now_add= True)
    refresh_token = models.CharField(max_length = 150)
    expires_in = models.DateTimeField()
    token_type = models.CharField(max_length = 50)



class Spotify_User(models.Model):
    username = models.CharField(max_length=200)
    latest_zipcode = models.IntegerField()
    access_token = models.CharField(max_length=200)
    refresh_token = models.CharField(max_length=200)
    def __str__(self):
        return self.username
