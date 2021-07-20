from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Book, Comment, TooManyRelationException
# Create your tests here.


class SimpleBookTest(TestCase):
    fixtures=["fixture1.json"]
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='hoge', email="hoge@gmail.com",
            password="test@gmail.com"
        )
        self.book = Book.objects.create(
            author="test", title="hoge_title", is_special=True)
        self.comment1 = Comment.objects.create(
            comment="test", book=self.book, author=self.user)
    def test_does_fixture_work(self):
        book=Book.objects.get(pk=1)
        print(book.comments.get())

    def test_blank_comment_is_not_allowed(self):
        with self.assertRaises(Exception):
            comment=Comment.objects.create(
                comment="",book=self.book,author=self.user
            )
            comment.save()

    def test_many_comment(self):
        pass
        comment2 = Comment.objects.create(
            comment="test321", book=self.book, author=self.user)
        comment2.save()
        comment3 = Comment.objects.create(
            comment="test321", book=self.book, author=self.user)
        comment3.save()
        with self.assertRaises(TooManyRelationException):
            comment4 = Comment.objects.create(
                comment="test321", book=self.book, author=self.user)
            comment4.save()
