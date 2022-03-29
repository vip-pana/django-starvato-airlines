from django.db import models

# Create your models here.
class Airport(models.Model):
    name = models.CharField(max_length=30, default='ciao')
    localcode = models.IntegerField(default=3)
    country = models.CharField(max_length=30 , default='ciao')
    region = models.CharField(max_length=30, default='ciao')

    def __str__(self):
        return self.name

class Fly(models.Model):
    fly_code = models.IntegerField()
