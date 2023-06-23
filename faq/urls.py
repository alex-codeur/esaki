from django.urls import path

from . import views

urlpatterns = [
   path('questions/', views.QuestionListView.as_view(), name='question_lists'),
   path('questions/<int:pk>', views.QuestionDetailView.as_view(), name='question_detail')
]