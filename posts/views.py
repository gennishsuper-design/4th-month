from django.shortcuts import render
from django.http.response import HttpResponse
from django.http.request import HttpRequest
# Create your views here.

def hello_word(request: HttpRequest):
    return HttpResponse("<h1>Hello word!</h1>")


def me(request: HttpRequest):
    return HttpResponse("<h1>My name is Zhenish T</h1>")
