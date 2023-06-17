from django.shortcuts import render, get_object_or_404
from django.core.paginator import (
    Paginator,
    EmptyPage,
    PageNotAnInteger,
)

from .models import Post

# Create your views here.

def post_list(request):
    object_list = Post.objects.all()
    paginator = Paginator(object_list, 4)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
        
    context = {
        'posts': posts,
        'page': page,
    }
    
    return render(request, "blog/post/list.html", context)

def post_detail(request, slug: str):
    post = get_object_or_404(Post, slug=slug)
    
    return render(request, 'blog/post/detail.html', {'post': post})