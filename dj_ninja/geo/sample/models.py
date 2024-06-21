from django.contrib.gis.db import models
import json

# Create your models here.
class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Store(Base):
    polygon = models.PolygonField()
    name = models.CharField(max_length=200)
    
    @property
    def hoge(self):
        return "hogehoge"+str(self.id)
    @property
    def geojson(self)->dict:
        return json.loads(self.polygon.json)

class Book(Base):
    name=models.CharField(max_length=100)
    