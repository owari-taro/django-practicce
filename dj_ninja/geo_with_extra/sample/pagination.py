import logging
from collections import OrderedDict
from typing import (
    Any,
    List,
    Optional,
    Type,
    Union,
)

from django.core.paginator import InvalidPage, Page, Paginator
from django.db.models import QuerySet
from django.http import HttpRequest
from ninja import Schema
from ninja.pagination import PaginationBase
from ninja.types import DictStrAny
from pydantic import Field

from ninja_extra.conf import settings
from ninja_extra.exceptions import NotFound
from ninja_extra.schemas import PaginatedResponseSchema
from ninja_extra.urls import remove_query_param, replace_query_param
from ninja_extra.schemas.response import Url
from urllib.parse import urljoin, urlparse

logger = logging.getLogger()
from typing import Generic,TypeVar

T = TypeVar("T")

class CustomPaginatedResponseSchema(Schema):
    count: int
    next: Optional[Url]
    previous: Optional[Url]
    data: List[Any]#=Field(alias="results")



class PaginatedResponseSchema(CustomPaginatedResponseSchema, Generic[T]):
    data: List[T]



class PaginationExtra(PaginationBase):
    class Input(Schema):
        limit: int = Field(100,gt=0, lt=3000)
        offset: int = Field(0, ge=0)
    #class Output(Schema):
    #    data:List[Any]
    page_query_param = "page"
    page_size_query_param = "page_size"
    
    max_limit = 1000
    def paginate_queryset(
        self,
        queryset: QuerySet,
        pagination: Input,
        request: Optional[HttpRequest] = None,
        **params: DictStrAny,
    ) -> Any:
        assert request, "request is required"
        #limit = pagination.limit
        #offet = pagination.offset
        # current_page_number = pagination.page
        # paginator = self.paginator_class(queryset, pagination.page_size)
        try:
            #query_param=pagination
            url = request.build_absolute_uri()
            #query_parameterを削除
            url=urljoin(url, urlparse(url).path) 
            # page: Page = paginator.page(current_page_number)
            print(url)
            return self.get_paginated_response(
                base_url=url,
                queryset=queryset,
                limit=pagination.limit,
                offset=pagination.offset
            )
        except InvalidPage as exc:  # pragma: no cover
            msg = "invalid"
            raise NotFound(msg) from exc

    def get_paginated_response(
        self, *, base_url: str, queryset: QuerySet, limit,offset
    ) -> DictStrAny:
        return OrderedDict(
            [
                ("count", queryset.count()),
                ("next", self.get_next_link(base_url,queryset.count(),limit,offset)),
                ("previous", self.get_previous_link(base_url,queryset.count(),limit,offset)),
                ("data", list(queryset.all()[offset : offset + limit])),
            ]
        )

    def get_previous_link(self, base_url: str,count:int, limit: str, offset: str) -> Optional[str]:
        if offset <= 0:
            return None
        if offset>=count:#offsetがデータ全数より多いとき
            offset=count-limit
            return self.create_url(base_url,offset,limit)
        offset = max(0, offset - limit)
        return self.create_url(base_url, offset, limit)

    def get_next_link(self, base_url: str, count: int, limit: int, offset: int):
        if offset+limit >= count:
            return None
        offset = min(offset + limit, count)
        return self.create_url(base_url, offset, limit)

    def create_url(self, base_url, offset: int, limit: int):
        return f"{base_url}?{offset=}&{limit=}"

    @classmethod
    def get_response_schema(
        cls, response_schema: Union[Type[Schema], Type[Any]]
    ) -> Any:
        return PaginatedResponseSchema[response_schema]  # type: ignore[valid-type]

    #def get_next_link(self, url: str, page: Page) -> Optional[str]:
     #   if not page.has_next():
      #      return None
      #  page_number = page.next_page_number()
      #  return replace_query_param(url, self.page_query_param, page_number)

   # def get_previous_link(self, url: str, page: Page) -> Optional[str]:
    #    if not page.has_previous():
     #       return None
      #  page_number = page.previous_page_number()
       # if page_number == 1:
        #    return remove_query_param(url, self.page_query_param)
        #return replace_query_param(url, self.page_query_param, page_number)
