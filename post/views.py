from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def hello(request):
    return render(request, 'post/hello.html')


def greet(request):
    return render(request, 'post/greet.html')


def salut(request):
    return HttpResponse("Forward ever!!!!")