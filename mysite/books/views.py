from django.shortcuts import render

from .models import Book


def index(request):

    books = Book.objects.all()
    #for book in books:
     #   book.author = book.author.all()

    return render(request, 'index.html', {'books': books})

