from django.shortcuts import render

from .forms import SearchForm


def home_view(request, *args, **kwargs):
    search = SearchForm()
    context = {'search':search}\

    if request.method == 'POST':
        search = SearchForm(request.POST)
        print(search)
    return render(request, 'home.html', context)


