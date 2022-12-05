from django import forms
from django.forms import (fields, widgets, Textarea, NumberInput, Select, DateField)
from .models import OurApps, Tasks


class OurAppsForms(forms.ModelForm):
    class Meta:
        model= OurApps
        fields = ["name", "photo", "app_link", "category", "sub_category", "points"]

        widgets = {
            'name': Textarea(attrs={'rows': 1, 'class': 'form-control col-8'}),
            'app_link': Textarea(attrs={'rows': 1, 'class': 'form-control col-8'}),
            'category': Select(attrs={ 'rows': 1, 'class': 'form-control col-8'}),
            'sub_category': Select(attrs={ 'rows': 1, 'class': 'form-control col-8'}),
            'points': NumberInput(attrs={'rows': 1, 'class': 'form-control col-8'}),
        }

class TasksForm(forms.Form):
        photo = forms.ImageField(label="Add a Screenshot")

        

    
        
