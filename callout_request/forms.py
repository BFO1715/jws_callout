from django import forms
from.models import Request

class RequestForm(forms.ModelForm):
    class meta:
        model = Request
        fields = ('description', 'slug', 'featured_image', 'author', 'excerpt', 'content')

        widgets = {
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'featured_image': forms.ImageField(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'excerpt': forms.Textarea(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }