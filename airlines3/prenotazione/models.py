from django.db import models

from datetime import date

class Airport(models.Model):
    name        = models.CharField(max_length=250)
    localcode   = models.IntegerField()
    country     = models.CharField(max_length=250)
    region      = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Fly(models.Model):
    start = models.ForeignKey(Airport, default=None, on_delete=models.SET_DEFAULT, related_name='start')
    arrive = models.ForeignKey(Airport, default=None, on_delete=models.SET_DEFAULT, related_name='arrive')
    time = models.DateField()
    