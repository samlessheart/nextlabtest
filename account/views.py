from django.shortcuts import render, redirect, render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import  logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomUserChangeForm


class SignupPageView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "account/signup.html"

@login_required(login_url='/login/')
def log_out(request):
    logout(request)
    messages.info(request, 'You are logged out')  
    return redirect('login')