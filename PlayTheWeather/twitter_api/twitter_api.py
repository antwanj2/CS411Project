import tweepy
from decouple import config
from . import apikeys

class TwitterAPI:
    def __init__(self):
        #read settings from our ‘.env’ file
        self.api_key = apikeys.twitter_api
        self.api_secret = apikeys.tiwtter_secret_api
        self.client_id = config('TWITTER_CLIENT_ID') #not sure what this is supposed to be
        self.client_secret = config('TWITTER_CLIENT_SECRET') #not sure what this is supposed to be
        self.oauth_callback_url = config('TWITTER_OAUTH_CALLBACK_URL') #not sure what this is supposed to be

    def twitter_login(self):
        #authenticate our application with the Twitter API and request a login URL. We also return the access tokens to store them later.
        oauth1_user_handler = tweepy.OAuthHandler(self.api_key, self.api_secret, callback=self.oauth_callback_url)
        url = oauth1_user_handler.get_authorization_url(signin_with_twitter=True)
        request_token = oauth1_user_handler.request_token["oauth_token"]
        request_secret = oauth1_user_handler.request_token["oauth_token_secret"]
        return url, request_token, request_secret

    def twitter_callback(self,oauth_verifier, oauth_token, oauth_token_secret):
        #called by Twitter after successful user login. We confirm the received token and get our final access tokens
        oauth1_user_handler = tweepy.OAuthHandler(self.api_key, self.api_secret, callback=self.oauth_callback_url)
        oauth1_user_handler.request_token = {
            'oauth_token': oauth_token,
            'oauth_token_secret': oauth_token_secret
        }
        access_token, access_token_secret = oauth1_user_handler.get_access_token(oauth_verifier)
        return access_token, access_token_secret

    def get_me(self, access_token, access_token_secret):
        #returns the Twitter user basic profile information
        try:
            client = tweepy.Client(consumer_key=self.api_key, consumer_secret=self.api_secret, access_token=access_token,
                                   access_token_secret=access_token_secret)
            info = client.get_me(user_auth=True, expansions='pinned_tweet_id')
            return info
        except Exception as e:
            print(e)
            return None