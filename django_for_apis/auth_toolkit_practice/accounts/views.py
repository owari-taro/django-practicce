from .models import Element
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope
from django.shortcuts import render
from django.contrib.auth import get_user_model
from oauth2_provider.contrib.rest_framework.permissions import TokenHasScope,TokenHasResourceScope
from oauth2_provider.contrib.rest_framework import   OAuth2Authentication
from oauth2_provider.models import *
from rest_framework import generics, serializers, viewsets, permissions
from .serializer import UserSerializer, ElementSerializer
User = get_user_model()
# Create your\ views here.


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = UserSerializer

from django.contrib.auth.models import Group
from rest_framework import mixins, views
from rest_framework.generics import GenericAPIView
from .serializer import GroupSerializer

class GroupList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    required_scopes = ['adult']
    queryset = Group.objects.all()
    serializer_class = GroupSerializer



class ElementList(generics.ListCreateAPIView):
  #  authentication_classes = [OAuth2Authentication]
    permission_classes = [permissions.IsAuthenticated,TokenHasScope]
    required_scopes = ["adult"]
    serializer_class = ElementSerializer
    queryset = Element.objects.all()


class UserList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetails(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = UserSerializer
