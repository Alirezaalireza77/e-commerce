from django.urls import path, include
from .views import OrderViewSet
from rest_framework.routers import DefaultRoutere

router = DefaultRoutere()
router.register(r'order', OrderViewSet, basename='order')
urlpatterns = [
    path('order/', include(router.urls)),
]