from django import forms
from .models import Building, Floor, Location, Person

class BuildingForm(forms.ModelForm):
    class Meta:
        model = Building
        fields = ['site_display_name', 'site_address', 'site_prefix', 'site_state']

class FloorForm(forms.ModelForm):
    class Meta:
        model = Floor
        fields = ['building', 'floor_number', 'floor_description', 'floor_image']

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['floor', 'location_name', 'location_description', 'location_url', 'x_coordinate', 'y_coordinate']

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'email', 'phone', 'location']
