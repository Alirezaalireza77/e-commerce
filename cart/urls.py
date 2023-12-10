from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart_summary, name='cart_summary'),
    path('', views.cart_add, name='cart_add'),
    path('', views.cart_delete , name='cart_delete'),
    path('', views.cart_update, name='cart_update'),
]