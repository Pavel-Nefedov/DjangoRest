from rest_framework.viewsets import ModelViewSet
from .models import Menu
from .serializers import MenuModelSerializer


class MenuViewSet(ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuModelSerializer
