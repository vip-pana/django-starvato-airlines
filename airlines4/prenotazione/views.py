
from django.shortcuts import redirect, render



from .forms import SearchForm, BookingForm
from .models import Booking, Fly, Search



def home_view(request):
    search = SearchForm()
    if request.method == 'POST':
        try:
            first_search = Search.objects.latest('id')
            if first_search.id == 1:
                print('esiste una prima ricerca')
                search = SearchForm(request.POST, instance=first_search)
        except:
            print('non esiste una ricerca')
            first_search=False
            search = SearchForm(request.POST)
        if search.is_valid():
            try:
                querySet= Fly.objects.filter(Fly_start=request.POST['start'], Fly_arrive=request.POST['arrive'], Fly_day=request.POST['day'])
                if querySet[0]:
                    print(querySet)
                    if first_search:
                        return redirect('/search/')
                    else:
                        search.save()
                        return redirect('/search/')
            except:
                print('non ci sono risultati')
        else:
            print('non sono valido')
            
    else:
        print(search.errors)
    context = {
        'search':search,
    }
    return render(request, 'home.html', context)
    

def search_view(request):
    search = Search.objects.latest('id')
    querySet= Fly.objects.filter(Fly_start=search.start, Fly_arrive=search.arrive, Fly_day=search.day)
    fly_start = querySet[0].Fly_start
    context = {
        'search':search,
        'querySet': querySet,
        'fly_start': fly_start
    }
    return render(request, 'search_page.html', context)



def FlyDetailView(request, id):
    querySet = Fly.objects.get(id=id)
    prenotazioni = Booking.objects.all()
    lista_prenotazioni = []
    for i in range(len(prenotazioni)):
        lista_prenotazioni.append(int(prenotazioni[i].booking_code))
    posti = querySet.aircraft.seats
    booking = BookingForm()
    if request.method == 'POST':
        booking = BookingForm(request.POST or None)
        if booking.is_valid():
            booking.save()
            booking = BookingForm()
    context = {
        'querySet':querySet,
        'posti':posti,
        'booking':booking,
        'lista_prenotazioni':lista_prenotazioni,
        }
    return render(request, 'fly_detail_view.html', context)

  