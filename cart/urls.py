from django.urls import path, include
from .views import CartItemViewSet, CartViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'cart-items', CartItemViewSet, basename='cartitem')
router.register(r'cart', CartViewSet, basename='cart')

urlpatterns = [
    path('',include(router.urls)),
]