from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view

from .forms import CreateBookForm
from .models import Book, Publisher, Author, Category
from .serializers import BookSerializer


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


@api_view(['GET'])
def get_books(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    print(serializer)
    return JsonResponse(serializer.data, safe=False)


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
