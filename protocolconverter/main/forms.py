from django import forms
from .models import *


class GackPath(forms.Form):
    path = forms.CharField(widget=forms.Textarea(attrs={'cols': 40, 'rows': 5}),
                           label="путь до gack файла")
