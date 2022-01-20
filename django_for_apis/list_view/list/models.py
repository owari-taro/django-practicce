from django.db import models

class Book(models.Model):
    name=models.CharField()
    price=models.FloatField()
    created_at=models.DateTimeField(auto_now=True)

class Comment(models.Model):
    comment=models.CharField()
    created_at=models.DateTimeField(auto_now=True)
    book=models.ForeignKey(Book,on_delete=models.CASCADE) 




# Create your models here.
