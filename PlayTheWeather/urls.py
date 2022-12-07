from django.urls import path, include
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('zipcode', views.zipcode),
    path('playlist', views.playlist),
    path('settings', views.settings),
    path('twitter_login/', views.twitter_login, name='twitter_login'),
    path('twitter_callback/', views.twitter_callback, name='twitter_callback'),
    path('twitter_logout/', views.twitter_logout, name='twitter_logout'),
    path('admin/', admin.site.urls),
]