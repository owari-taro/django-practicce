from django.contrib.gis.db import models
import json
from django.core.serializers.json import DjangoJSONEncoder


# Create your models here.
class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Store(Base):
    polygon = models.PolygonField(null=True)
    name = models.CharField(max_length=200)

    @property
    def geojson(self) -> dict:
        return json.loads(self.polygon.json)


class Author(Base):
    name = models.CharField(max_length=100, unique=True)
    pen_name = models.CharField(max_length=100, unique=True)


class Book(Base):
    name = models.CharField(max_length=100)
    meta = models.JSONField(null=True, encoder=DjangoJSONEncoder)
    author = models.ForeignKey(Author,on_delete=models.CASCADE,null=True)
    @property
    def author_name(self):
        return self.author.name