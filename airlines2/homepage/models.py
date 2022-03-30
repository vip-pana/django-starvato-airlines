from django.db import models
from datetime import datetime

# Create your models here.
class Airport(models.Model): #aereoporto modello
    name = models.CharField(max_length=30, default='ciao')
    localcode = models.IntegerField(default=3)
    country = models.CharField(max_length=30 , default='ciao')
    region = models.CharField(max_length=30, default='ciao')

    def __str__(self):
        return self.name


class UnderBanner(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=30, default='undefined')
    description = models.TextField(max_length=200, default='description undefined')


class Fly(models.Model):
    start = models.ForeignKey(Airport, related_name='start', on_delete=models.CASCADE, default=None)
    arrive = models.ForeignKey(Airport, related_name='arrive',on_delete=models.CASCADE, default=None)
    orario = models.DateTimeField(auto_now=False, auto_now_add=False, default=datetime.now())


    def __str__(self):
        return self.start + '-' + self.arrive
