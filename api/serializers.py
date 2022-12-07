from rest_framework import serializers
from pages.models import Tasks, OurApps

class TasksSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = '__all__'


class OurAppsSerializers(serializers.ModelSerializer):
    class Meta:
        model = OurApps
        fields = '__all__'