from typing import Any
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Question

# Create your views here.
class QuestionListView(ListView):
    model = Question
    context_object_name = 'questions'
    ordering = ['-date_created']
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_input = self.request.GET.get('search-area') or ""
        if search_input:
            context['questions'] = context['questions'].filter(title__icontains=search_input)
            context['search_input'] = search_input
        return context
    

class QuestionDetailView(DetailView):
    model = Question
    

class QuestionCreateView(CreateView):
    model = Question
    fields = ['title', 'content']
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)