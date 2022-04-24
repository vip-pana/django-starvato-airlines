from enum import unique
from django.shortcuts import render, redirect
from .models import Airport
from .forms import FlyForm, Fly, BookingForm, Booking
from django.core.mail import send_mail
from definitive_airlines.settings import EMAIL_HOST_USER

# Create your views here.
def home_view(request):
    all_airports = Airport.objects.all()
    flyForm = FlyForm()
    context = {
        'flyForm':flyForm,
        'all_airports':all_airports,
        }
    if request.method == 'POST':
        flyForm = FlyForm(request.POST)
        if flyForm.is_valid():
            people = request.POST['persone']
            filt = Fly.objects.filter(start=request.POST['start'], arrive=request.POST['arrive'], date=request.POST['date'], free_seats__gte = request.POST['persone'])
            try:
                if filt[0]:
                    return search_view(request, filt, people)
            except:
                context['noStart'] = True
    return render(request, 'home.html', context)


def search_view(request, filt, people):
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
            if people == 0:
                pending_list = Booking.objects.filter(status='pending')
                for book in pending_list:
                    message_name = book.name
                    message_email_to_send = book.email
                    ticket = book.unique_id
                    seat = book.fly_seat
                    send_mail(
                        'Grazie '+ message_name +' per la fiducia!, ecco a lei il suo ticket', #subject
                        'Ticket: '+ ticket + '\nposto a sedere ' + seat, # message
                        EMAIL_HOST_USER, 
                        [message_email_to_send],)
                    book.status = 'completed'
                    book.save()
            fly.free_seats -= 1
            fly.save()
            if people > 0:
                return redirect('flyDetail', fly.id, people)
            return redirect('/success/')
        else:
            context['nullSearch'] = True
    return render(request, 'detail.html', context)

def success_view(request):
    context = {}
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