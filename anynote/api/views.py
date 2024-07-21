from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions, generics
from rest_framework.views import APIView

from api.serializers import UserSerializer, UsersSerializer


class UsersApiView(generics.ListCreateAPIView):
    """
    API endpoint that allows to get all users' data.

    Only for debugging
    permission: is_staff

    """
    queryset = User.objects.all()
    serializer_class = UsersSerializer
    # permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]


usersApiView = UsersApiView.as_view()


class UserApiView(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows to get a specific ser data.

    Only for debugging
    permission: is_staff

    """
    queryset = User.objects.all()
    lookup_field = "pk"
    serializer_class = UsersSerializer


userApiView = UserApiView.as_view()
