from django.db import models

from datetime import datetime

class Airport(models.Model):
    name        = models.CharField(max_length=250)
    localcode   = models.IntegerField()
    country     = models.CharField(max_length=250)
    region      = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    

class SearchFly(models.Model):
    starting = models.ForeignKey(Airport, on_delete=models.SET_DEFAULT, null=True, related_name='starting', default=-3)
    arriving = models.ForeignKey(Airport, on_delete=models.SET_NULL, null=True, related_name='arriving', default=-4)
    timing = models.DateField(null=True)
    hourStart = models.TimeField(default=datetime.now)



class Fly(models.Model):
    start = models.ForeignKey(Airport, on_delete=models.SET_NULL, null=True, related_name='start', default=-1)
    arrive = models.ForeignKey(Airport, on_delete=models.SET_NULL, null=True, related_name='arrive', default=-2)
    time = models.DateField(null=True)
    hourStart = models.TimeField(default=datetime.now)