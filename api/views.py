from django.shortcuts import render
from .serializers import OurAppsSerializers, TasksSerializers, ProfileSerializers
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.parsers import MultiPartParser, FormParser
from pages.models import Tasks, OurApps
from account.models import Profile
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from .permissions import IsStaffOrReadOnly
# Create your views here.



# list all the apps that can be completed and create a new app 
class AppList(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated, IsStaffOrReadOnly]
    parser_classes = [MultiPartParser, FormParser]

    def get(self, request, format = None):
        if request.user.is_staff:
            apps = OurApps.objects.all()
        else:
            apps = OurApps.objects.exclude(tasks__user = request.user)
        serializer = OurAppsSerializers(apps, many=True)

        return Response(serializer.data)

    def post(self, request,):
        serializer = OurAppsSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# list the task that has been completed by user and create task 
class TaskList(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def get(self, request, ):
        tasks = Tasks.objects.filter(user= request.user)
        serializer = TasksSerializers(tasks, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = TasksSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class Profiledetail(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        prof = Profile.objects.get(id = request.user.profile.id)
        serializer = ProfileSerializers(prof)
        return Response(serializer.data)