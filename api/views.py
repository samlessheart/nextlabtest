from django.shortcuts import render
from .serializers import OurAppsSerializers, TasksSerializers
from rest_framework import generics, viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from pages.models import Tasks, OurApps
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

# Create your views here.



# list all the app or create a new app 
class AppList(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        apps = OurApps.objects.all()
        serializer = OurAppsSerializers(apps, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = OurAppsSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






