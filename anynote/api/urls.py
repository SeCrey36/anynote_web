from django.urls import path
from api.views import (
    usersApiView,
    userApiView,
    tokenRefreshView,
    tokenObtainPairView,
    tokenVerifyView,
    notesApiView,
    noteApiView,
)

urlpatterns = [
    path("users/", usersApiView, name="usersApi"),
    path("user/", userApiView, name="userApi"),

    path("notes/", notesApiView, name="notesApi"),
    path("note/", noteApiView, name="noteApi"),

    path("token/", tokenObtainPairView, name="token_obtain_pair"),
    path("token/refresh/", tokenRefreshView, name="token_refresh"),
    path("token/verify/", tokenVerifyView, name="token_verify")
]
