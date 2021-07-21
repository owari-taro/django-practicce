from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Book, Comment, TooManyRelationException, Award
# Create your tests here.
from django.db.utils import IntegrityError
# django.db.utils.IntegrityError


class SimpleBookTest(TestCase):
    fixtures = ["fixture1.json"]
    print(fixtures)

    def setUp(self):
        #seUp is called every time when  a test method is executed
        self.comment = Comment.objects.get(pk=1)
        self.user = get_user_model().objects.create_user(
            username='hoge', email="hoge@gmail.com",
            password="test@gmail.com"
        )
        self.book = Book.objects.create(
            author="test", title="hoge_title", is_special=True)
        self.book2=Book.objects.create(author="sdf",title="fadsfa",is_special=False)
        self.comment1 = Comment.objects.create(
            comment="test", book=self.book, author=self.user)

    def test_book_has_many_awards(self):
        award1 = Award.objects.create(name="test")
        award2 = Award.objects.create(name="test2")
        self.book.awards.add(award1)
        self.book.awards.add(award2)
        self.book2.awards.add(award1)
        self.assertEqual(self.book.awards.count(), 2)
        self.assertEqual(award1.books.count(), 2)
        self.assertEqual(award2.books.count(), 1)


    def test_does_fixture_work(self):

        book = Book.objects.get(pk=1)
        print(book.comments.get())

    def test_not_null(self):
        with self.assertRaises(IntegrityError):
            self.comment.author = None
            self.comment.save()

    def test_blank_comment_is_not_allowed(self):
        with self.assertRaises(Exception):
            comment = Comment.objects.create(
                comment="", book=self.book, author=self.user
            )
            comment.save()

    def test_book_unique_constraint(self):
        with self.assertRaises(IntegrityError):
            book = Book.objects.create(
                author="test", title="hoge_title", is_special=False)
            book.save()

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
