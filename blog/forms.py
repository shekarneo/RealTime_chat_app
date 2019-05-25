from django import forms
from .models import Post

class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['author', 'title', 'created_date', 'published_date', 'content']