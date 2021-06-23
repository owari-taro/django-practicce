from typing import List
from django.shortcuts import render
from django.views.generic import ListView, DetailView

# Create your views here.
from .models import Book
from django.contrib.auth.mixins import LoginRequiredMixin

class BookListView(LoginRequiredMixin,ListView):
    model = Book
    template_name = "books/book_list.html"
    login_url="account_login"

class BookDetailView(LoginRequiredMixin,DetailView):
    model = Book
    template_name = 'books/book_detail.html'
    context_object_name = "book"
    login_url="account_login"