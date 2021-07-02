from rest_framework import serializers
from .models import Album


class AlbumSerializer(serializers.ModelSerializer):
 #   tracks = serializers.StringRelatedField(many=True)
    tracks = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Album
        fields = ['album_name', 'artist', 'tracks']
