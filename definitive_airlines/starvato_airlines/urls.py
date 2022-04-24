from django.urls import path
from .views import flyDetailView, home_view, search_view, success_view, find_p_view

urlpatterns = [
    path('', home_view, name='home'),
    path('search/', search_view, name='search'),
    path('ticket/<int:id>/<int:people>', flyDetailView, name='flyDetail'),
    path('success/', success_view),
    path('find/', find_p_view, name='find_p')
]