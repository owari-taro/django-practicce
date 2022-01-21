from django.shortcuts import render
from .serializer import CommentSerializer
from .models import Comment
from rest_framework import generics
# Create your views here.

class CommentListrView(generics.ListAPIView):
    queryset=Comment.objects.all()
    serializer_class=CommentSerializer


class CommentCusltomView(generics.ListAPIView):
    #queryset=Comment.objects.all()
    serializer_class=CommentSerializer
    def get_queryset(self):
        """
        [summary]

        Returns:
            [type]: [description]
        """        
        book_id = self.kwargs['book_id']
        return Comment.objects.filter(book_id=book_id)