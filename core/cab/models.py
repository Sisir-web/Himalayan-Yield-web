from django.db import models
from django.conf import settings


# Create your models here.
class Cab(models.Model):
   Cab_Types=models.CharField(max_length=20)
   cab_number=models.CharField(max_length=20)
   seats=models.IntegerField()
   is_available=models.BooleanField(default=True)

def __str__(self):
   return f"{self.Cab_Types}-{self.cab_number}"

class Driver(models.Model):
   name=models.CharField(max_length=50)
   phone=models.IntegerField()
   cab = models.OneToOneField(Cab,on_delete=models.SET_NULL,null=True)

def __str__(self):
   return self.name

from django.contrib.auth.models import User

class CabBooking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)  
    cab = models.ForeignKey(Cab, on_delete=models.SET_NULL, null=True)
    pickup_location = models.CharField(max_length=255)
    drop_location = models.CharField(max_length=255)
    journey_date = models.DateField()
    booking_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled')
    ], default='Pending')

    def __str__(self):
        return f"Booking #{self.id} - {self.user.username if self.user else 'Guest'}"
