from django.forms import ModelForm

from .models import zipToCoords

class ZipForm(ModelForm):
    class Meta:
        model = zipToCoords
        fields = '__all__'