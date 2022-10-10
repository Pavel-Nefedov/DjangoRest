from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination
from rest_framework.renderers import JSONRenderer
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from .models import TODO, Project
from .serializers import TODOModelSerializer, ProjectModelSerializer

class TODOAPIListPagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'page_size'
    max_page_size = 20


class TODOViewSet(ModelViewSet):
    queryset = TODO.objects.all()
    serializer_class = TODOModelSerializer
    pagination_class = TODOAPIListPagination

    def delete(self, request, *args, **kwargs):
        return TODO.is_active(False)

class TODOAPIDetailView(RetrieveUpdateDestroyAPIView):
    queryset = TODO.objects.all()
    serializer_class = TODOModelSerializer
    pagination_class = TODOAPIListPagination

    def get_queryset(self):
        param = self.request.query_params.get('name')
        if param is not None:
            return TODO.objects.filter(name__contains=param)
        return super().get_queryset()


class ProjectAPIListPagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'page_size'
    max_page_size = 10


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    pagination_class = ProjectAPIListPagination


class ProjectAPIDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    pagination_class = ProjectAPIListPagination

    def get_queryset(self):
        param = self.request.query_params.get('title')
        if param is not None:
            return Project.objects.filter(title__contains=param)
        return super().get_queryset()