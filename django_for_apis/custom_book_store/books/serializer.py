from django.db.models import fields
from rest_framework import serializers
from .models import Book, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class BookSerializer(serializers.ModelSerializer):

    comments = serializers.StringRelatedField(many=True)
    # comments = CommentSerializer(fields=("comment",),ma)

    class Meta:
        model = Book
        fields = ["is_special", "author", "title", "comments"]
