from rest_framework.serializers import HyperlinkedModelSerializer
from .models import TODO, Project

from usersapp.models import User

class SimpleUserModelSerializer(HyperlinkedModelSerializer): #чтобы выводить только имя и фамилию
    class Meta:
        model = User
        fields = ['firstname', 'lastname']

class TODOModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = TODO
        fields = '__all__'

class ProjectModelSerializer(HyperlinkedModelSerializer):
    #users = SimpleUserModelSerializer(many=True)

    class Meta:
        model = Project
        fields = '__all__'