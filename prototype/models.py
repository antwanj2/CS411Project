from django.conf import settings
from django.db import models
from django.utils import timezone

class zipToCoords(models.Model): #i dont think there is a purpose to this actually
    zip = models.CharField(max_length=7)
    name = models.CharField(max_length = 200) #name of the city
    lat = models.CharField(max_length = 200)
    lon = models.CharField(max_length = 200)
    country = models.CharField(max_length = 200)

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title