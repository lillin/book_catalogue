from rest_framework.serializers import ModelSerializer, CharField
from .models import Book, Author, Category


class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = ['name']


class AuthorSerializer(ModelSerializer):

    class Meta:
        model = Author
        fields = ['name', 'surname']


class BookSerializer(ModelSerializer):

    author = AuthorSerializer(read_only=True, many=True)
    category = CategorySerializer(read_only=True, many=True)
    publisher = CharField(source='publisher.name')

    class Meta:
        model = Book
        fields = ['title', 'author', 'publisher', 'category', 'publication_date']
