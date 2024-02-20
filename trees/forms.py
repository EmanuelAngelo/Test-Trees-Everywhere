from django import forms
from .models import PlantedTree



class LoginForm(forms.Form):
  username = forms.CharField()
  password = forms.CharField(widget=forms.PasswordInput)

class PlantedTreeForm(forms.ModelForm):
  class Meta:
    model = PlantedTree
    fields = ['tree', 'age', 'location_latitude', 'location_longitude']