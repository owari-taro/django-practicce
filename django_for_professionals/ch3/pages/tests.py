# from django.test import TestCase
import pytest

# Create your tests here.
from django.urls import reverse


def test_homepage_status_code(client):
    res = client.get("/")
    assert res.status_code == 200


def test_homepage_url_name(client):
    res = client.get(reverse("home"))
    assert res.status_code == 200
