from django.contrib import admin
from .models import Category, Post, Comment

# Register your models here.

# admin.site.register(Post)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('image_tag', 'title', 'status', 'tags', 'created', 'publish', 'author')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'body')
    ordering = ('author', 'status', 'publish')
    list_filter = ('author', 'created', 'publish')
    list_editable = ['status', 'tags']
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['created']