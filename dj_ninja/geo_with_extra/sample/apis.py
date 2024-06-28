from ninja import NinjaAPI
from sample.models import Store, Book
from sample.schema import StoreOut
from ninja_extra import NinjaExtraAPI, api_controller, http_get
from django.shortcuts import get_object_or_404

api = NinjaAPI()
import time
import json
from ninja.security import django_auth

api = NinjaExtraAPI()


def ip_whitelist(request):
    return True


@api_controller("/store", tags=["Store"])  # auth=django_auth)
class StoreAPI:
    @http_get("", response=list[StoreOut])
    def get(self, request):

        stores = Store.objects.all()
        print(request.user)
        # sessionがあれば時刻を表示
        print(request.session.get("now"))
        request.session["now"] = time.time()
        # response=[StoreOut(id=each.id,geometry=json.loads(each.polygon.json),name=each.name)for each in stores]
        return stores

    @http_get("/{store_id}", response=StoreOut)
    def get_by_id(self, request, store_id: int):

        store = get_object_or_404(Store, id=store_id)
        print(request.user)
        # sessionがあれば時刻を表示
        print(request.session.get("now"))
        request.session["now"] = time.time()
        # response=[StoreOut(id=each.id,geometry=json.loads(each.polygon.json),name=each.name)for each in stores]
        return store


api.register_controllers(StoreAPI)

'''
@api_controller('/', tags=['Math'])
class MathAPI:

    @http_get('/subtract',)
    def subtract(self, a: int, b: int):
        """Subtracts a from b"""
        return {"result": a - b}

    @http_get('/divide',)
    def divide(self, a: int, b: int):
        """Divides a by b"""
        return {"result": a / b}

    @http_get('/multiple',)
    def multiple(self, a: int, b: int):
        """Multiples a with b"""
        return {"result": a * b}

api.register_controllers(
    MathAPI
)
'''
"""
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
"""
