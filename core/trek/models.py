from django.db import models

# Create your models here.
class Trek(models.Model):
   name=models.CharField(max_length=100)
   duration=models.CharField(max_length=50)
   price_per_person=models.DecimalField(max_digits=10,decimal_places=2)
   difficulty=models.CharField(max_length=20)
   description=models.TextField(max_length=1000)

class Itenary(models.Model):
   trek=models.ForeignKey(Trek,on_delete=models.CASCADE,related_name='itenary')
   day_number=models.IntegerField(default=1)
   description=models.TextField(max_length=1000)
