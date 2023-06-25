from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image
from django.utils.html import format_html

from taggit.managers import TaggableManager
from cloudinary.models import CloudinaryField
from ckeditor.fields import RichTextField


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')

# Category model

class Category(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    
    def __str__(self) -> str:
        return self.name

# Post model

class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category_posts")
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = RichTextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_CHOICES, default='draft', max_length=10)
    publish = models.DateTimeField(default=timezone.now())
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posted')
    image = CloudinaryField('image')
    tags = TaggableManager()
    objects = models.Manager() # Default manager
    published = PublishedManager() # Custom manager
    likes = models.ManyToManyField(User, related_name="post_like", blank=True)
    
    def __str__(self) -> str:
        return self.title
    
    # Keep track or count of likes
    def number_of_likes(self):
        return self.likes.count()
            
    def image_tag(self):
        return format_html('<img src="{}" style="width:50px; height:50px;border-radius:50%;"/>'.format(self.image.url))
    
    
# Comment model

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.post.title
    