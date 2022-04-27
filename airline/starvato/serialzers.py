from rest_framework import serializers
from .models import *

class IdentifyAPI(serializers.ModelSerializer):
    class Meta:
        model = Identify
        fields = '__all__'

class AirportAPI(serializers.ModelSerializer):
    class Meta:
        model = Airport
        fields = '__all__'

class AircraftAPI(serializers.ModelSerializer):
    class Meta:
        model = Aircraft
        fields = '__all__'

class FlyAPI(serializers.ModelSerializer):
    class Meta:
        model = Fly
        fields = '__all__'

class BookingAPI(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

