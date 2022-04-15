from datetime import datetime
from django.db import models
from .utils import unique_id


class Airport(models.Model):
    unique_id   = models.CharField(max_length=36, default=unique_id())
    name        = models.CharField(max_length=250)
    localcode   = models.IntegerField()
    country     = models.CharField(max_length=250)
    region      = models.CharField(max_length=250) 

    def __str__(self) -> str:
        return self.name


class Aircraft(models.Model):
    unique_id   = models.CharField(max_length=36, default=unique_id())
    model       = models.CharField(max_length=100)
    seats       = models.IntegerField(default=60)
    km_tot      = models.IntegerField(default=0)
    pilots_num  = models.IntegerField(default=4)
    team_num    = models.IntegerField(default=4)

    def __str__(self) -> str:
        return self.model + ' ' + str(self.id)


class Fly(models.Model):
    unique_id   = models.CharField(max_length=36, default=unique_id())
    aircraft    = models.ForeignKey(Aircraft, on_delete=models.SET_NULL, null=True, related_name='aircraft')
    start       = models.ForeignKey(Airport, on_delete=models.SET_NULL, null=True, related_name='start')
    arrive      = models.ForeignKey(Airport, on_delete=models.SET_NULL, null=True, related_name='arrive')
    date        = models.DateField(default=datetime.now)
    hour        = models.TimeField(default=datetime.now)

    def __str__(self) -> str:
        return str(self.start) + ' - ' + str(self.arrive) + ' ' +str(self.date)


class Search(models.Model):
    start       = models.ForeignKey(Airport, on_delete=models.SET_NULL, null=True, related_name='S_start')
    arrive      = models.ForeignKey(Airport, on_delete=models.SET_NULL, null=True, related_name='S_arrive')
    date        = models.DateField(default=datetime.now)

    def __str__(self) -> str:
        return str(self.start) + ' ' + str(self.arrive) + ' ' + str(self.date)


class Booking(models.Model):
    unique_id       = models.CharField(max_length=36, default=unique_id())
    fly             = models.ForeignKey(Fly, on_delete=models.SET_NULL, null=True, related_name='fly_booking')
    airC_seat       = models.CharField(max_length=5)
    name            = models.CharField(max_length=200)
    surname         = models.CharField(max_length=200)
    email           = models.EmailField()
    address         = models.CharField(max_length=200)
    city            = models.CharField(max_length=200)
    state           = models.CharField(max_length=200)
    zip_code        = models.IntegerField()

    def __str__(self):
        return str(self.fly) +  ' ' + str(self.id)