from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Post
from .serializer import PostSerializer
# Create your views here.
from .permissions import IsAuthorReadOnly

 
class PostList(generics.ListCreateAPIView):
    #permission_classes = (permissions.IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
 

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
