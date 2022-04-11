
from datetime import datetime
from django.db import models

from .utils import make_id

class Airport(models.Model):
    name        = models.CharField(max_length=250)
    localcode   = models.IntegerField()
    country     = models.CharField(max_length=250)
    region      = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Search(models.Model):
    start   = models.ForeignKey(Airport, on_delete=models.SET_DEFAULT, default=-1, related_name='start')
    arrive  = models.ForeignKey(Airport, on_delete=models.SET_DEFAULT, default=-2, related_name='arrive')
    day     = models.DateField(default=datetime.now)
    hour    = models.TimeField(default=datetime.now)

class Aircraft(models.Model):
    plate_code      = models.CharField(max_length=250, unique=True)
    aircraft_model  = models.CharField(max_length=250)
    seats           = models.IntegerField(default=40)
    km_tot          = models.IntegerField(default=0, null=True, blank=True) #dovrebbe aumentare a ogni fly
    pilots          = models.IntegerField(default=4) #dovrebbe cambiare a seconda del modello
    team            = models.IntegerField(default=4)

    def __str__(self):
        return self.plate_code

class Fly(models.Model):
    unique_id = models.CharField(max_length=37, default=make_id())#deve essere un generator
    Fly_start = models.ForeignKey(Airport, on_delete=models.SET_DEFAULT, default=-1, related_name='Fly_start')
    Fly_arrive = models.ForeignKey(Airport, on_delete=models.SET_DEFAULT, default=-2, related_name='Fly_arrive')
    Fly_day = models.DateField(default=datetime.now)
    Fly_hour = models.TimeField(default=datetime.now)
    aircraft = models.ForeignKey(Aircraft, on_delete=models.SET_NULL, null=True, default=-4, related_name='aircraft')
    

class Booking(models.Model):
    fly = models.ForeignKey(Fly, on_delete=models.SET_NULL, null=True )
    booking_code = models.CharField(max_length=36, unique=True, blank=True)
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zip_code = models.IntegerField()

    def __str__(self) -> str:
        return self.name + ' ' +self.surname + ' ' + self.booking_code
