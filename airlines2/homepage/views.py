from django.shortcuts import render

from .models import Airport, UnderBanner

# Create your views here.

def homepage_view(request, *args, **kwargs):
    airports = Airport.objects.all()
    under_banners = UnderBanner.objects.all()
    context = {
        'airports': airports,
        'under_banners':under_banners
    }
    return render(request, 'homepage.html', context)

def aggiungi_dati(request):
    pass