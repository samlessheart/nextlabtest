from django import forms
from django.forms import (fields, widgets, Textarea, NumberInput, Select, DateField, FileInput)
from .models import OurApps, Tasks


class OurAppsForm(forms.ModelForm):
    class Meta:
        model= OurApps
        fields = [ "photo", "name", "app_link", "category", "sub_category", "points"]

        widgets = {
            'photo' : FileInput(attrs={'rows': 2, 'class': 'form-control col-8'}),
            'name': Textarea(attrs={'rows': 1, 'class': 'form-control col-8 '}),
            'app_link': Textarea(attrs={'rows': 1, 'class': 'form-control col-8'}),
            'category': Select(attrs={ 'rows': 1, 'class': 'form-control col-8'}),
            'sub_category': Select(attrs={ 'rows': 1, 'class': 'form-control col-8'}),
            'points': NumberInput(attrs={'rows': 1, 'class': 'form-control col-8'}),
        }

class TasksForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['photo']

        widgets = {
            'photo': FileInput(attrs={'class':"file-upload"}),
        }
    

    
        
