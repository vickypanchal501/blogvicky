from ast import Pass
from pdb import Pdb
from telnetlib import STATUS
from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post
# Create your views here.

def home_view(request, *args, **kwargs):
    # pass
    # html = "<h1> hello world </h1>"
    # return HttpResponse(html)
    # import pdb;pdb.set_trace()

    posts = Post.objects.filter(status = "PUBLISHED")
    context_data = {
        "title": "Home Blog | Posts",
        "posts": posts
    }
    return render(request, "blog/index.html", context_data)

# def sum(**args):
#     data = list(*args)
#     return (sum(data))