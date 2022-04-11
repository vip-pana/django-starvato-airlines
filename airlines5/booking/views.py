from readline import parse_and_bind
from django.shortcuts import redirect, render


from .forms import SearchForm, BookingForm
from .models import Fly, Search
from views_stuff.models import Underbanner


# Create your views here.
def home_view(request):
    underbanners = Underbanner.objects.all()
    flyForm = SearchForm()
    if request.method == 'POST':
        try:
            f_search = Search.objects.latest('id')
            if f_search.id == 1:
                flyForm = SearchForm(request.POST, instance=f_search)
        except:
            print('non esiste una ricerca')
            f_search = False
            flyForm = SearchForm(request.POST)
        if flyForm.is_valid():
            try:
                querySet = Fly.objects.filter(start = request.POST['start'], arrive=request.POST['arrive'], date=request.POST['date'])
                if querySet[0] and f_search:
                    return redirect('/search/')
                else:
                    flyForm.save()
                    return redirect('/search/')
            except:
                print('form valid ma non funge')
            

    context = {
        'flyForm':flyForm,
        'underbanners':underbanners,
    }
    return render(request, 'home.html', context)


def search_view(request):
    underbanners = Underbanner.objects.all()
    search = Search.objects.latest('id')
    querySet= Fly.objects.filter(start=search.start, arrive=search.arrive, date=search.date)
    context = {
        'underbanners':underbanners,
        'search':search,
        'querySet':querySet,
    }
    return render(request, 'search.html', context)


def flyDetailView(request, id):
    querySet = Fly.objects.get(id=id)
    booking = BookingForm()
    if request.method == 'POST':
        booking = BookingForm(request.POST)
        if booking.is_valid():
            booking.save()
            return redirect('/success/')
    context = {
        'querySet':querySet,
    }
    return render(request, 'detail.html', context)

def success_view(request):
    return render(request, 'success.html', {})
