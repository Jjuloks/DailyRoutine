from django.shortcuts import render
from .models import Task
from .serializers import TaskSerializer
from django.utils import timezone
from datetime import date, datetime,  timedelta
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend



class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    
    serializer_class = TaskSerializer

    
    @action(detail=False, methods=["get"])
    def today(self, request):
        today_date = date.today()
        queryset = Task.objects.filter(deadline = today_date)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=["get"])
    def tommorow(self, request):
        today_date = date.today()
        tommorrow_date =  today_date + timedelta(days=1)
        queryset = Task.objects.filter(deadline = tommorrow_date)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


    def get_queryset(self):
        queryset = Task.objects.all()
        fromDate = self.request.query_params.get("from")
        toDate = self.request.query_params.get("to")
        deadline__range = [fromDate, toDate]

        if fromDate is not None and toDate is not None:
            queryset = queryset.filter(deadline__range=[fromDate, toDate])

        return queryset







# Create your views here.
