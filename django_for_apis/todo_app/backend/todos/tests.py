from django.test import TestCase
from .models import Todo
# Create your tests here.


class TodoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Todo.objects.create(title="first!", body="body!")

    def test_title_content(self):
        todo = Todo.objects.get(id=1)
        actual = f"{todo.title}"
        self.assertSetEqual(actual, "first!")
