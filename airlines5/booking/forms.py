from django import forms
from .models import Search, Booking

class SearchForm(forms.ModelForm):
    class Meta:
        model = Search
        fields = '__all__'
        


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'