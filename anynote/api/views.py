from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from rest_framework_simplejwt.authentication import JWTAuthentication

from api.serializers import UserSerializer, UsersSerializer, NotesSerializer

from main.models import NoteModel


class UsersApiView(generics.ListCreateAPIView):
    """
    API endpoint that allows to get all users' data.

    Only for debugging
    permission: is_staff

    """
    queryset = User.objects.all()
    serializer_class = UsersSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

    # def post(self, request, *args, **kwargs):
    #     serializer = UsersSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #
    #     return Response(serializer.data)


usersApiView = UsersApiView.as_view()


class UserApiView(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows to get a specific user data.

    Only for debugging
    permission: is_staff

    """
    queryset = User.objects.all()
    lookup_field = "pk"
    serializer_class = UsersSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """
        Allows to get only JWT given authorized user data. Restricts access to other users data.

        Custom permissions demonstration.
        """
        print(request.user)
        print(args, kwargs)
        if request.user.id != kwargs.get("pk"):
            return Response("Access denied", status=status.HTTP_403_FORBIDDEN)
        return self.retrieve(request, *args, **kwargs)


userApiView = UserApiView.as_view()


class NotesApiView(generics.ListCreateAPIView):
    """
    API endpoint that allows to get all Notes' data

    Only for debugging
    permission: is_staff
    """

    queryset = NoteModel.objects.all()
    serializer_class = NotesSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]


    def post(self, request, *args, **kwargs):
        request.data["user_id"] = request.user.id
        request.data["user"] = request.user.id
        print(request.data)
        return self.create(request, *args, **kwargs)


notesApiView = NotesApiView.as_view()


class NoteApiView(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows to get post and path individual Note data

    permission: is_authenticated
    """
    queryset = NoteModel.objects.all()
    serializer_class = NotesSerializer
    lookup_field = "pk"
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]


noteApiView = NoteApiView.as_view()

tokenObtainPairView = TokenObtainPairView.as_view()

tokenRefreshView = TokenRefreshView.as_view()

tokenVerifyView = TokenVerifyView.as_view()
