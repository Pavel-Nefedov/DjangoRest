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
from django.urls import path, include, re_path
from rest_framework import views, permissions
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from graphene_django.views import GraphQLView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

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
router.register('user2s', UserViewSet)
router.register('menus', MenuViewSet)
router.register('footers', FooterViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Library",
        default_version='0.1',
        description="Documentation to out project",
        contact=openapi.Contact(email="admin@admin.local"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),

)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('apiview/', UserListApiView.as_view()),
    path('user_update/<int:pk>/', UserUpdateApiView.as_view()),
    path('user_retrieve/<int:pk>/', UserRetrieveApiView.as_view()),
    path('project_detail/<int:pk>/', ProjectAPIDetailView.as_view()),
    path('todo_detail/<int:pk>/', TODOAPIDetailView.as_view()),
    path('api-token-auth/', views.obtain_auth_token),
    path('api/v1/auth/', include('djoser.urls')),


    path("graphql/", GraphQLView.as_view(graphiql=True)),

    re_path(r'^auth/', include('djoser.urls.authtoken')),
#     re_path(r'^api/(?P<version>\d)/authors/$', AuthorViewSet.as_view()),
#
#     path('api/authors/1', include('authors.urls', namespace='1')),
#     path('api/authors/2', include('authors.urls', namespace='2')),

    # path('api/users/', UserListApiView.as_view()),

    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),


]
