from rest_framework import serializers
from .models import *

class NoteSerealizer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'
