from rest_framework import serializers
from .models import Cab,CabBooking,Driver

class CabSerializer(serializers.ModelSerializer):
   class Meta:
      model=Cab
      fields='__all__'

class CabBookingSerializer(serializers.ModelSerializer):
   class Meta:
      model=CabBooking
      fields='__all__'
   
class DriverSerializer(serializers.ModelSerializer):
   class Meta:
      model=Driver
      fields='__all__'

