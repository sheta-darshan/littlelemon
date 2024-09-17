from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Menu, Booking
from .serializers import MenuItemSerializer, BookingSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def msg(request):
    return Response({"message": "This view is protected"})

def index(request):
    return render(request, 'index.html', {})

class MenuItemsView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = MenuItemSerializer
    queryset = Menu.objects.all()

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]  # Add this line to ensure consistent permissions
    serializer_class = MenuItemSerializer
    queryset = Menu.objects.all()

class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
