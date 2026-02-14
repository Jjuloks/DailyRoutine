from django.db import models

# Create your models here.

class Task(models.Model):
    STATUS_CHOICES = [
        ("todo", "To do"),
        ("done", "Done"),
    ]

    title = models.CharField(max_length=25)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=5,choices=STATUS_CHOICES,default="todo")
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField(null= True, blank=True)
    completed_at = models.DateField(null= True, blank=True)

    def __str__(self):
                return f"{self.title}, {self.description}"     

