from django.conf import settings
from django.http import Http404
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions, generics
from rest_framework.exceptions import PermissionDenied
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
import jwt


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
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]


userApiView = UserApiView.as_view()


class AccountApiView(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows to get a data of user who requests this page and is authenticated.

    Working version
    permission: is_authenticated

    """
    queryset = User.objects.all()
    serializer_class = UsersSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        access_token = self.request.META.get('HTTP_AUTHORIZATION').split()[1]
        print(access_token)
        try:
            decoded_token = jwt.decode(access_token, settings.SECRET_KEY, algorithms=['HS256'])
            user_id = decoded_token.get('user_id')
            if user_id:
                return User.objects.get(pk=user_id)
            else:
                raise Http404("Note not found.")

        except jwt.exceptions.InvalidSignatureError:
            raise PermissionDenied("Invalid access token.")

        except NoteModel.DoesNotExist:
            raise Http404("Note not found.")


accountApiView = AccountApiView.as_view()


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
        # request.data["user_id"] = request.user.id
        # request.data["user"] = request.user.id
        print(request.data)
        return self.create(request, *args, **kwargs)


notesApiView = NotesApiView.as_view()


class NoteApiView(generics.ListCreateAPIView):
    """
    API endpoint that allows to get post and path individual Note data

    permission: is_authenticated
    """
    queryset = NoteModel.objects.all()
    serializer_class = NotesSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        access_token = self.request.META.get('HTTP_AUTHORIZATION').split()[1]
        print(access_token)
        try:
            decoded_token = jwt.decode(access_token, settings.SECRET_KEY, algorithms=['HS256'])
            user_id = decoded_token.get('user_id')
            if user_id:
                return NoteModel.objects.filter(user=User.objects.get(pk=user_id))
            else:
                raise Http404("Note not found.")

        except jwt.exceptions.InvalidSignatureError:
            raise PermissionDenied("Invalid access token.")

        except NoteModel.DoesNotExist:
            raise Http404("Note not found.")


noteApiView = NoteApiView.as_view()

tokenObtainPairView = TokenObtainPairView.as_view()

tokenRefreshView = TokenRefreshView.as_view()

tokenVerifyView = TokenVerifyView.as_view()
