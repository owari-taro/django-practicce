from enum import auto
from pyexpat import model
from django.db import models

class Book(models.Model):
    title=models.CharField(max_length=300)
    author=models.CharField(max_length=300)
    isbn=models.CharField(max_length=13)
    created_at=models.DateTimeField(auto_created=True)
    def __str__(self):
        return f"{self.title}:{self.isbn}"

class Comment(models.Model):
    
    comment=models.CharField(max_length=300)
    book=models.ForeignKey(Book,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_created=True)
