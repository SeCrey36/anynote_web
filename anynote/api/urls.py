from django.urls import path
from api.views import (
    usersApiView,
    userApiView,
    tokenRefreshView,
    tokenObtainPairView,
    tokenVerifyView,
)

urlpatterns = [
    path("users/", usersApiView, name="usersApi"),
    path("users/<int:pk>/", userApiView, name="userApi"),

    path("token/", tokenObtainPairView, name="token_obtain_pair"),
    path("token/refresh/", tokenRefreshView, name="token_refresh"),
    path("token/verify/", tokenVerifyView, name="token_verify")
]
