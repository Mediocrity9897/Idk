from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.
def procces_get_view(request: HttpRequest) -> HttpResponse:
    context = {
        
    }
    return render(request, "requestdataapp/request-quary-params.html", context=context)


def user_form(request: HttpRequest) -> HttpResponse:
    return render(request, "requestdataapp/request-querry-params.html")