from django.db import models

# Create your models here.
class Product(models.Model):
   name=models.CharField(max_length=50)
   description=models.TextField(max_length=50,blank=True)
   price=models.DecimalField(max_digits=10,decimal_places=2)
   is_available=models.BooleanField(default=True)

class Order(models.Model):
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    delivery_address = models.TextField()
    message = models.TextField(blank=True)
    ordered_at = models.DateTimeField(auto_now_add=True)
    is_fulfilled = models.BooleanField(default=False)
