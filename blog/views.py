from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.core.paginator import (
    Paginator,
    EmptyPage,
    PageNotAnInteger,
)
from django.contrib.postgres.search import SearchVector

from .models import Category, Post, Comment
from blog.forms import CommentForm, SearchPost

# Create your views here.

def post_list(request, category=None):
    posts = Post.objects.order_by('-publish')
    categories = Category.objects.all()
    if category:
        category = get_object_or_404(Category, slug=category)
        posts = posts.filter(category=category)
    paginator = Paginator(posts, 4)
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
        'categories': categories,
    }
    
    return render(request, "blog/post/list.html", context)


def post_detail(request, slug: str):
    posts = Post.objects.all()[:4]
    categories = Category.objects.all()
    post = get_object_or_404(Post, slug=slug)
    comments = Comment.objects.filter(post=post.id)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            body = comment_form.cleaned_data['body']
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.author = request.user
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request, 'blog/post/detail.html', {'post': post, 'posts': posts, 'categories': categories, 'comments': comments, 'new_comment': new_comment, 'comment_form': comment_form})


def post_search(request):
    posts = Post.objects.all()[:4]
    categories = Category.objects.all()
    query = None
    results = []
    search_form = SearchPost()
    if 'query' in request.GET:
        search_form = SearchPost(request.GET)
        if search_form.is_valid():
            query = search_form.cleaned_data['query']
            results = Post.objects.filter(Q(title__icontains=query) | Q(body__icontains=query))
            
    return render(request, 'blog/post/search.html', {'search_form': search_form, 'query': query, 'results': results, 'posts': posts, 'categories': categories})