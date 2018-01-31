from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Author(models.Model):
    name = models.CharField(max_length=40)
    surname = models.CharField(max_length=40)
    # what we need to do with the author's books?
    # or if rel-ships of Author-Book were defined on the Book model,
    # we wouldn't need to define them again?
    phone_number = PhoneNumberField()
    email = models.EmailField()


class Publisher(models.Model):
    name = models.CharField(max_length=40)
    country = models.CharField(max_length=20)
    city = models.CharField(max_length=10)
    email = models.EmailField()
    phone_number = PhoneNumberField()
    website = models.URLField()


class Category(models.Model):
    name = models.CharField(max_length=20)


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    publication_date = models.DateField()
