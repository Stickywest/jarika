from django.urls import path
from .views import home, rooms, services, bookings

urlpatterns = [
    path('', home, name='home'),
    path('rooms/', rooms, name='rooms'),
    path('services/', services, name='services'),
    path('bookings/', bookings, name='bookings'),
    
]
