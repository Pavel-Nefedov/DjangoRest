from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Author, Article, Book, Biography
from rest_framework import serializers
from rest_framework.serializers import StringRelatedField


class AuthorModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Author
        # exclude = ['url']
        fields = '__all__'


class AuthorNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('first_name', 'last_name')



class BookSerializerNew(HyperlinkedModelSerializer):
    author = AuthorModelSerializer()
    class Meta:
        model = Book
        fields = '__all__'


class BookModelSerializer(HyperlinkedModelSerializer):
    authors = StringRelatedField(many=True)
    # authors = AuthorModelSerializer(many=True)
    class Meta:
        model = Book
        fields = '__all__'



class ArticleModelSerializer(HyperlinkedModelSerializer):
    author = AuthorModelSerializer()
    class Meta:
        model = Article
        fields = '__all__'


class BiographyModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Biography
        fields = '__all__'

