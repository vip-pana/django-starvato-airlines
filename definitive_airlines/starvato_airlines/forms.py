from django import forms
from .models import Fly, Booking

class FlyForm(forms.ModelForm):
    class Meta:
        model = Fly
        fields = ['start','arrive','date','date_rit']

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['unique_id','name','surname','email','address','city','state','zip_code','fly','fly_seat',]

