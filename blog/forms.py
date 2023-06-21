from django import forms

from .models import Comment

class CommentForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={'class': "w-full bg-white rounded border border-gray-300 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 h-32 text-base outline-none text-gray-700 py-1 px-3 resize-none leading-6 transition-colors duration-200 ease-in-out"}))
    
    class Meta:
        model = Comment
        fields = ['body']
        
class SearchPost(forms.Form):
    query = forms.CharField(max_length=200)
    
    class Meta:
        fields = ['query']