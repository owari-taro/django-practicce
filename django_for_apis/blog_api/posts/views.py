from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Post
from .serializer import PostSerializer, UserSerializer
# Create your views here.
from .permissions import IsAuthorReadOnly
from django.contrib.auth import get_user, get_user_model
from rest_framework import viewsets


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
