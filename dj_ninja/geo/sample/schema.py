from ninja import Schema, ModelSchema
from sample.models import Store,Book,Author
from typing import Optional


class Geojson(Schema):
    type:str
    coordinates:list
class StoreOut(ModelSchema):
    # name:str
    # polygon:dict
    #geometry:dict
    geojson:Geojson
    class Meta:
        model = Store
        fields = ["id","name"]
    #@property
    #def hoge(self)->str:
    #    return "hoge"#+self.id
from typing import Any

##関連github
##https://github.com/vitalik/django-ninja/issues/291
class BookOut(Schema):
    name:str
    #bookモデルのprpertyで設定する
    author_name:str
    meta:Optional[Any]=None
