from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import AboutPageView, HomePageView
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


class AboutPageTests(SimpleTestCase):
    def setUp(self):
        url = reverse('about')
        self.response = self.client.get(url)

    def test_aboutpage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_aboutpage_template(self):
        self.assertTemplateUsed(self.response, 'about.html')

    def test_aboutpage_contains_correct_html(self):
        self.assertContains(self.response, 'about page')

    def test_aboutpage_doesnot_contain(self):
        self.assertNotContains(
            self.response, 'hi there i should not be on the page')

    def test_aboupage_url_resolve_aboutpageview(self):
        view = resolve('/about/')
        self.assertEqual(view.func.__name__,
                         AboutPageView.as_view().__name__)
