from django.shortcuts import render
from apps.books.models import Book
from django.views.generic import ListView

# Create your views here.
class BookListView(ListView):
    model = Book
    template_name = "books/index.html"