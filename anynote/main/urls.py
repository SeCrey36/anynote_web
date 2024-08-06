from django.urls import path

from . import views

urlpatterns = [
    path("test/", views.test),
]


# from .views import loginView, registrationView, accountView
# path("login/", loginView),
# path("registration/", registrationView),
# path("account/", accountView)
