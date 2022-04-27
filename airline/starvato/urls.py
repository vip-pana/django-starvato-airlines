from django.db import router
from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'booking', Booking_api)
router.register(r'identify', Identify_api)
router.register(r'airport', Airport_api)
router.register(r'aircraft', Aircraft_api)
router.register(r'fly', Fly_api)



urlpatterns = [
    path('api', include(router.urls)),
    path('api_auth', include('rest_framework.urls', namespace='rest_framework')),
    path('', home_view, name='home'),
    path('search/', search_view, name='search'),
    path('ticket/<int:id>/<int:people>', flyDetailView, name='flyDetail'),
    path('success/', success_view),
    path('find/', find_p_view, name='find_p'),
    path('mod_ticket/<int:id>/', mod_ticket_view, name='mod_ticket'),
    path('delete/<int:id>', delete_ticket_view, name='delete'),
]