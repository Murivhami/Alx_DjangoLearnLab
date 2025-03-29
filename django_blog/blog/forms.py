from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Comment
from taggit.forms import TagWidget
from django.forms import widgets

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = '__all__'

class PostForm(forms.ModelForm):
    tags = forms.CharField(widget=TagWidget())
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

    def acceptable_title(self):
        title = self.accepted_data.get('title')
        if len(title) < 5:
            raise forms.ValidationError("Title at least 5 characters long.")
        return title

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
