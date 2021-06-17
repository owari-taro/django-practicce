from django.test import TestCase
from django.contrib.auth import get_user, get_user_model
# Create yosur tests here.
from django.urls import reverse, resolve
from .forms import CustomUserCreationForm
from .views import SignupPageView


class CusotmUserTest(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="will", email="will@email.com", password='testpass123')

        self.assertEqual(user.username, "will")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_super_user(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username="superadmin",
            email='superadmin@emial.com',
            password='testpass123'
        )

        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)


class SignupPageTests(TestCase):
    def setUp(self):
        url = reverse('signup')
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'signup.html')
        self.assertContains(self.response, 'signup')
       # self.assertNotContains(self.reponse,'his there i should not be on the page')

    def test_sinup_form(self):
        form = self.reponse.context.get('form')
        self.assertIsInstance(form, CustomUserCreationForm)
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_sinup_view(self):
        view = resolve('/accounts/signup/')
        self.assertEqual(view.func.__name__,
                         SignupPageView.as_view().__name__)
