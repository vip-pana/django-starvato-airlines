from django.shortcuts import render, HttpResponse

# Create your views here.
def homepage_view(request, *args, **kwargs):
    return render(request, 'homepage/homepage.html', {})