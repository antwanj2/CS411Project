from django.urls import path, include 
from . import views

urlpatterns = [
    path('', include("frontend.urls")),
    path('zipcode', views.zipcode),
    path('playlist', views.playlist),
    path('settings', views.settings),
]