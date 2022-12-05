from django.db import models

# Create your models here
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    pass



class Profile(models.Model):
    points = models.IntegerField(default=0)


