from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
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

            publisher, created = Publisher.objects.get_or_create(name=cleaned_data['publisher'])

            author, created = Author.objects.get_or_create(name=cleaned_data['author'].split(" ")[0],
                                                           surname=" ".join(cleaned_data['author'].split(" ")[1:]))
            category, created = Category.objects.get_or_create(name=cleaned_data['category'])

            book = Book.objects.create(title=cleaned_data['title'],
                                       publisher=publisher,
                                       publication_date=cleaned_data['publication_date'])

            book.author.add(author)
            book.category.add(category)
            return HttpResponseRedirect('create_book')
    else:
        form = CreateBookForm()
    return render(request, 'create_book.html', {'form': form})

# TODO: make 1 API URL which returns only data about books (JSON need)


def get_books(request):
    books = Book.objects.all()
    books_list = []
    for book in books:
        books_list.append({'title': book.title,
                           'author': ",".join([author.name + ' ' + author.surname for author in book.author.all()]),
                           'publisher': book.publisher.name,
                           'category': ",".join([category.name for category in book.category.all()]),
                           'publication date': book.publication_date})
    return JsonResponse(books_list, safe=False)
