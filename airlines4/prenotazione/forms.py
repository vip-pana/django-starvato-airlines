from dataclasses import field
from django import forms
from .models import Search

class SearchForm(forms.ModelForm):
    class Meta:
        model = Search
        fields = ['start', 'arrive', 'day']