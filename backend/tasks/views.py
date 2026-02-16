from django.shortcuts import render
from .models import Task
from rest_framework import viewsets
from .serializers import TaskSerializer
from django.utils import timezone


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    
    serializer_class = TaskSerializer





# Create your views here.
