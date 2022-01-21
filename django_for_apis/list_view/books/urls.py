from django.urls import path
from .views import CommentListrView


urlpatterns=[
    path("",CommentListrView.as_view())
]