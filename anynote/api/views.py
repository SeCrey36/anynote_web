from django.conf import settings
from django.contrib.auth.models import User
from django.http import Http404

from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied

import jwt
from main.models import NoteModel
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from api.serializers import NotesSerializer, UsersSerializer


class RegisterApiView(generics.CreateAPIView):
    """API endpoint that allows to register a new user

    """

    queryset = User.objects.all()
    serializer_class = UsersSerializer
    permission_classes = [permissions.AllowAny]


registerApiView = RegisterApiView.as_view()

tokenObtainPairView = TokenObtainPairView.as_view()

tokenRefreshView = TokenRefreshView.as_view()

tokenVerifyView = TokenVerifyView.as_view()


class AccountApiView(generics.RetrieveUpdateDestroyAPIView):
    """API endpoint that allows to get a data of user who requests this page and is authenticated.

    Working version
    permission: is_authenticated

    """

    queryset = User.objects.all()
    serializer_class = UsersSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        access_token = self.request.META.get('HTTP_AUTHORIZATION').split()[1]
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


class AccountNotesApiView(generics.ListCreateAPIView):
    """API endpoint that allows to get and post users Note data

    permission: is_authenticated
    """

    queryset = NoteModel.objects.all()
    serializer_class = NotesSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        access_token = self.request.META.get('HTTP_AUTHORIZATION').split()[1]
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

    def post(self, request, *args, **kwargs):
        request.data["user"] = request.user.id
        print(request.data)
        return self.create(request, *args, **kwargs)


accountNotesApiView = AccountNotesApiView.as_view()


class AccountNoteApiView(generics.RetrieveUpdateDestroyAPIView):
    """API endpoint that allows to get post and patch individual Note data

    permission: is_authenticated
    """

    queryset = NoteModel.objects.all()
    serializer_class = NotesSerializer
    lookup_field = "pk"
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


accountNoteApiView = AccountNoteApiView.as_view()


# DIRECT DATA ACCESS VIEWS. FOR DEBUGGING

class UsersApiView(generics.ListCreateAPIView):
    """API endpoint that allows to get and post users' data.

    Only for debugging
    permission: is_staff

    """

    queryset = User.objects.all()
    serializer_class = UsersSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]


usersApiView = UsersApiView.as_view()


class UserApiView(generics.RetrieveUpdateDestroyAPIView):
    """API endpoint that allows to get post and patch individual user data.

    Only for debugging
    permission: is_staff

    """

    queryset = User.objects.all()
    lookup_field = "pk"
    serializer_class = UsersSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]


userApiView = UserApiView.as_view()


class NotesApiView(generics.ListCreateAPIView):
    """API endpoint that allows to get all Notes' data

    Only for debugging
    permission: is_staff

    """

    queryset = NoteModel.objects.all()
    serializer_class = NotesSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]


# def post(self, request, *args, **kwargs):
#       print(request)
#       serializer = self.get_serializer(data=request.data)
#       serializer.is_valid(raise_exception=True)
#       self.perform_create(serializer)
#       headers = self.get_success_headers(serializer.data)
#       return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
#       # return self.create(request, *args, **kwargs)


notesApiView = NotesApiView.as_view()


class NoteApiView(generics.RetrieveUpdateDestroyAPIView):
    """API endpoint that allows to get post and patch individual Note data

    Only for debugging
    permission: is_staff

    """

    queryset = NoteModel.objects.all()
    serializer_class = NotesSerializer
    lookup_field = "pk"
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]


noteApiView = NoteApiView.as_view()
