from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import TODO, Project
from .serializers import TODOModelSerializer, ProjectModelSerializer


class TODOViewSet(ModelViewSet):
    queryset = TODO.objects.all()
    serializer_class = TODOModelSerializer

class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer