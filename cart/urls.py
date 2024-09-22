from django.urls import path, include
from .views import CartItemListViewset, CartItemViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'cart-items', CartItemViewSet, basename='cartitem')
router.register(r'cart-list', CartItemListViewset, basename='cartlist')

urlpatterns = [
    path('',include(router.urls)),
]