from django.shortcuts import render
from rest_framework import viewsets, mixins
from .serializers import OrderSerializer
from rest_framework.permissions import IsAuthenticated
from .models import Order

# Create your views here.

class OrderViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.ListModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.UpdateModelMixin,
                   viewsets.GenericViewSet):
    
    queryset = Order.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer


    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
    

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

