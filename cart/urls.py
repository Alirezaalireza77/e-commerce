from django.urls import path, include
from .views import CartItemViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'cart-items', CartItemViewSet, basename='cartitem')

urlpatterns = [
    path('',include(router.urls)),
]