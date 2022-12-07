from django.contrib import admin
from .models import Profile
# Register your models here.

from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm, CustomUserCreationForm

from django.contrib.auth import get_user_model
CustomUser = get_user_model()

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["email", "username", "is_superuser",]


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile )