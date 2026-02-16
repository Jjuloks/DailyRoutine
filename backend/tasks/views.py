from django.shortcuts import render
from .models import Task
from .serializers import TaskSerializer
from django.utils import timezone
from datetime import date
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action



class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    
    serializer_class = TaskSerializer

    
    @action(detail=False, methods=["get"])
    def today(self, request):
        today_date = date.today()
        queryset = Task.objects.filter(deadline = today_date)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    





# Create your views here.
