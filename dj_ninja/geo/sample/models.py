from django.contrib.gis.db import models
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.conf import settings
from django.core.exceptions import ValidationError
from shapely import from_wkt


# Create your models here.
class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True




class Store(Base):
    geometry = models.PolygonField(null=True, blank=True)
    name = models.CharField(max_length=200, unique=True)

    @property
    def geojson(self) -> dict:
        return json.loads(self.geometry.json)

    def clean(self):
        # check geometry
        if self.geometry and self.geometry.valid == False:
            raise ValidationError(f"invalid geometry")
        if (
            self.geometry
            and settings.JP_EXTENT.contains(from_wkt(self.geometry.wkt)) == False
        ):
            raise ValidationError(f"polygon must be within japan")

    def save(
        self, force_insert=False, force_update=False, using=False, update_fields=None
    ):
        # using only lower letters  to avoid dulicate inserts like "comment" and "Comment"
        # self.permission = self.permission.lower()
        self.full_clean()
        super(Store, self).save()


class Author(Base):
    name = models.CharField(max_length=100, unique=True)
    pen_name = models.CharField(max_length=100, unique=True)


class Book(Base):
    name = models.CharField(max_length=100)
    meta = models.JSONField(null=True, encoder=DjangoJSONEncoder)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)

    @property
    def author_name(self):
        return self.author.name
