from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *

class NoteSerealizer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Note
        fields = '__all__'

class UserSerealizer(serializers.ModelSerializer):
    notes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'notes', ]
