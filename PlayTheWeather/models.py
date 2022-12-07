from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

#database for the spotify users?

#I need a function to be able to change the zipcode
    #do i need to change anything else?
#need to use the authorization api
#what else do i need?
class Spotify_User(models.Model):
    username = models.CharField(max_length=200)
    latest_zipcode = models.IntegerField()
    access_token = models.CharField(max_length=200)
    refresh_token = models.CharField(max_length=200)
    def __str__(self):
        return self.username

#https://blog.devgenius.io/how-to-login-with-twitter-on-django-cdc11c8b470a
class TwitterAuthToken(models.Model):
    oauth_token = models.CharField(max_length=255)
    oauth_token_secret = models.CharField(max_length=255)

    def __str__(self):
        return self.oauth_token


class TwitterUser(models.Model):
    twitter_id = models.CharField(max_length=255)
    screen_name = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    profile_image_url = models.CharField(max_length=255, null=True)
    twitter_oauth_token = models.ForeignKey(TwitterAuthToken, on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.screen_name
