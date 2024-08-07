from django.http.response import HttpResponse

# Create your views here.


def test(request) -> HttpResponse:
    return HttpResponse("TEsttesttest")
