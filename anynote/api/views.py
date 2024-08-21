from django.contrib.auth.models import User

from rest_framework import generics, permissions

from api.serializers import NotesSerializer, UsersSerializer
from main.models import NoteModel
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)


class RegisterApiView(generics.CreateAPIView):
    """API endpoint that allows to register a new user."""

    queryset = User.objects.all()
    serializer_class = UsersSerializer
    permission_classes = [permissions.AllowAny]


registerApiView = RegisterApiView.as_view()

tokenObtainPairView = TokenObtainPairView.as_view()

tokenRefreshView = TokenRefreshView.as_view()

tokenVerifyView = TokenVerifyView.as_view()


class AccountApiView(generics.RetrieveUpdateDestroyAPIView):
    """API endpoint that allows to get a logged-in user data.

    Working version
    permission: is_authenticated

    """

    queryset = User.objects.all()
    serializer_class = UsersSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """Return the request's user data."""
        return self.request.user


accountApiView = AccountApiView.as_view()


class AccountNotesApiView(generics.ListCreateAPIView):
    """API endpoint that allows to get and post users Note data.

    permission: is_authenticated
    """

    queryset = NoteModel.objects.all()
    serializer_class = NotesSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """Return notes queryset of a request's user."""
        return NoteModel.objects.filter(user=self.request.user)

    def post(self, request, *args, **kwargs):
        """Create a new note for a request user."""
        request.data["user"] = request.user.id
        return self.create(request, *args, **kwargs)


accountNotesApiView = AccountNotesApiView.as_view()


class AccountNoteApiView(generics.RetrieveUpdateDestroyAPIView):
    """API endpoint that allows to get post and patch individual Note data.

    permission: is_authenticated
    """

    queryset = NoteModel.objects.all()
    serializer_class = NotesSerializer
    lookup_field = "pk"
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """Return notes queryset of a request's user."""
        return NoteModel.objects.filter(user=self.request.user)


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
    """API endpoint that allows to get all Notes' data.

    Only for debugging
    permission: is_staff

    """

    queryset = NoteModel.objects.all()
    serializer_class = NotesSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]


notesApiView = NotesApiView.as_view()


class NoteApiView(generics.RetrieveUpdateDestroyAPIView):
    """API endpoint that allows to get post and patch individual Note data.

    Only for debugging
    permission: is_staff

    """

    queryset = NoteModel.objects.all()
    serializer_class = NotesSerializer
    lookup_field = "pk"
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]


noteApiView = NoteApiView.as_view()
