# from django.test import TestCase
import pytest

# Create your tests here.
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed


@pytest.fixture(scope="function")
def response(client):
    # clientはfunction scope
    return client.get(reverse("home"))


def test_homepage_status_code(response):
    # res = client.get("/")
    print(response)
    assert response.status_code == 200


def test_homepage_url_name(response):
    # res = client.get(reverse("home"))
    assert response.status_code == 200
