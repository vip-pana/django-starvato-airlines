from multiprocessing import context
from time import time
from django.shortcuts import render

from prenotazione.models import Fly

from .forms import SearchForm


def home_view(request, *args, **kwargs):
    search = SearchForm()
    context = {'search':search}

    if request.method == 'POST':
        search = SearchForm(request.POST)
        if search.is_valid():
            startForm = request.POST['start']
            arriveForm = request.POST['arrive']
            timeForm = request.POST['time']
            querySet = Fly.objects.filter(start=startForm, arrive = arriveForm, time=timeForm)
            # return querySet
        else:
            print(search.errors)
    return render(request, 'home.html', context)


def search_view(request,*args, **kwargs):
    context = {}
    return render(request, 'search.html', context)