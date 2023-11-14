from django.urls import path
from snippets import views

urlpatterns=[
    path("",views.top,name="top"),
    path("upload/",views.upload,name="upload"),
    path("feedback/",views.upload_feedback,name="feedback"),
    path("search/",views.search,name="search"),

    path("<int:snippet_id>/",views.snippet_detail,name="snippet_detail"),
    path("<int:snippet_id>/edit/",views.snippet_edit,name="snippet_edit")
]