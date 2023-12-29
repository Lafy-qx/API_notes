from django.db import models
from datetime import datetime


class Note (models.Model):
    title = models.CharField(max_length=32, blank=False)
    text = models.TextField(blank=False)
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name='owner', on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title
