from ast import Pass
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home_view(request, *args, **kwargs):
    # pass
    # html = "<h1> hello world </h1>"
    # return HttpResponse(html)
    return render(request, "base.html", {"title": "hello world!"})

# def sum(**args):
#     data = list(*args)
#     return (sum(data))