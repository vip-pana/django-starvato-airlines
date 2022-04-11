from django.urls import path
from .views import home_view, search_view, flyDetailView, success_view

urlpatterns = [
    path('', home_view, name='home'),
    path('search/', search_view, name='search'),
    path('ticket/<int:id>/', flyDetailView, name='fly_detail'),
    path('success/', success_view),
]