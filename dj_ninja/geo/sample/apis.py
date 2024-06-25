from ninja import NinjaAPI
from sample.models import Store,Book
from sample.schema import StoreOut

api = NinjaAPI()
import time
import json
@api.get("/hello",response=list[StoreOut])
def hello(request):
    stores=Store.objects.all()
    print(request.user)
    #sessionがあれば時刻を表示
    print(request.session.get("now"))
    request.session["now"]=time.time()
    #response=[StoreOut(id=each.id,geometry=json.loads(each.polygon.json),name=each.name)for each in stores]
    return stores
from sample.schema import BookOut
@api.get("books",response=list[BookOut])
def books(request):
    book=Book.objects.all()
    return book