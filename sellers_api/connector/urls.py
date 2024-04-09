from django.urls import path, include

from rest_framework import routers

from . import views

router = routers.DefaultRouter()

router.register(r'connectors', views.ConnetorsViewSet, basename='connectors')
router.register(r'sellers-connectors', views.SellerConnectorsViewSet, basename='sellers-connectors') 

urlpatterns = [
    path(r'api/',include(router.urls))
]