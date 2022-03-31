from django.shortcuts import render

from .models import Airport, UnderBanner
from .forms import FlyForm

# Create your views here.

def homepage_view(request, *args, **kwargs):
    airports = Airport.objects.all()
    under_banners = UnderBanner.objects.all()
    
    if request.method == 'post':
        result = request.POST
        
    context = {
        'airports': airports,
        'under_banners':under_banners
    }
    return render(request, 'homepage.html', context)

def search_view(request, *args, **kwargs):
    flyForm = FlyForm()
    if request.method == 'POST':
        flyForm = FlyForm(request.POST)
        if flyForm.is_valid():
            print(flyForm.cleaned_data)
        else:
            print(flyForm.errors)
    context = {
        'flyForm' : flyForm
    }
    return render(request, 'search.html', context)