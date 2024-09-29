from django.urls import path, include
from .models import Product
from .serializers import ProductSerializer
from .views import SignUpViewSet, LogoutViewSet, LoginViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'signup', SignUpViewSet, basename='signup')
router.register(r'login', LoginViewSet, basename='login')
router.register(r'logout', LogoutViewSet, basename='logout')

urlpatterns = [
    path('shop', include(router.urls)),

]