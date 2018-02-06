from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import CreateBookForm
from .models import Book, Publisher, Author, Category


def index(request):

    books = Book.objects.all()

    return render(request, 'index.html', {'books': books})


def create_book(request):
    if request.method == 'POST':
        form = CreateBookForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data

            publisher = Publisher.objects.create(name=cleaned_data['publisher'])
            # actually I don't know what can I do with authors with names like Gabriel Garcia Markes or Rainer Maria Rilke
            # I tried to use surname=cleaned_data['author'].split(" ")[1:] but it added a list to db
            author = Author.objects.create(name=cleaned_data['author'].split(" ")[0],
                                           surname=cleaned_data['author'].split(" ")[1])
            category = Category.objects.create(name=cleaned_data['category'])

            book = Book.objects.create(title=cleaned_data['title'],
                                       publisher=publisher,
                                       publication_date=cleaned_data['publication_date'])

            book.author.add(author)
            book.category.add(category)
            return HttpResponseRedirect('create_book')
    else:
        form = CreateBookForm()
    return render(request, 'create_book.html', {'form': form})
