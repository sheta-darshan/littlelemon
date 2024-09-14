from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Menu, Booking
from .serializers import MenuItemSerializer, BookingSerializer

def index(request):
    return render(request, 'index.html', {})

class MenuItemsView(generics.ListCreateAPIView):
    serializer_class = MenuItemSerializer
    queryset = Menu.objects.all()

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    serializer_class = MenuItemSerializer
    queryset = Menu.objects.all()
    
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    
    