from django.test import TestCase
from django.urls import reverse
from .models import Post
# Create your tests here.


class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(text="just a test")

    def test_text_content(self):
        post = Post.objects.get(id=1)
        expected = f"{post.text}"
        self.assertEqual(expected, "just a test")


class HomePageviewTest(TestCase):
    def setUp(self):
        Post.objects.create(text="this is another test")

    def test_view_url_exists(self):
        resp = self.client.get("/")
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse("home"))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_templatea(self):
        resp = self.client.get(reverse("home"))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, "home.html")
