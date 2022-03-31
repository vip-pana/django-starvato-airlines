from dataclasses import fields
from django import forms


from .models import Fly

class SearchForm(forms.ModelForm):
    class Meta:
        model = Fly
        fields = ['start', 'arrive', 'time']