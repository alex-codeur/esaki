from django.shortcuts import render

from .models import Post

# Create your views here.

def post_list(request):
    posts = Post.objects.all()
    
    return render(request, "blog/post/list.html", {'posts': posts})

def post_detail(request, slug: str):
    try:
        post = Post.objects.get(slug=slug)
    except Post.DoesNotExist:
        raise('This post doesnot exist')
    
    return render(request, 'blog/post/detail.html', {'post': post})