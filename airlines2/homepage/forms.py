from select import select
from django import forms
# NON LO STO USANDO


from .models import Fly

class FlyForm(forms.ModelForm):
    class Meta:
        model=Fly
        fields = [
            'start',
            'arrive',
            'orario',
        ]
        widgets = {
            'start' : forms.Select(attrs={'class':'form-control'}),
        }