from django import forms
from .models import Request
from .models import Comment

# Request form
class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ('description', 'slug', 'featured_image', 'user', 'equipment', 'content')

        widgets = {
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'featured_image': forms.FileInput(attrs={'class': 'form-control'}),
            'user': forms.Select(attrs={'class': 'form-control'}),
            'equipment': forms.Textarea(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }


    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        self.fields['user'].disabled = True  
        if user:
            self.fields['user'].initial = user

# Comment form
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        