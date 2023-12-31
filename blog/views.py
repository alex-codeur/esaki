from django.db.models import Q, Count
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import (
    Paginator,
    EmptyPage,
    PageNotAnInteger,
)

from taggit.models import Tag

from .models import Category, Post, Comment
from blog.forms import CommentForm, SearchPost

# Create your views here.

def post_list(request, category=None, tag_slug=None):
    posts = Post.published.order_by('-publish')
    categories = Category.objects.all()
    tags = Tag.objects.all()
    tag = None
    if category:
        category = get_object_or_404(Category, slug=category)
        posts = posts.filter(category=category).order_by("publish")
        
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts = posts.filter(tags__in=[tag])
        
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
        'tag': tag,
        'tags': tags,
    }
    
    return render(request, "blog/post/list.html", context)


def post_detail(request, slug: str):
    posts = Post.published.all()[:4]
    categories = Category.objects.all()
    tags = Tag.objects.all()
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
    
    posts_tag_ids = post.tags.values_list('id', flat=True)
    similar_post = Post.published.filter(tags__in=posts_tag_ids).exclude(id=post.id)
    similar_post = similar_post.annotate(same_tags=Count('tags')).order_by('-same_tags', '-publish')[:3]
    
    return render(request, 'blog/post/detail.html', {
        'post': post,
        'posts': posts,
        'categories': categories, 
        'comments': comments, 
        'new_comment': new_comment,
        'comment_form': comment_form, 
        'tags': tags,
        'similar_post': similar_post,
    })


def post_search(request):
    posts = Post.published.all()[:4]
    categories = Category.objects.all()
    tags = Tag.objects.all()
    query = None
    results = []
    search_form = SearchPost()
    if 'query' in request.GET:
        search_form = SearchPost(request.GET)
        if search_form.is_valid():
            query = search_form.cleaned_data['query']
            results = Post.published.filter(Q(title__icontains=query) | Q(body__icontains=query))
            
    return render(request, 'blog/post/search.html', {'search_form': search_form, 'query': query, 'results': results, 'posts': posts, 'categories': categories, 'tags': tags})


def post_like(request, pk):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, id=pk)
        if post.likes.filter(id=request.user.id):
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        return redirect('post_list')
    else:
        messages.success(request, ("You Must Be Logged In To View That Page..."))
        return redirect('post_list')