from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from django.views import View

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


# Create your views here.


def test(request):
    return HttpResponse("TEsttesttest")


# class LoginView(View):
#
#     def get(self, request):
#         return render(request, "main/login.html", {})
#
#     def post(self, request):
#         # data = {k: v[0] for k, v in dict(request.POST).items()} # print(data) for testing POST received data.
#         username = request.POST["username"]
#         password = request.POST["password"]
#
#         user = authenticate(
#             request=request,
#             username=username,
#             password=password
#         )
#
#         if user is not None:
#             login(request, user)
#             return HttpResponse(user.username)
#         else:
#             return HttpResponse('failure')
#
#
# loginView = LoginView.as_view()
#
#
# class RegistrationView(View):
#     def get(self, request):
#         return render(request, "main/registration.html", {})
#
#     def post(self, request):
#         # data = {k: v[0] for k, v in dict(request.POST).items()} # print(data) for testing POST received data.
#         username = request.POST["username"]
#         password1 = request.POST["password1"]
#         password2 = request.POST["password2"]
#         if self.username_is_occupied_check(username):
#             return HttpResponse("Username is occupied")
#         else:
#             if password1 == password2:
#                 user = User.objects.create_user(
#                     username=username,
#                     password=password1,
#                 )
#                 return HttpResponseRedirect("/login")
#             else:
#                 return HttpResponse("Passwords must match")
#         # return HttpResponse(str(data))
#
#     @staticmethod
#     def username_is_occupied_check(username):
#         names = list(User.objects.all().values_list("username"))
#         # [print(names[i][0]) for i in range(len(names))]
#         if any(username in names[i][0] for i in range(len(names))):
#             # print("nameOccupied")
#             return True
#         else:
#             # print("nameAccepted")
#             return False
#
#
# registrationView = RegistrationView.as_view()
#
#
# class AccountView(View):
#     def get(self, request):
#         return render(request, "main/account.html", {})
#
#     def post(self, request):
#         data = {k: v[0] for k, v in dict(request.POST).items()}  # print(data) for testing POST received data.
#         return HttpResponse(str(data))
#
#
# accountView = AccountView.as_view()
