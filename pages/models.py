from django.db import models

# Create your models here.

class OurApps(models.Model):
    name = models.CharField(max_length=20, unique= True)
    photo = models.ImageField(upload_to='appphoto/', null=True)
    app_link = models.CharField(max_length=50,)
    category = models.CharField(max_length=20,)
    sub_category = models.CharField(max_length=20,)
    points = models.IntegerField()


class Tasks(models.Model):
    apps = models.ForeignKey(OurApps, on_delete=models.SET_NULL, null=True )
    photo = models.ImageField(upload_to="taskphoto/" )
    confirmed = models.BooleanField(default=False)


