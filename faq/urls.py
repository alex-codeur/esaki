from django.urls import path

from . import views

urlpatterns = [
   path('questions/', views.QuestionListView.as_view(), name='question_lists'),
   path('questions/new', views.QuestionCreateView.as_view(), name='question_create'),
   path('questions/<int:pk>', views.QuestionDetailView.as_view(), name='question_detail'),
   path('questions/<int:pk>/update', views.QuestionUpdateView.as_view(), name='question_update'),
   path('questions/<int:pk>/delete', views.QuestionDeleteView.as_view(), name='question_delete'),
   path('questions/<int:pk>/comment', views.AddCommentView.as_view(), name='question_comment'),
   path('like/<int:pk>', views.like_view, name='like_post')
]