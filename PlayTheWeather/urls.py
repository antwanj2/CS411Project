from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('zipcode', views.zipcode),
    path('playlist', views.playlist),
    path('settings', views.settings),
]