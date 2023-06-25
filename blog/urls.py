from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path('search/', views.post_search, name='post_search'),
    path('', views.post_list, name='post_list'),
    path('category/<slug:category>/', views.post_list, name='category_post_list'),
    path('tag/<slug:tag_slug>/', views.post_list, name='tag_post_list'),
    path('<slug>/', views.post_detail, name='post_detail'),
    path('post_like/<int:pk>', views.post_like, name='post_like')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)