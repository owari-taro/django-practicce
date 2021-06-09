#from django.db.models import query
from rest_framework import generics
from books.models import Book
from .serializer import BookSeriazlizer
# Create your views here.


class BookAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSeriazlizer
