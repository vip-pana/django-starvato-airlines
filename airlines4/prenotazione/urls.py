from django.urls import path
from .views import home_view, search_view, FlyDetailView

urlpatterns = [
    path('', home_view),
    path('search/', search_view, name='search'),
    path('ticket/<int:id>/', FlyDetailView, name='fly_detail'),
]
