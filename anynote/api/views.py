from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions, generics
from rest_framework.views import APIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from rest_framework_simplejwt.authentication import JWTAuthentication

from api.serializers import UserSerializer, UsersSerializer


class UsersApiView(generics.ListCreateAPIView):
    """
    API endpoint that allows to get all users' data.

    Only for debugging
    permission: is_staff

    """
    queryset = User.objects.all()
    serializer_class = UsersSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]


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
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]


userApiView = UserApiView.as_view()

tokenObtainPairView = TokenObtainPairView.as_view()

tokenRefreshView = TokenRefreshView.as_view()

tokenVerifyView = TokenVerifyView.as_view()
