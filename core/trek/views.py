from django.shortcuts import render
from rest_framework import viewsets
from .models import Trek,Itenary
from .serializer import TrekSerializer,ItenarySerializer

# Create your views here.
class Trek(viewsets.ModelViewSet):
   queryset=Trek.objects.all()
   serializer_class=TrekSerializer

class Itenary(viewsets.ModelViewSet):
   queryset=Itenary.objects.all()
   serializer_class=ItenarySerializer
