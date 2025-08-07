from rest_framework.routers import DefaultRouter
from .import views
from .views import CabBookingViewset,CabViewset,DriverViewset
from django.urls import include,path

router = DefaultRouter()
router.register('cab',views.CabViewset,basename='cab')
router.register('cabbooking',views.CabBookingViewset,basename='cabbooking')
router.register('driver',views.DriverViewset,basename='driver')

urlpatterns=[
   path('',include(router.urls))
]
