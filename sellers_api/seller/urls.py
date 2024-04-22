from django.urls import path, include

from rest_framework import routers

from . import views

router = routers.DefaultRouter()

router.register(r'sellers', views.SellerViewSet, basename='sellers')
router.register(r'sellers-users', views.UserViewSet, basename='sellers-users') 


urlpatterns = [
    path(r'api/',include(router.urls)),
    path('api/sellers-users/seller/<uuid:seller_id>/<str:username>', views.UserSellerIDViewSet.as_view({'get': 'list'}), name="sellers-users-seller-id"),
    path('api/sellers-users/seller/<uuid:seller_id>/', views.UserSellerIDViewSet.as_view({'get': 'list'}), name="sellers-users-seller-id-name"),
    path('api/seller-auth/', views.SellerAuthViewSet.as_view(), name="seller-auth")
]
