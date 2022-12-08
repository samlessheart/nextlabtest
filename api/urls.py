from django.urls import path 
from .views import AppList, TaskList

urlpatterns = [
    path('applist/', AppList.as_view(), ),
    path('tasklist/', TaskList.as_view(), ),
]
