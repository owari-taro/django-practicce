from django.db import models
# Create your models here.
from django.contrib.auth import get_user_model
from django.db.models.fields import related
from typing import Optional, Iterable

CommentLimit = 3


class TooManyRelationException(Exception):
    pass


class Publisher(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self) -> str:
        return self.name


class Book(models.Model):
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    is_special = models.BooleanField(default=False)
   # comments = models.ForeignKey(
    #    Comment, on_delete=models.CASCADE, related_name="book")
 #   publisher = models.ForeignKey(
  #      Publisher,  related_name="books", on_delete=models.CASCADE)

    # def save(self, force_insert: bool = False, force_update: bool = False,
    #        using: Optional[str] = False, update_fields: Optional[Iterable[str]] = None):
    #  print("save method")

    # if self.comments.count() > CommentLimit:
    #    raise TooManyException("")
    # print(type(self.comments))
    # print(self.comments.count())

   #     super(Book, self).save()

    def __str__(self):
        return self.title


class Comment(models.Model):
    comment = models.CharField(max_length=200)
    # allow one to many
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        get_user_model(),  on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.comment}.{self.author}"

    def save(self, force_insert: bool = False, force_update: bool = False,
             using: Optional[str] = False, update_fields: Optional[Iterable[str]] = None):
        print("save method")
        if self.comment=="":
            raise Exception()
        if self.book.comments.count() > CommentLimit:
            raise TooManyRelationException("")
        print(self.book.comments.count())

        super(Comment, self).save()
