from .serializers import *
from .models import *
from rest_framework.permissions import IsAuthenticated

from rest_framework import generics


class NoteList(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerealizer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super(NoteList,self).get_queryset().order_by('-id')

        sort = self.request.GET.get('sort')
        author = self.request.GET.get('author')

        if author:
            queryset = queryset.filter(owner=author)

        if sort == 'toNew':
            queryset = queryset.order_by('created')

        if sort == 'toOld':
            queryset = queryset.order_by('-created')

        return queryset


class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerealizer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerealizer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerealizer
