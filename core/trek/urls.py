from django.urls import path,include
from rest_framework.routers import DefaultRouter
from trek.views import Trek,Itenary
from .import views

router = DefaultRouter()
router.register('trek',views.Trek,basename='trek')
router.register('itenary',views.Itenary,basename='itenary')

urlpatterns = [
    path('',include(router.urls)),
]
