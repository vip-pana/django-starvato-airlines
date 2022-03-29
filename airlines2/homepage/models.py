from django.db import models

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
    start = models.ForeignKey(Airport, on_delete=models.CASCADE)
    arrive = models.ForeignKey(Airport, on_delete=models.CASCADE)