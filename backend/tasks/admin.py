from django.contrib import admin
from .models import Task

# Register your models here.

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description","status","deadline","created_at", "duration_time", "completed_at")
    list_filter = ("status","deadline")
    search_fields = ("title", "description")