from django.db import models
from django.contrib.auth import get_user_model
from PIL import Image
CustomUser = get_user_model()
from django.core.files import File
from io import BytesIO
from PIL import Image
# Create your models here.

category = [('1', 'Entertainment'),  ('2', 'Productiivity'),   ('3' ,'News')]

sub_category = [('11','Game'), ('12','Widgets'), 
                    ('13', 'Educational'), ('14','Social'), ('16','shopping'), ('15','finance')]

def compress_image(image):
    im = Image.open(image)
    if im.mode != 'RGB':
        im = im.convert('RGB')
    im_io = BytesIO()
    im.save(im_io, 'jpeg', quality=70,optimize=True)
    new_image = File(im_io, name=image.name)
    return new_image


class OurApps(models.Model):
    name = models.CharField(max_length=20, unique= True)
    photo = models.ImageField(upload_to='appphoto/',  null=True)
    app_link = models.CharField(max_length=50,)
    category = models.CharField(max_length=20, choices= category, )
    sub_category = models.CharField(max_length=20, choices=sub_category)
    points = models.IntegerField()

    def __str__(self):
        return self.name
    def save(self,force_insert=False, force_update=False, using=None,*args, **kwargs):
        if self.photo:
            image = self.photo
            if image.size > 0.3*500*500: #if size greater than 300kb then it will send to compress image function
                self.photo = compress_image(image)
        super(OurApps, self).save(*args, **kwargs)


class Tasks(models.Model):
    apps = models.ForeignKey(OurApps, on_delete=models.SET_NULL, null=True )
    photo = models.ImageField(upload_to="taskphoto/" , null= True)
    confirmed = models.BooleanField(default=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='tasks')


