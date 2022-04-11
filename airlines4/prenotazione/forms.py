from dataclasses import field
from django import forms
from .models import Search, Booking

class SearchForm(forms.ModelForm):
    class Meta:
        model = Search
        fields = ['start', 'arrive', 'day']

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields= '__all__'