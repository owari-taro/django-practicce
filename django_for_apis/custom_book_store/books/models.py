from django.db import models
# Create your models here.
from django.contrib.auth import get_user_model
from django.db.models.fields import related
from typing import Optional, Iterable
CommentLimit = 1000


class TooManyException(Exception):
    pass


class Book(models.Model):
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    is_special = models.BooleanField(default=False)

    def save(self, force_insert: bool = False, force_update: bool = False,
             using: Optional[str] = False, update_fields: Optional[Iterable[str]] = None):
        print("save method")

        if self.comments.count() > CommentLimit:
            raise TooManyException("")
        print(type(self.comments))
        print(self.comments.count())

        super(Book, self).save()

    def __str__(self):
        return self.title


class Comment(models.Model):
    comment = models.CharField(max_length=200)
    # allow one to many
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
