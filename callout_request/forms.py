from django import forms
from .models import Request
from .models import Comment

class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ('description', 'slug', 'featured_image', 'author', 'excerpt', 'content')

        widgets = {
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'featured_image': forms.FileInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'excerpt': forms.Textarea(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        self.fields['author'].disabled = True  # Prevent modifying the author field
        if user:
            self.fields['author'].initial = user

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        