from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import generics, viewsets,permissions
from .serializer import UserSerializer
User=get_user_model()
# Create your\ views here.
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetails(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = UserSerializer
