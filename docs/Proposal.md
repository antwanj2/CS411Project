# Idea 1 - Route Finder 

Collect data from a user's schedule on Google Calendar and recommend a route for their day to get them from home, to each of their commitments, and back home at the end of the day. For travel options, we will ask the user about their preference (walking/bus/train) and whether they have a car. This application would help users to accurately estimate their travel time and, in turn, avoid being late. This app could also be helpful for people who are new to the city (eg. BU freshmen or transfer students). 

State 1: User signs into their Google Calendar account 

State 2: User enters their home address (or we locate them)

State 3: User enters/ranks their travel preferences 

State 4: App generates multiple routes for the day

State 5: User chooses their preferred route 

State 6: App saves the chosen route to the user's account and sends reminders when the user should leave their location

## APIs

* [MBTA](https://www.programmableweb.com/api/mbta)
* [Google Calendar](https://www.programmableweb.com/api/google-calendar) 
* [Google Maps](https://www.programmableweb.com/api/google-maps)


# Idea 2 - Play the Weather

Create a Spotify playlist based on the weather at the user's location (mood: rainy=sad, etc) and the user's favorite artists/genres. Potential add-on: BeReal like feature, where the user gets a notification at a random time during the day and is prompted to share the last song they listened to.
This application could help users save time when it comes to finding a playlist that matches your mood - we will create one just for you! This app also has potential to help ease feelings of seasonal depression. 


State 1: User signs into their Spotify account

State 2: User enters their zipcode (or we locate them)

State 3: Use a weather API and zipcode to get weather forecast at user's location

State 4: App generates a playlist based on the weather forecast and user's music preferences

State 5: User may edit the playlist if they desire

## APIs

* [Weather](https://www.programmableweb.com/api/weather-channel) 
* [Spotify](https://www.programmableweb.com/api/spotify-web)
