from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class TaskModel(models.Model):
    PRIORITY_CHOICES = [
        ("LOW","Low"),
        ("MEDIUM","Medium"),
        ("HIGH","High")
    ]
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name="tasks")
    title = models.CharField(max_length=256)
    priority = models.CharField(max_length=10,choices=PRIORITY_CHOICES,default="LOW")
    created_at = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)
    is_archived = models.BooleanField(default=False)
    should_notify = models.BooleanField(default=False)

    def __str__(self):
        return self.title

