import self as self
from django.test import TestCase
import json
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APISimpleTestCase, APITestCase
from mixer.backend.django import mixer
from django.contrib.auth.models import User
from .views import AuthorViewSet
from .models import Author, Book


# APIRequestFactory

class TestAuthorViewSet(TestCase):
    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get('/api/authors/')
        view = AuthorViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_guest(self):
        factory = APIRequestFactory()
        request = factory.post('/api/authors/',
                               {'name': 'Пушкин', 'birthday_year': 1799},
                               format='json')
        view = AuthorViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_admin(self):
        factory = APIRequestFactory()
        request = factory.post('/api/authors/',
                               {'first_name': 'Пушкин', 'last_name': 'Саня',
                                'birthday_year': 1799, 'email': 'sdgag@mail.ru'},
                               format='json')
        admin = User.objects.create_superuser('admin', 'admin@mail.ru', 'admin')
        force_authenticate(request, admin)
        view = AuthorViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

# APIClient

    def test_get_detail(self):
        author = Author.objects.create(first_name='Пушкин', birthday_year=1799)

        client = APIClient()
        response = client.get(f'/api/authors/{author.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_guest(self):
        author = Author.objects.create(first_name='Пушкин', birthday_year=1799)

        client = APIClient()
        response = client.put(f'/api/authors/{author.id}/', {'name': 'Грин',
                                                             'birthday_year': 1880})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_edit_admin(self):
        author = Author.objects.create(first_name='Пушкин', last_name='Саня', birthday_year=1799, email='ermat@mail.ru')
        client = APIClient()
        User.objects.create_superuser('admin', 'admin@mail.ru', 'admin')
        client.login(username='admin', password='admin')
        response = client.put(f'/api/authors/{author.id}/', {'first_name': 'Грин',
                                                             'last_name': 'Саня',
                                                             'birthday_year': 1920,
                                                             'email': 'ermat@mail.ru'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        author = Author.objects.get(id=author.id)
        self.assertEqual(author.first_name, 'Грин')
        self.assertEqual(author.birthday_year, 1920)
        client.logout()

####

class TestMath(APISimpleTestCase):

    def test_sqrt(self):
        import math
        self.assertEqual(math.sqrt(4), 2)

#####

# APITestCase

class TestBookViewSet(APITestCase):
    def test_get_list(self):
        response = self.client.get('/api/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_edit_admin(self):
    #     author = Author.objects.create(first_name='Пушкин', last_name='Саня', birthday_year=1799, email='ermat@mail.ru')
    #     book = Book.objects.create(name='Пиковая дама')
    #
    #     admin = User.objects.create_superuser('admin', 'admin@admin.com', 'admin123456')
    #     self.client.login(username='admin', password='admin123456')
    #
    #     response = self.client.put(f'/api/books/{book.id}/',
    #                                {'name': 'Руслан и Людмила'})
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     book = Book.objects.get(id=book.id)
    #     self.assertEqual(book.name, 'Руслан и Людмила')

    def test_edit_mixer(self):
        author = mixer.blend(Author)

        admin = User.objects.create_superuser('admin', 'admin@admin.com', 'admin123456')
        self.client.login(username='admin', password='admin123456')
        response = self.client.put(f'/api/authors/{author.id}/', {'first_name': 'Санёк',
                                                             'last_name': 'Грин',
                                                             'birthday_year': 1880,
                                                             'email': 'ermat@mail.ru'})
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        author = Author.objects.get(id=author.id)
        self.assertEqual(author.first_name, 'Санёк')

