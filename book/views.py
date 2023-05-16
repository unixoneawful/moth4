from django.http import HttpResponse
from django.shortcuts import render
from . import models

def hello_view(request):
    return HttpResponse('My first homework moth 4')

def book_view(request):
    book = models.Book.objects.all()
    return render(request, 'book.html', {'book': book})