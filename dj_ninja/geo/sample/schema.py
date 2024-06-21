from ninja import Schema, ModelSchema
from sample.models import Store,Book
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

class BookOut(ModelSchema):
    class Meta:
        model=Book
        fields="__all__"