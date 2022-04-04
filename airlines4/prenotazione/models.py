from datetime import datetime
from django.db import models

class Airport(models.Model):
    name        = models.CharField(max_length=250)
    localcode   = models.IntegerField()
    country     = models.CharField(max_length=250)
    region      = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Search(models.Model):
    start = models.ForeignKey(Airport, on_delete=models.SET_DEFAULT, default=-1, related_name='start')
    arrive = models.ForeignKey(Airport, on_delete=models.SET_DEFAULT, default=-2, related_name='arrive')
    day = models.DateField(default=datetime.now)
    hour = models.TimeField(default=datetime.now)

class Fly(models.Model):
    Fly_start = models.ForeignKey(Airport, on_delete=models.SET_DEFAULT, default=-1, related_name='Fly_start')
    Fly_arrive = models.ForeignKey(Airport, on_delete=models.SET_DEFAULT, default=-2, related_name='Fly_arrive')
    Fly_day = models.DateField(default=datetime.now)
    Fly_hour = models.TimeField(default=datetime.now)