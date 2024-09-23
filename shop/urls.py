from django.urls import path, include
from .models import Product
from .serializers import ProductSerializer
from .views import ProductList, SignUpViewSet, LogoutViewSet
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'product-list', ProductList, basename = 'productlist')


urlpatterns = [
    path('products/', include(router.urls)),
    # path('about/', views.about, name='about'),
    # path('api/login/', obtain_auth_token, name='login'),
    # path('api/logout/', LogoutViewSet.as_view(), name='logout'),
    # path('api/products/<int:pk>', ProductListViewSet, name='product'),
    # path('api/signup/', SignUpViewSet.as_view(), name='signup'),
]