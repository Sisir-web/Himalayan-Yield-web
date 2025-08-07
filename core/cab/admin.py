from django.contrib import admin
from .models import Cab,CabBooking,Driver

# Register your models here.
admin.site.register(Cab)
admin.site.register(CabBooking)
admin.site.register(Driver)
