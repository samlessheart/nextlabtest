from django.urls import path 
from .views import SignupPageView
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [ 
    
    path("signup/", SignupPageView.as_view(), name="signup"),
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html'), name='login' ),
    path('logout/', views.log_out, name='logout'),
    


]