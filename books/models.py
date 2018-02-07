from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Author(models.Model):
    name = models.CharField(max_length=40, unique=True)
    surname = models.CharField(max_length=40, unique=True)
    phone_number = PhoneNumberField(null=True)
    email = models.EmailField(null=True)


class Publisher(models.Model):
    name = models.CharField(max_length=40, unique=True)
    country = models.CharField(max_length=20, null=True)
    city = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True)
    phone_number = PhoneNumberField(null=True)
    website = models.URLField(null=True)


class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ManyToManyField(Author, related_name='books')
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, related_name='books')
    publication_date = models.DateField(null=True)
