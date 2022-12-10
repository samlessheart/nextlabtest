from django.urls import path 
from .views import AppList, TaskList, Profiledetail

urlpatterns = [
    path('applist/', AppList.as_view(), ),
    path('tasklist/', TaskList.as_view(), ),
    path('profile/', Profiledetail.as_view(), ),
]
