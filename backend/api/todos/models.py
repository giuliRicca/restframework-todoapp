from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Task(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=150, blank=True, default='')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    completed = models.BooleanField(blank=True)

    class Meta:
        ordering = ['created']
