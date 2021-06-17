from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import HomePageView
# Create your tests here.


class HomePageTest(SimpleTestCase):
    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    def test_homepage_status_code(self):
        #response = self.client.get('/')
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_url_name(self):
        #response = self.client.get(reverse('home'))
        self.assertEqual(self.response.status_code, 200)

    def test_home_page_template(self):
        # "response=self.client.get('/')
        self.assertTemplateUsed(self.response, 'home.html')

    def test_contain_correct_html(self):
        # response=self.client.get('/')
        self.assertContains(self.response, 'homepage')

    def test_doesnt_contain_incorrect_html(self):
       # response=self.client.get('/')
        self.assertNotContains(self.response, "hello world")

    def test_homepage_url_resolve_homepageview(self):
        view = resolve('/')
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)
