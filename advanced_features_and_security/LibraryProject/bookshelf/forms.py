from django import forms
from .models import Book, CustomUser


# A model form for Book
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "published_date"]  # adjust to your actual model fields


# A form for searching books safely
class SearchForm(forms.Form):
    title = forms.CharField(max_length=100)


# A form for your custom user (optional, for registration/profile updates)
class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ["username", "email", "date_of_birth", "profile_photo"]
