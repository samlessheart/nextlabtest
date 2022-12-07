from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from .models import Tasks, OurApps
CustomUser = get_user_model()


@receiver(post_save, sender= Tasks)
def create_task(sender, instance , created, **kwargs):
    if created:
        app = instance.apps
        user = instance.user.profile
        user.points = user.points + app.points
        user.save()

        




