from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image
from django.utils.html import format_html

# Create your models here.

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_CHOICES, default='draft', max_length=10)
    publish = models.DateTimeField(default=timezone.now())
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posted')
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    
    def __str__(self) -> str:
        return self.title
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        img = Image.open(self.image.path)
        if img.height > 250 or img.width > 250:
            output_size = (250, 250)
            img.thumbnail(output_size)
            img.save(self.image.path)
            
    def image_tag(self):
        return format_html('<img src="{}" style="width:50px; height:50px;border-radius:50%;"/>'.format(self.image.url))