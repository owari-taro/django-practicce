from rest_framework import serializers
from books.models import Book


class BookSeriazlizer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'author', 'subtitle', 'isbn')
