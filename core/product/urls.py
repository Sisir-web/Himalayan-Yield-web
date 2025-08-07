from django.urls import path,include
from rest_framework.routers import DefaultRouter
from product.views import Product,Order
from .import views

router = DefaultRouter()
router.register('product',views.Product,basename='product')
router.register('order',views.Order,basename='order')

urlpatterns = [
    path('',include(router.urls)),
]
