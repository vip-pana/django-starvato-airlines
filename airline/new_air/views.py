from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from .models import Airport
# Create your views here.

def homepage_view(request, *args, **kwargs):
    ls = Airport.objects.all()
    context = {'obj':ls}
    return render(request, 'homepage/homepage.html', context)




