from rest_framework.generics import ListAPIView, CreateAPIView

from user.models import User
from user.serializers import UserSerializer

class UserListView(ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all().order_by('-created')


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserSerializer


