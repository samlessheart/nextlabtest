from django.db import models



# Create your models here
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    pass



class Profile(models.Model):
    
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='profile')
    points = models.IntegerField(default=0)



