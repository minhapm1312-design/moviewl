from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):

    class Meta:
        model = Movie
        exclude = ['user']

        widgets = {
            'rating': forms.HiddenInput(),
            'review': forms.Textarea(attrs={'rows': 4}),
        }