from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls.base import reverse
from .models import Post


class BlogTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser",
            email="test@gmail.com",
            password="1234"
        )
        self.post = Post.objects.create(title="a good title",
                                        body="nice body content",
                                        author=self.user
                                        )

    def test_string_representation(self):
        post = Post(title="a sample title")
        self.assertEqual(str(post), post.title)

    def test_post_content(self):

        self.assertEqual(f"{self.post.title}", 'a good title')
        self.assertEqual(f"{self.post.author}", "testuser")

    def test_post_list_view(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "nice body content")
        self.assertTemplateUsed(response, "home.html")

    def test_post_detail_view(self):
        response = self.client.get("/post/1/")
        no_response = self.client.get("/post/321/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "a good title")
        self.assertTemplateUsed(response, "post_detail.html")
