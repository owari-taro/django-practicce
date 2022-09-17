import pytest
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.mark.django_db
def test_create_user():
    user = User.objects.create_user(username="will", email="will@email.com", password="testpass123")
    assert user.username == "will"
