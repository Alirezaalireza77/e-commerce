from rest_framework import generics, status, mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Cart, CartItem
from .serializers import CartItemSerializer, CartSerializer
from shop.models import Product
import uuid


class CartViewSet(mixins.DestroyModelMixin,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  GenericViewSet):
                  
    
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [AllowAny]


    def create(self, request, *args, **kwargs):
       user = request.user if request.user.is_authenticated else None
       cart, created = Cart.objects.get_or_create(user=user)
       serializer = self.get_serializer()
       return Response(serializer.data, status=status.HTTP_201_CREATED)
    


    def destroy(self, request, *args, **kwargs):
        user = request.user if request.user.is_authenticated else None
        try:
            cart = Cart.objects.get(user=user)
            cart.delete()
            return Response({'message': 'cart was deleted.'}, status=status.HTTP_200_OK)
        except:
            return Response({'message':'cart does not exist.'}, status=status.HTTP_404_NOT_FOUND)
        

    def get_queryset(self):
        user = self.request.user
        return Cart.objects.filter(user=user)
    

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)



class CartItemViewSet(mixins.CreateModelMixin,
                       mixins.UpdateModelMixin,
                         GenericViewSet):

    queryset = CartItem.objects.all()
    permission_classes = [AllowAny]
    serializer_class = CartItemSerializer


    def create(self, request, *args, **kwargs):
        cart_key = str(uuid.uuid4())
        user = request.user if request.user.is_authenticated else None
        cart, _ = Cart.objects.get_or_create(user=user, cart_key=cart_key)
        product = Product.objects.get(id=request.data.get('product_id'))
        data = {
            'cart': cart.id,
            'product': request.data.get('product_id'),
            'quantity': request.data.get('quantity', 1),
            'price': product.price,
        }
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.add_item(serializer.validated_data)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

    

    def update(self, request, *args, **kwargs):
        user = request.user if request.user.is_authenticated else None
        cart = Cart.objects.get(user=user)
        product = Product.objects.get(id=request.data.get('product_id'))
        data={
            'cart': cart.id,
            'product': request.data.get('product_id'),
            'quantity': request.data.get('quantity'),
            'price': product.price,
        }
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.remove_item(serializer.validated_data)
        return Response(serializer.data, status=status.HTTP_200_OK)
        


