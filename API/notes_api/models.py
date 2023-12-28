from django.db import models
from datetime import datetime


class Note (models.Model):
    title = models.CharField(max_length=32, blank=False)
    text = models.TextField(blank=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
