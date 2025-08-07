from django.shortcuts import render
from .models import Product,Order
from .serializer import ProductSerializer,OrderSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets


# Create your views here.
class Product(viewsets.ModelViewSet):
   queryset=Product.objects.all()
   serializer_class=ProductSerializer

class Order(viewsets.ModelViewSet):
   queryset=Order.objects.all()
   serializer_class=OrderSerializer
