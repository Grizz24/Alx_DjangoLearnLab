
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Tag
from .models import Comment

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
            tags_str = self.cleaned_data['tags']
            tag_names = [t.strip() for t in tags_str.split(',') if t.strip()]
            for name in tag_names:
                tag, created = Tag.objects.get_or_create(name=name)
                instance.tags.add(tag)
        return instance

class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows':3}), label='')

    class Meta:
        model = Comment
        fields = ['content']