from django.shortcuts import render

# Create your views here.

from .models import Room, Service, Booking

from django.shortcuts import render
from .models import Room, Service

def home(request):
    featured_rooms = Room.objects.all()[:3]  # Get first 3 rooms as featured
    services = Service.objects.all()[:3]  # Get first 3 services as featured
    return render(request, 'hotel/home.html', {'rooms': featured_rooms, 'services': services})


def rooms(request):
    rooms = Room.objects.all()
    return render(request, 'hotel/rooms.html', {'rooms': rooms})

def services(request):
    services = Service.objects.all()
    return render(request, 'hotel/services.html', {'services': services})

def bookings(request):
    bookings = Booking.objects.all()
    return render(request, 'hotel/bookings.html', {'bookings': bookings})
