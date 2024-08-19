from django.http.response import HttpResponse

# Create your views here.

def test(request) -> HttpResponse:
    """Unused view for main app."""
    return HttpResponse("TEsttesttest")
