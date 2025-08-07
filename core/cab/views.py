from django.shortcuts import render
from rest_framework import viewsets
from .models import Cab,CabBooking,Driver
from .serializer import CabBookingSerializer,CabSerializer,DriverSerializer

# Create your views here.
class CabViewset(viewsets.ModelViewSet):
   queryset=Cab.objects.all()
   serializer_class=CabSerializer

class CabBookingViewset(viewsets.ModelViewSet):
   queryset=CabBooking.objects.all()
   serializer_class=CabBookingSerializer

class DriverViewset(viewsets.ModelViewSet):
   queryset=Driver.objects.all()
   serializer_class=DriverSerializer
