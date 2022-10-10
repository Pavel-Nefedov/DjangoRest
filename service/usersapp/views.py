from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.renderers import JSONRenderer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import User
from .serializers import UserModelSerializer



class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


class UserListApiView(ListAPIView):
    renderer_classes = [JSONRenderer]
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


class UserRetrieveApiView(RetrieveAPIView):
    renderer_classes = [JSONRenderer]
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


class UserUpdateApiView(UpdateAPIView):
    renderer_classes = [JSONRenderer]
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    premission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication,)

