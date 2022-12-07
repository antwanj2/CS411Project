#contains some helper functions to help us with the authorization process
#https://blog.devgenius.io/how-to-login-with-twitter-on-django-cdc11c8b470a

from django.contrib.auth.models import User
from . import twitter_api
from .models import TwitterUser


def create_update_user_from_twitter(twitter_user_new):
    #receives a TwitterUser (from our model) and determines if it needs to create or update a new Django user 
    # and TwitterUser. It also associates the final tokens with the created user.
    twitter_user = TwitterUser.objects.filter(twitter_id=twitter_user_new.twitter_id).first()
    if twitter_user is None:
        user = User.objects.filter(username=twitter_user_new.screen_name).first()
        if user is None:
            user = User(username=twitter_user_new.screen_name,
                        first_name=twitter_user_new.name)
            user.save()
        twitter_user = TwitterUser(twitter_id=twitter_user_new.twitter_id,
                                   name=twitter_user_new.name,
                                   screen_name=twitter_user_new.screen_name,
                                   profile_image_url=twitter_user_new.profile_image_url)
        twitter_user.user = user
        twitter_user.twitter_oauth_token = twitter_user_new.twitter_oauth_token
        twitter_user.save()
        return user, twitter_user
    else:
        twitter_user.twitter_oauth_token = twitter_user_new.twitter_oauth_token
        twitter_user.save()
        user = twitter_user.user
        if user is not None:
            return user, twitter_user
        else:
            return None, twitter_user


def check_token_still_valid(twitter_user):
    #used to determine if a user still has a valid session on Twitter
    twitter_api = TwitterAPI()
    info = twitter_api.get_me(twitter_user.twitter_oauth_token.oauth_token,
                              twitter_user.twitter_oauth_token.oauth_token_secret)
    return info