from django.db import models
from django.conf import settings


# Create your models here.
class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract=True

class Snippet(Base):
    title = models.CharField("title", max_length=128)
    code = models.TextField("code", blank=True)
    description = models.TextField("description", blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
