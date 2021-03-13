from django.db import models
from django.contrib.auth.models import AbsractUser




# Create your models here.
class CustomUser(AbstractUser):
    age= models.PositiveIntegerFiled(null=True,blan=True)