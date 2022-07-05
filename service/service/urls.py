"""service URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import views
from rest_framework.routers import DefaultRouter

from authors.views import AuthorViewSet, BiographyViewSet, BookViewSet, ArticleViewSet
from usersapp.views import UserViewSet, UserListApiView, UserRetrieveApiView, UserUpdateApiView
from menuapp.views import MenuViewSet
from footerapp.views import FooterViewSet
from todolist.views import TODOViewSet, ProjectAPIDetailView, ProjectViewSet, TODOAPIDetailView

router = DefaultRouter()

router.register('TODO', TODOViewSet)
router.register('projects', ProjectViewSet)
router.register('authors', AuthorViewSet)
router.register('books', BookViewSet)
router.register('articles', ArticleViewSet)
router.register('biographies', BiographyViewSet)
router.register('users', UserViewSet)
router.register('menus', MenuViewSet)
router.register('footers', FooterViewSet)




urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('apiview/', UserListApiView.as_view()),
    path('user_update/<int:pk>/', UserUpdateApiView.as_view()),
    path('user_retrieve/<int:pk>/', UserRetrieveApiView.as_view()),
    path('project_detail/<int:pk>/', ProjectAPIDetailView.as_view()),
    path('todo_detail/<int:pk>/', TODOAPIDetailView.as_view())

]
