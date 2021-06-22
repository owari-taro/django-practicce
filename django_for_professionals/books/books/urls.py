from django.urls import path
from django.urls.resolvers import URLPattern
from .views import BookListView, BookDetailView

urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    path('<uuid:pk>/', BookDetailView.as_view(), name="book_detail")

]
