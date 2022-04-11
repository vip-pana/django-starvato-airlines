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
