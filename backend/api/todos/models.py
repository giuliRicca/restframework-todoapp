from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Task(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False, blank=True, null=True)
    objects = models.Manager()

    def __srt__(self):
        return self.title

    class Meta:
        ordering = ['created']
