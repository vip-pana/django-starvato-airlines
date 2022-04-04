
from django.shortcuts import render

from prenotazione.models import Fly

from .forms import SearchForm


def home_view(request, *args, **kwargs):
    search = SearchForm()
    context_home = {'search':search}

    if request.method == 'POST':
        search = SearchForm(request.POST)
        if search.is_valid():
            startForm = request.POST['start']
            arriveForm = request.POST['arrive']
            timeForm = request.POST['time']
            querySet = Fly.objects.filter(start=startForm, arrive = arriveForm, time=timeForm)
            try:
                if querySet[0]:
                    search_context = {
                        'querySet':querySet,
                        'search': search
                    }
                    if request.method == 'POST':
                        search = SearchForm(request.POST)
                        if search.is_valid():
                            startForm = request.POST['start']
                            arriveForm = request.POST['arrive']
                            timeForm = request.POST['time']
                            querySet = Fly.objects.filter(start=startForm, arrive = arriveForm, time=timeForm)
                            print(querySet)
                    return render(request, 'search.html', search_context)
            except:
                print('nessun risultato')
        else:
            print(search.errors)
    return render(request, 'home.html', context_home)


def search_view(request,*args, **kwargs):
    search = SearchForm()
    search_context = {
        'querySet':args[0],
        'search': search
    }
    print('ciao')
    return render(request, 'search.html', search_context)