from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Book, Review
# reate your tests here.


class BookTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser",
            email="test@gmail.com",
            password="test1234"
        )
        self.book = Book.objects.create(
            title="harry", author="ore", price='25')
        self.review = Review.objects.create(
            book=self.book, author=self.user, review="wow")

    def test_book_listing(self):
        self.assertEqual(f'{self.book.title}', 'harry')
        self.assertEqual(f'{self.book.author}', 'ore')

    def test_book_list_view(self):
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'harry')
        self.assertTemplateUsed(response, 'books/book_list.html')

    def test_book_detail_view(self):
        response = self.client.get(self.book.get_absolute_url())
        no_response = self.client.get('/books/12367674/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'harry')
        self.assertContains(response, 'wow')
        self.assertTemplateUsed(response, 'books/book_detail.html')
