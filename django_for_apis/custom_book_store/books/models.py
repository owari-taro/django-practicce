from django.db import models

# Create your models here.
from django.contrib.auth import get_user_model
from django.db.models.fields import related
from typing import Optional, Iterable
from django.utils import timezone
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

    def __str__(self):
        return self.title

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["author", "title"],
                name="author_title_unique"
            ),
        ]


class Comment(models.Model):
    comment = models.CharField(max_length=200)
    # allow one to man
    book = models.ForeignKey(Book, null=True, on_delete=models.CASCADE,
                             related_name="comments")
    author = models.ForeignKey(
        get_user_model(),  on_delete=models.CASCADE)
    created_at = models.DateTimeField(null=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=True, auto_now=True)

    def __str__(self):
        return f"{self.comment}.{self.author}"

    def save(self, force_insert: bool = False, force_update: bool = False,
             using: Optional[str] = False, update_fields: Optional[Iterable[str]] = None):
       # print("save method")
        if len(self.comment) == 0:
            raise Exception("empty string isnt allowed")
        if self.book.comments.count() > CommentLimit:
            raise TooManyRelationException("")

        super(Comment, self).save()


class Award(models.Model):
    # example model for testing manytomany field
    name = models.CharField(max_length=250)
    books = models.ManyToManyField(Book, null=True,related_name="awards"
    )
    created_at = models.DateTimeField(null=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=True, auto_now=True)

    def __str__(self):
        return self.name