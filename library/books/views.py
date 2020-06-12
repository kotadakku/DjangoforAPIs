from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.views.generic import ListView
from .models import Book


def index(self):
    return HttpResponse("Hello World")

class BookListView(ListView):
    model = Book
    template_name = 'books/books_list.html'