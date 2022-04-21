from django.shortcuts import redirect, render
from airlines5.settings import EMAIL_HOST_USER
from .forms import SearchForm, BookingForm
from .models import Booking, Fly, Search
from views_stuff.models import Underbanner

from django.core.mail import send_mail

# Create your views here.
def home_view(request):
    underbanners = Underbanner.objects.all()
    flyForm = SearchForm()
    context = {
        'flyForm':flyForm,
        'underbanners':underbanners,
        'iterator' : range(1, 11)
    }
    if request.method == 'POST':
        try:
            f_search = Search.objects.latest('id')
            if f_search.id == 1:
                flyForm = SearchForm(request.POST, instance=f_search)
        except:
            f_search = False
            flyForm = SearchForm(request.POST)
        if flyForm.is_valid():
            flyForm.save()
            last_save = Search.objects.latest('id')
            try:
                if last_save.have_return2:
                    print('ciao')
                    start_travel = Fly.objects.filter(start = request.POST['start'], arrive=request.POST['arrive'], date=request.POST['date'], free_seats__gte = request.POST['person'])
                    rit_travel = Fly.objects.filter(start = request.POST['arrive'], arrive=request.POST['start'], date=request.POST['date_rit'], free_seats__gte = request.POST['person'])
                    try:
                        if start_travel[0]:
                            print('esiste start')
                    except:
                        context['noAnd'] = True
                    try:
                        if rit_travel[0]:
                            print('esiste rit') 
                    except:
                        context['noRit'] = True
                    try:
                        if start_travel[0] and rit_travel[0]:
                            return redirect('/search/')
                    except:pass
            except: 
                try:
                    start_travel = Fly.objects.filter(start = request.POST['start'], arrive=request.POST['arrive'], date=request.POST['date'], free_seats__gte = request.POST['person'])
                    if start_travel[0]:
                        return redirect('/search/')
                except:
                    context['noAnd'] = True
    return render(request, 'home.html', context)


def search_view(request):
    underbanners = Underbanner.objects.all()
    search = Search.objects.latest('id')
    context = {
        'underbanners':underbanners,
        'search':search,
    }
    querySet= Fly.objects.filter(start=search.start, arrive=search.arrive, date=search.date, free_seats__gte = search.person)
    context['querySet'] = querySet
    return render(request, 'search.html', context)


def flyDetailView(request, id):
    fly = Fly.objects.get(id=id)
    saved_booking = Booking.objects.filter(fly=fly)
    booking = BookingForm() #per prenotare
    person = Search.objects.get(id=1) #persone totali che chiedono la prenotazione
    context = {
        'querySet':fly, #dati volo
        'booking':booking, #form prenotazione
        'saved_booking':saved_booking, #posti che non si possono toccare
        'person':int(person.person), #persone che chiedono la prenotazione
    }
    if request.method == 'POST':
        booking = BookingForm(request.POST)
        if booking.is_valid() and int(person.person)>0:
            booking.save()
            resave = Booking.objects.latest('id')
            resave.status = 'pending'
            resave.save()
            person.person = int(person.person) - 1
            person.save()
            if int(person.person) == 0:
                booking4message = Booking.objects.filter(status='pending')
                for element in booking4message:
                    message_name = element.name
                    message_email_to_send = element.email
                    ticket = element.unique_id
                    seat = element.airC_seat
                    send_mail(
                        'Grazie '+ message_name +' per la fiducia!, ecco a lei il suo ticket', #subject
                        'Ticket: '+ ticket + '\nposto a sedere ' + seat, # message
                        EMAIL_HOST_USER, 
                        [message_email_to_send],
                    )
                    element.status = 'completed'
                    element.save()

            fly.free_seats = fly.free_seats - 1 #questo si attiva quando lo status è complete
            fly.save()            
            if int(person.person) > 0:
                return redirect('fly_detail', fly.id)
            return redirect('/success/')
        else:
            context['nullSearch'] = True
    return render(request, 'detail.html', context)


# mi creo un array in cui inserisco indipendentemente le persone(oggetti) dentro fino a che person non va a 0
# quando le person vanno a 0 invio la mail a tutti le persone e gioco finito
# PROBLEMA, creare un array per l'invio delle persone, forse un model




def success_view(request):
    return render(request, 'success.html', {})



