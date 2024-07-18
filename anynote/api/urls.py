from django.urls import path
from api.views import usersApiView, userApiView

urlpatterns = [
    path('users/', usersApiView, name="usersApi"),
    path('users/<int:pk>', userApiView, name="userApi"),
]
