from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    MALE = 'M'
    FEMALE = 'F'
    age = models.IntegerField(null=True, blank=True)
    GENDER_CHOICES = ((MALE, 'Male'), (FEMALE, 'Female'))
    gender = models.CharField(max_length=2,
                              choices=GENDER_CHOICES, default=MALE)
    is_alive = models.BooleanField(default=True)


class Element(models.Model):
    name = models.CharField(max_length=10)
    old = models.IntegerField(null=True, blank=True)
    comment=models.TextField(max_length=300)