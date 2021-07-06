from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope
from rest_framework import generics, permissions, serializers
from django.urls import path, include
from django.contrib.auth.models import Group
from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Element
User = get_user_model()
admin.autodiscover()


# first we define the serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', "first_name", "last_name")

class ElementSerializer(serializers.ModelSerializer):
    class Meta:
        model=Element
        fields=("name","comment","old",)

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ("name", )

# Create the API views
