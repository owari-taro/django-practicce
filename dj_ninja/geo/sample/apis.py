from ninja import NinjaAPI
from sample.models import Store
from sample.schema import StoreOut
api = NinjaAPI()
import json
@api.get("/hello",response=list[StoreOut])
def hello(request):
    stores=Store.objects.all()
    #response=[StoreOut(id=each.id,geometry=json.loads(each.polygon.json),name=each.name)for each in stores]
    return stores