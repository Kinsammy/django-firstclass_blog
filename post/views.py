from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post


# Create your views here.
def hello(request):
    # The posts will be available on the  post template te
    # Load all posts to object
    # pass it to the 3rd argument
    posts = Post.objects.all()
    return render(request, 'post/hello.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post/post_detail.html', {'post': post})


def greet(request):
    return render(request, 'post/greet.html')


def salut(request):
    return HttpResponse("Forward ever!!!!")
