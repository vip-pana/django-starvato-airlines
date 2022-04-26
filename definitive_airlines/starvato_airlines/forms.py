from dataclasses import fields
from pyexpat import model
from django import forms
from .models import Cache, Fly, Booking

class FlyForm(forms.ModelForm):
    class Meta:
        model = Fly
        fields = ['start','arrive','date','date_rit']

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['unique_id','name','surname','email','address','city','state','zip_code','fly','fly_seat',]

class CacheForm(forms.ModelForm):
    class Meta:
        model = Cache
        fields = ['flyone','flytwo']