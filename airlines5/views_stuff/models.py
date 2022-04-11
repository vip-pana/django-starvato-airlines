from contextlib import nullcontext
from django.db import models

# Create your models here.
class Underbanner(models.Model):
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=30, default='undefined')
    description = models.TextField(max_length=200, default='description undefined')

    def __str__(self) -> str:
        return self.title + ' ' +str(self.image)