from django.urls import path
from .views import flyDetailView, home_view, search_view, success_view, find_p_view, mod_ticket_view, delete_ticket_view

urlpatterns = [
    path('', home_view, name='home'),
    path('search/', search_view, name='search'),
    path('ticket/<int:id>/<int:people>/return/<str:filt_rit>', flyDetailView, name='flyDetail'),
    path('success/', success_view),
    path('find/', find_p_view, name='find_p'),
    path('mod_ticket/<int:id>/', mod_ticket_view, name='mod_ticket'),
    path('delete/<int:id>', delete_ticket_view, name='delete'),
]