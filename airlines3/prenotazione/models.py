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
    start = models.ForeignKey(Airport, on_delete=models.SET_NULL, null=True, related_name='start', default=-1)
    arrive = models.ForeignKey(Airport, on_delete=models.SET_NULL, null=True, related_name='arrive', default=-2)
    time = models.DateField(null=True)
    hourStart = models.TimeField()
    