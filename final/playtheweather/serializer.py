from rest_framework import serializer
from .models import UserLocation

class UserLocation(serializers.ModelSerializer):
    class Meta:
        model = UserLocation
        fields = ('zip','lon','lat','city','country','time')