from django.urls import path, include
from .views import SignUpViewSet, LogoutViewSet, LoginViewSet, ProductListViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'signup', SignUpViewSet, basename='signup')
router.register(r'login', LoginViewSet, basename='login')
router.register(r'logout', LogoutViewSet, basename='logout')
router.register(r'products', ProductListViewSet, basename='products')

urlpatterns = [
    path('shop/', include(router.urls)),

]
