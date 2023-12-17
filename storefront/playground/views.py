from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# helps to response for a request or it is just request hundler or action
# define functions here 

def hello(request):
    return HttpResponse('Hello World')

