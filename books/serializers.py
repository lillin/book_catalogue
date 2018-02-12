from rest_framework.serializers import ModelSerializer, CharField
from .models import Book, Author, Category


class CategorySerializer(ModelSerializer):
    """
    Serializer for Category model
    """

    name = CharField(source='category__name')

    class Meta:
        model = Category
        fields = {'name'}


class AuthorSerializer(ModelSerializer):
    """
    Serializer for Author model
    """

    name = CharField(source='author__name')
    surname = CharField(source='author__surname')

    class Meta:
        model = Author
        fields = {'name', 'surname'}


class BookSerializer(ModelSerializer):
    """
    Serializer for Book model
    """

    author = AuthorSerializer(read_only=True, many=True)
    category = CategorySerializer(read_only=True, many=True)
    publisher = CharField(source='publisher.name')

    class Meta:
        model = Book
        fields = {'title', 'author', 'publisher', 'category', 'publication_date'}
