from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

# Create your views here.


def index(request):
    book_all = Book.objects.all()
    return render(request, 'index.html', {'books': book_all})


def about(request):
    return render(request, 'about-us.html')
