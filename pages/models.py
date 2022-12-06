from django.db import models
from django.contrib.auth import get_user_model

CustomUser = get_user_model()
# Create your models here.

category = [('1', 'Entertainment'),  ('2', 'Productiivity'),   ('3' ,'News')]

sub_category = [('11','Game'), ('12','Widgets'), 
                    ('13', 'Educational'), ('14','Social'), ('16','shopping'), ('15','finance')]



class OurApps(models.Model):
    name = models.CharField(max_length=20, unique= True)
    photo = models.ImageField(upload_to='appphoto/',  null=True)
    app_link = models.CharField(max_length=50,)
    category = models.CharField(max_length=20, choices= category, )
    sub_category = models.CharField(max_length=20, choices=sub_category)
    points = models.IntegerField()

    def __str__(self):
        return self.name


class Tasks(models.Model):
    apps = models.ForeignKey(OurApps, on_delete=models.SET_NULL, null=True )
    photo = models.ImageField(upload_to="taskphoto/" , null= True)
    confirmed = models.BooleanField(default=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='tasks')


OurApps.objects.filter( )