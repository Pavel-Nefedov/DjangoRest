from uuid import uuid4

from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=64)
    birthday_year = models.PositiveIntegerField()
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name


class Biography(models.Model):
    text = models.TextField(max_length=32)
    author = models.OneToOneField(Author, on_delete=models.CASCADE)


class Book(models.Model):
    name = models.CharField(max_length=32)
    authors = models.ManyToManyField(Author)

class Article(models.Model):
    name = models.CharField(max_length=32)
    author = models.OneToOneField(Author, on_delete=models.CASCADE)
