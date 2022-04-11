from django.shortcuts import render

from .models import Fly

# Create your views here.
def home_view(request):
    fly = Fly.objects.all()
    print(fly)
    context = {
        'fly':fly,
    }
    return render(request, 'home.html', context)