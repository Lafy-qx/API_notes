from django.contrib import admin
from .models import *


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'text',  "created")
    search_fields = ['title']

    

