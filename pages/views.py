from django.shortcuts import render
from .forms import OurAppsForms, TasksForm
# Create your views here.


from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "pages/home.html"





