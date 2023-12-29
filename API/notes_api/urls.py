from .views import *
from django.urls import path, re_path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path(r'notes/<int:pk>/', NoteDetail.as_view()),
    path(r'notes/', NoteList.as_view()),
    path(r'users/<int:pk>/', UserDetail.as_view()),
    path(r'users/', UserList.as_view()),
    path(r'token-auth/', obtain_auth_token),
    

]
