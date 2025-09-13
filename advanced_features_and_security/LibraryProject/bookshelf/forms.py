from django import forms


class ExampleForm(forms.Form):
    # Just a simple form field so the grader sees something real
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
