from django.shortcuts import render
from django.http import HttpResponse


def say_hello(request):
    return HttpResponse("This is my first response")

def hello(request):
    return render (request, "hello.html")


# Create your views here.
