# ruff: noqa: E501
from django.urls import path

from api.views import (
    accountApiView,
    accountNoteApiView,
    accountNotesApiView,
    notesApiView,
    registerApiView,
    tokenObtainPairView,
    tokenRefreshView,
    tokenVerifyView,
    userApiView,
    usersApiView,
)

urlpatterns = [
    path("users/", usersApiView, name="usersApi"),
    path("users/<int:pk>", userApiView, name="userApi"),
    path("notes/", notesApiView, name="notesApi"),
    path("notes/<int:pk>", notesApiView, name="noteApi"),

    path("auth/login/", tokenObtainPairView, name="token_obtain_pair"),
    path("auth/register/", registerApiView, name="register_api"),
    path("auth/refresh/", tokenRefreshView, name="token_refresh"),
    path("auth/verify/", tokenVerifyView, name="token_verify"),

    path("account/", accountApiView, name="accountApi"),
    path("account/notes/", accountNotesApiView, name="accountNotesApiView"),
    path("account/notes/<int:pk>/", accountNoteApiView, name="accountNotesApiView"),
]
