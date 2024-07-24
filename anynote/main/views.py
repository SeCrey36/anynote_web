from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from django.views import View

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


# Create your views here.


def test(request):
    return HttpResponse("TEsttesttest")
