
from django.shortcuts import redirect, render

from prenotazione.models import Fly

from .forms import SearchForm
from .models import Airport, SearchFly


def home_view(request, *args, **kwargs):#devo richiamare gli aerei perche search form non va piu bene
    
    search = SearchForm()
    
    airports = Airport.objects.all()
    context_home = {'search':search,
                    'airports':airports,
    }

    if request.method == 'POST':
        
        search = SearchForm(request.POST)
        print('ciao')
        if search.is_valid():
            startForm = request.POST['start']
            arriveForm = request.POST['arrive']
            timeForm = request.POST['time']
            querySet = Fly.objects.filter(start=startForm, arrive = arriveForm, time=timeForm)

            try:
                if querySet[0]:
                    search.save()
                    return redirect('/search/')
            except:
                print('nessun risultato')
        else:
            
            print(search.errors)
    return render(request, 'home.html', context_home)


def search_view(request,*args, **kwargs):
    search = SearchForm()
    searchFly = SearchFly()
    searcher = SearchFly.objects.latest('id')
    print(searcher)
    if request.method == 'POST':
        search = SearchForm(request.POST)
        print(search)
        if search.is_valid():
            startForm = request.POST['start']
            arriveForm = request.POST['arrive']
            timeForm = request.POST['time']
            querySet = Fly.objects.filter(start=startForm, arrive = arriveForm, time=timeForm)

    search_context = {
        'search': search,
        'searchFly': searchFly,
    }
    print('ciao')
    return render(request, 'search.html', search_context)