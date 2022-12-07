from django.urls import path 
from . import views

urlpatterns = [ 
    
    path("", views.home, name="home"),
    path("admindash/", views.admindash, name="admindash"),
    path("userdash/", views.userdash, name="userdash"),
    path("taskcomplete/<int:pk>", views.taskcomplete, name="taskcomplete"),
    path("profiledash/", views.profiledash, name="profiledash"),
    


]