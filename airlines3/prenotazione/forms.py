from django import forms


from .models import SearchFly

class SearchFly(forms.ModelForm):
    class Meta:
        model = SearchFly
        fields = ['starting', 'arriving', 'timing']