def flyDetailView(request, id):
    fly = Fly.objects.get(id=id)
    saved_booking = Booking.objects.filter(fly=fly)
    booking = BookingForm() 
    person = Search.objects.get(id=1)
    context = {
        'querySet':fly,
        'booking':booking,
        'saved_booking':saved_booking,
        'person':person.person,
    }
    if request.method == 'POST':
        booking = BookingForm(request.POST)
        if booking.is_valid():
            message_name = request.POST['name']
            message_email_to_send = request.POST['email']
            ticket = request.POST['unique_id']
            seat = request.POST['airC_seat']
            send_mail(
                'Grazie '+ message_name +' per la fiducia!, ecco a lei il suo ticket', #subject
                'Ticket: '+ ticket + '\nposto a sedere ' + seat, # message
                EMAIL_HOST_USER, 
                [message_email_to_send],
            ) 

            booking.fields['status'].initial = 'pending' #non fa nulla
            booking.save()
            person.person = int(person.person) - 1
            fly.free_seats = fly.free_seats - 1
            fly.save()
            if int(person.person) > 0:
                person.save()
                return redirect('fly_detail', fly.id)
            return redirect('/success/')
        else:
            context['nullSearch'] = True

    return render(request, 'detail.html', context)