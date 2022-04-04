airlines v.3.0

ho ricreato il tutto per tenerlo piu' pulito e ho usato un altro database perche' avevo incasinato quello prima

ho creato l'app prenotazione che possiede i models airports collegato con chiave esterna a fly,
fly usa il file forms.py per dare un form visibile al template,
viene tutto inserito nel context della views che renderizza home.html

il form e' visibile con le sue modifiche grazie al modulo di django installato a parte 'widget_tweaks'
che permette di modificare direttamente sul html

-capire come estrarre i dati utilizzando i widget_tweaks, senza e' fattibile ma con ho notato qualche problema

TO DO:
- estrarre i dati dal form di home.html
- pagina search dove vengono mostrati i dati filtrati su fly

MENO IMPORTANTE:
- creare una pagina di amministrazione per inserire dati non del superuser
-inserire gli under banners
- inserire carosello

_____________________________________________________________________________--
il form di ricerca base funziona quasi del tutto devo solo collegare come mettere
per farlo è un po un casino o creo la funzione dentro o metto nell'action che chiama la funzione o boh non ho capit


vedere urls per le app
vedere redirect


_______________________________________________________________________________-

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




