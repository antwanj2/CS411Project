from django.urls import path
from . import views
from .views import AuthURL

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('get-auth-url', AuthURL.as_view()),
    path('zipcode', views.zipcode),
    path('playlist', views.playlist),
    path('settings', views.settings),
]