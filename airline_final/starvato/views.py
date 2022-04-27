from django.shortcuts import render, redirect

from .models import Airport, People
from .forms import FlyForm, Fly, BookingForm, Booking
from django.core.mail import send_mail
from airline_final.settings import EMAIL_HOST_USER

from rest_framework import viewsets
from .serialzers import *

# Create your views here.
def home_view(request):
    pending_list = Booking.objects.filter(status='pending')
    for element in pending_list:
        element.delete()
    all_airports = Airport.objects.all()
    flyForm = FlyForm()
    context = {
        'flyForm':flyForm,
        'all_airports':all_airports,
        }
    if request.method == 'POST':
        flyForm = FlyForm(request.POST)
        
        if flyForm.is_valid():
            people = request.POST.get('persone', '')
            filt = Fly.objects.filter(start=request.POST['start'], arrive=request.POST['arrive'], date=request.POST['date'], free_seats__gte = request.POST.get('persone', ''))
#             try: 
#               if request.POST['tipo']:
#                    filt_rit = Fly.objects.filter(start=request.POST['arrive'], arrive=request.POST['start'], date=request.POST['date_rit'], free_seats__gte = request.POST['persone'])
#                    try:
#                        if filt[0]:     
#                            pass
#                    except:
#                        context['noStart'] = True
#                    try:
#                        if filt_rit[0]:
#                            return search_view(request, filt, people, filt_rit)
#                    except:
#                        filt_rit = True
#                        context['noRit'] = True
#            except:
#                filt_rit = False
            try:
                if filt[0]:
                    
                    return search_view(request, filt, people,)
            except:
                context['noStart'] = True
    return render(request, 'home.html', context)


def search_view(request, filt, people):
    
#    filt_rit= str(filt_rit)
    recap = filt[0]
    context = {'filt':filt, 'recap':recap ,'people':people}
    return render(request, 'search.html', context)


#mancherebbe person per far prenotare piu' persone
def flyDetailView(request, id, people):
    fly = Fly.objects.get(id=id)
    booking_s = Booking.objects.filter(fly=fly)
    bookingForm = BookingForm()
    context = {
        'people':people,
        'fly':fly,
        'booking':BookingForm,
        'booking_s':booking_s,
    }
    if request.method == 'POST':
        bookingForm = BookingForm(request.POST)
        if bookingForm.is_valid():
            bookingForm.save()
            people -= 1
            booking_ls = Booking.objects.latest('id')
            booking_ls.status = 'pending'
            booking_ls.save()
            if people == 0:
                print('ciao')
                pending_list = Booking.objects.filter(status='pending')
                
                for book in pending_list:
                    
                    message_name = book.name
                    message_email_to_send = book.email
                    ticket = book.unique_id
                    seat = book.fly_seat
                    print(book)
                    send_mail(
                        'Grazie '+ message_name +' per la fiducia!, ecco a lei il suo ticket', #subject
                        'Ticket: '+ ticket + '\nposto a sedere ' + seat, # message
                        EMAIL_HOST_USER, 
                        [message_email_to_send])
                    return redirect('/success/')
            fly.free_seats -= 1
            fly.save()
            if people > 0:
                return redirect('flyDetail', fly.id, people)
        else:
            context['nullSearch'] = True
    return render(request, 'detail.html', context)

def success_view(request):
    pending_list = Booking.objects.filter(status='pending')
    context = {'pending_list':pending_list}
    for element in pending_list:
        element.status = 'completed'
        element.save()
    return render(request, 'success.html', context)

def find_p_view(request):
    context= {}
    if request.method == 'POST':
        code = request.POST['code']
        booking = Booking.objects.filter(unique_id = code)
        try:
            if booking[0]:
                print(booking[0])
                context['booking']=booking[0]
        except:
            context['error'] = True
    return render(request, 'find_p.html', context)

def mod_ticket_view(request, id):
    what_book = Booking.objects.get(id=id)
    bookingForm = BookingForm(instance=what_book)
    context = {'booking':bookingForm, 'confirmSave' : False}
    if request.method=='POST':
        bookingForm = BookingForm(request.POST, instance=what_book)
        if bookingForm.is_valid():
            bookingForm.save()
            context['confirmSave'] = True
    return render(request, 'mod_ticket.html', context)

def delete_ticket_view(request, id):
    what_book = Booking.objects.get(id=id)
    #what_book.fly.free_seats += 1
    what_book.delete()
    return render(request, 'delete.html', {})

class Fly_api(viewsets.ModelViewSet):
    queryset = Fly.objects.all()
    serializer_class = FlyAPI


class Booking_api(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingAPI


class Identify_api(viewsets.ModelViewSet):
    queryset = Identify.objects.all()
    serializer_class = IdentifyAPI

class Aircraft_api(viewsets.ModelViewSet):
    queryset = Aircraft.objects.all()
    serializer_class = AircraftAPI

class Airport_api(viewsets.ModelViewSet):
    queryset = Airport.objects.all()
    serializer_class = AirportAPI