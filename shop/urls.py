from django.urls import path, include
from .models import Product
from .serializers import ProductSerializer
from .views import ProductList, SignUpViewSet, LogoutViewSet
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'product-list', ProductList, basename = 'productlist')
router.register(r'signup', SignUpViewSet, basename='signup')

urlpatterns = [
    path('products/', include(router.urls)),
    path('signup/', include(router.urls))

]