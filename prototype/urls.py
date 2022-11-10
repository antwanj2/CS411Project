from django.urls import path
from . import views
from .views import zip

urlpatterns = [
    # path('', views.post_list, name='post_list'),
    path('', views.zip, name='zip'), #i think zip is the variable name ill call it
]