from django.urls import path
from . import views
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('zipcode', views.zipcode),
    path('playlist', views.playlist),
    path('settings', views.settings),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]