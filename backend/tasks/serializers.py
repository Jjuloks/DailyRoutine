from rest_framework import serializers
from .models import Task

from django.utils import timezone
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"


    def update(self, instance, validated_data):
        old_status = instance.status
        new_status= validated_data.get("status", old_status)


        if old_status !="done" and new_status == "done":
            validated_data["completed_at"] = timezone.now()
        
        return super().update(instance, validated_data)
  


