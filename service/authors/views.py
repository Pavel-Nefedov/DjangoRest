from django.shortcuts import render
from rest_framework import generics, permissions

from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet


from .models import Author, Book, Biography, Article
from .serializers import AuthorModelSerializer, ArticleModelSerializer, BookModelSerializer, BiographyModelSerializer


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer


class BookViewSet(ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer


class BiographyViewSet(ModelViewSet):
    queryset = Biography.objects.all()
    serializer_class = BiographyModelSerializer


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleModelSerializer



