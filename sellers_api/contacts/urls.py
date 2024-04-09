from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()

router.register(r'sellers-groups', views.SellerGruopsViewSet, basename='seller-groups') 
router.register(r'sellers-contacts', views.SellerContactsViewSet, basename='seller-contacts')

urlpatterns = [
    path(r'api/',include(router.urls)),
    path('api/sellers-contacts/<uuid:id>/<str:name>/', views.SellerContactNameViewSet.as_view({'get': 'list'}), name="sellers-contacts-name"),
    path('api/sellers-contacts/<uuid:id>/', views.SellerContactNameViewSet.as_view({'get': 'list'}), name="sellers-contacts-seller-id"),
    path('api/sellers-groups/<uuid:id>/<str:name>/', views.SellerGroupNameViewSet.as_view({'get': 'list'}), name="sellers-groups-name"),
    path('api/sellers-groups/<uuid:id>/', views.SellerGroupNameViewSet.as_view({'get': 'list'}), name="sellers-groups-seller-id"),
    path('api/sync-groups/', views.SincGroupsViewSet.as_view(), name="sellers-groups-sync")
]
