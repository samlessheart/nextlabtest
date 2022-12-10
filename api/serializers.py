from rest_framework import serializers
from pages.models import Tasks, OurApps
from account.models import Profile

class TasksSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = '__all__'
        read_only_fields = ['user']


class OurAppsSerializers(serializers.ModelSerializer):
    class Meta:
        model = OurApps
        fields = '__all__'


class ProfileSerializers(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    class Meta:
        model = Profile
        # fields = '['points', 'user']'
        fields = '__all__'