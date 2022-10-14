from rest_framework.serializers import HyperlinkedModelSerializer
from .models import User


class UserModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'firstname',
            'lastname',
            'email',
            ]


class UserAPISerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'is_superuser',
            'is_staff',
            ]