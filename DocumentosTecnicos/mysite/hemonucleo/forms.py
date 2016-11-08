from django import forms

class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=100)
    text = forms.CharField(max_length=100)
