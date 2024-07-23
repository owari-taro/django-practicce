from ninja import NinjaAPI
from sample.models import Store, Book
from sample.schema import StoreOut
from ninja_extra import NinjaExtraAPI, api_controller, http_get
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from ninja_extra.exceptions import APIException

api = NinjaAPI()
import time
import json
from ninja.security import django_auth
from ninja import Schema

class CustomException(APIException):
    extra=""
    def __init__(self,detail,code,extra=""):
        self.extra=extra
        super().__init__(detail,code)



class Error(Schema):
    detail:str

api = NinjaExtraAPI()


def ip_whitelist(request):
    return True

from ninja_extra.pagination import (
    paginate, PageNumberPaginationExtra

)
from sample.pagination import PaginationExtra,PaginatedResponseSchema

@api_controller("store/", tags=["Store"])  # auth=django_auth)
class StoreAPI:

    @http_get("", response=PaginatedResponseSchema[StoreOut])
    @paginate(PaginationExtra)
    def get(self, request):
        stores = Store.objects.all()
        #print(request.user)
        # sessionがあれば時刻を表示
        #print(request.session.get("now"))
        #request.session["now"] = time.time()
        # response=[StoreOut(id=each.id,geometry=json.loads(each.polygon.json),name=each.name)for each in stores]
        return stores




    @http_get("/{store_id}", response={200:StoreOut,500:Error})
    def get_by_id(self, request, store_id: int):
        try:
            store = get_object_or_404(Store, id=store_id)
        except Exception:
            raise CustomException(code=500,detail="waaaaa",extra="extraaa")
        print(request.user)
        # sessionがあれば時刻を表示
        print(request.session.get("now"))
        #request.session["now"] = time.time()
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
