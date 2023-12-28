from .views import *
from django.urls import path, re_path

urlpatterns = [
    path(r'notes/<int:pk>/', NoteDetail.as_view()),
    path(r'notes/', NoteList.as_view()),


]