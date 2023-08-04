from django.urls import path
from .views import UserListView, UserCreateAPIView

urlpatterns = [
    path('', UserListView.as_view(), name='user-list'),
    path('create/', UserCreateAPIView.as_view(), name='user-create'),
]