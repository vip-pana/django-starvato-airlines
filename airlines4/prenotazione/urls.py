from django.urls import path
from .views import home_view, search_view

urlpatterns = [
    path('', home_view),
    path('search/', search_view)
]
