from django.shortcuts import render
from rest_framework import generics, permissions

from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Author, Book, Biography, Article
from .serializers import AuthorModelSerializer, ArticleModelSerializer, BookModelSerializer, \
    BiographyModelSerializer, AuthorNameSerializer


# class AuthorViewSet(generics.ListAPIView):
class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer

    def get_serializer_class(self):
        print(self.request.version)
        if self.request.version == '1':
            return AuthorNameSerializer
        return AuthorModelSerializer


class BookViewSet(ModelViewSet):
    # permission_classes = [permissions.IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer

    # def get_serializer_class(self):
    #     if self.request.method in ['GET']:
    #         return BookSerializerNew
    #     return BookModelSerializer


class BiographyViewSet(ModelViewSet):
    queryset = Biography.objects.all()
    serializer_class = BiographyModelSerializer


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleModelSerializer



