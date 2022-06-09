from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Author, Article, Book, Biography
from rest_framework.serializers import StringRelatedField


class AuthorModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Author
        exclude = ['url', 'email']

class BiographyModelSerializer(HyperlinkedModelSerializer):
    author = AuthorModelSerializer()

    class Meta:
        model = Biography
        fields = '__all__'

class BookModelSerializer(HyperlinkedModelSerializer):
    #authors = StringRelatedField(many=True)
    authors = AuthorModelSerializer(many=True)

    class Meta:
        model = Book
        fields = '__all__'

class ArticleModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'