from .models import *
from django import forms

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('caption', 'description', 'image')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body', 'posted_by')