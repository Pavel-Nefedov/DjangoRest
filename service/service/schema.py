import graphene
from graphene_django import DjangoObjectType

from todolist.models import TODO, Project
from usersapp.models import User


class ToDoType(DjangoObjectType):
    class Meta:
        model = TODO
        fields = '__all__'


class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = '__all__'


class Query(graphene.ObjectType):
    all_todo = graphene.List(ToDoType)
    all_project = graphene.List(ProjectType)
    all_user = graphene.List(UserType)

    def resolve_all_todo(self, info):
        return TODO.objects.all()

    def resolve_all_project(self, info):
        return Project.objects.all()

    def resolve_all_user(self, info):
        return User.objects.all()


    hello = graphene.String(default_value="Hi!")


schema = graphene.Schema(query=Query)

# Схема д/з для graphQl

# {
# 	allTodo{
# 	id
#   title
#   isActive
# 	project {
#   	id
#     name
#   	users{
#       username
#     	firstname
#     	lastname
#     }
#   }
#   }
# }
