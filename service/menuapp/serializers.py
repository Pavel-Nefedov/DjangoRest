from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Menu


class MenuModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Menu
        fields = [
            'home',
            'catalog',
            'contacts',
            'settings',
            ]