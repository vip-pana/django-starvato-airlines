from django.utils.timezone import now
from django.db import models
from .utils import create_unique_id

# Create your models here.

class Identify(models.Model):
    unique_id = models.CharField(max_length=36)

    def __str__(self):
        return self.unique_id

class Airport(models.Model):
    unique_id   = models.CharField(max_length=36, blank=True)
    name        = models.CharField(max_length=100)
    zip_code    = models.IntegerField()
    country     = models.CharField(max_length=100)
    region      = models.CharField(max_length=100) 

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.unique_id == '':
            self.unique_id = create_unique_id(Identify)
            super().save(*args, **kwargs)
        else:
            super().save(*args, **kwargs)

class Aircraft(models.Model):
    unique_id   = models.CharField(max_length=36, blank=True)
    model       = models.CharField(max_length=100)
    seats       = models.IntegerField(default=60)
    pilots_num  = models.IntegerField(default=4)
    team_num    = models.IntegerField(default=4)

    def __str__(self):
        return self.model + ' ' + str(self.id)

    def save(self, *args, **kwargs):
        if self.unique_id == '':
            self.unique_id = create_unique_id(Identify)
            super().save(*args, **kwargs)
        else:
            super().save(*args, **kwargs)

class Fly(models.Model):
    unique_id   = models.CharField(max_length=36, blank=True)
    aircraft    = models.ForeignKey(Aircraft, on_delete=models.SET_NULL, null=True)
    free_seats  = models.IntegerField(default=10000)
    start       = models.ForeignKey(Airport, on_delete=models.SET_NULL, null=True, related_name='start')
    arrive      = models.ForeignKey(Airport, on_delete=models.SET_NULL, null=True, related_name='arrive')
    date        = models.DateField(default=now)
    date_rit    = models.DateField(default=now, blank=True)
    hour_start = models.TimeField(default=now)
    time_arrive = models.TimeField(default=now)
    price       = models.FloatField(default=50.00)

    def save(self, *args, **kwargs):
        if self.unique_id == '':
            self.unique_id = create_unique_id(Identify)
        else:
            pass
        if self.free_seats == 10000:
            self.free_seats = self.aircraft.seats
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.start) + ' - ' + str(self.arrive) + ' ' +str(self.date)


class Booking(models.Model):
    unique_id       = models.CharField(max_length=36, blank=True)
    name            = models.CharField(max_length=100)
    surname         = models.CharField(max_length=100)
    email           = models.EmailField()
    address         = models.CharField(max_length=100)
    city            = models.CharField(max_length=100)
    state           = models.CharField(max_length=100)
    zip_code        = models.IntegerField()
    fly             = models.ForeignKey(Fly, on_delete=models.CASCADE)
    fly_seat        = models.CharField(max_length=4)
    status          = models.CharField(max_length=10, default='null')

    def save(self, *args, **kwargs):
        if self.unique_id == '':
            self.unique_id = create_unique_id(Identify)
            super().save(*args, **kwargs)
        else:
            super().save(*args, **kwargs)

    def __str__(self):
        return self.name + ' ' + self.surname + ' ' + str(self.fly) +  ' ' + str(self.id)

class People(models.Model):
    people = models.IntegerField()