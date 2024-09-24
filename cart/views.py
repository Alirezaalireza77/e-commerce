# from rest_framework import generics, status, mixins
# from rest_framework.viewsets import GenericViewSet
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated, AllowAny
# from .models import Cart, CartItem
# from .serializers import CartItemSerializer, CartSerializer
# from shop.models import Product
# import uuid


# class CartItemViewSet(mixins.CreateModelMixin,
#                       mixins.DestroyModelMixin,
#                       mixins.UpdateModelMixin,
#                       mixins.RetrieveModelMixin,
#                       GenericViewSet
#                       ):
#     permission_classes = [AllowAny]
#     serializer_class = CartItemSerializer



#     def get_cart(self, request, *args, **kwargs):
#         if request.user.is_authenticated:
#             cart, created = Cart.objects.get_or_create(user=request.user)
#         else:
#             cart_key = request.data.get('cart_key')
#             if not cart_key:
#                 cart_key = str(uuid.uuid4())
#                 cart, created = Cart.objects.get_or_create(cart_key=cart_key)
#             cart,created = Cart.objects.get_or_create(cart_key=cart_key)
#         return cart
    


#     def create(self, request, *args, **kwargs):
#         cart = Cart.objects.get(user=request.user)
#         product_id = request.data.get('product_id')
#         cart_item, created = CartItem.objects.get_or_create(cart=cart, product_id=product_id)
#         quantity = request.data.get('quantity', 1)

#         if not created:
#             cart_item.quantity += 1
#             cart_item.save()
#         else:
#             cart_item.quantity = quantity
#             cart_item.price = cart.calculate_total_price()
#             cart_item.save()

#         cart.calculate_total_price()
#         serializer = CartItemSerializer(cart_item)
#         return Response(serializer.data, status=status.HTTP_201_created)
        

#     def destroy(self, request, *args, **kwargs):
#         cart_item_id = request.data.get('cart_item_id')
#         quantity = request.data.get('quantity')
#         try:
#             cart_item = CartItem.objects.get(id=cart_item_id, cart__user=request.user, quantity=quantity)
#             if cart_item.quantity > 1:
#                 cart_item -= 1
#                 cart_item = cart_item.cart
#                 Cart.calculate_total_price()
#                 serializer = CartItemSerializer(cart_item)
#                 return Response(serializer.data, status = status.HTTP_200_OK)
#             cart_item.delete()
#             cart_item = cart_item.cart
#             Cart.calculate_total_price()
#             return Response(status=status.HTTP_204_NO_CONTENT)
#         except cart_item.DoesNotExist:
#             return Response({"detail" : "cart item not found."}, status= status.HTTP_404_NOT_FOUND)
        

#     def update(self, request, *args, **kwargs):
#         cart_item_id = request.data.get('cart_item_id')
#         quantity = request.data.get('quantity')
#         try:
#             cart_item = CartItem.objects.get(id=cart_item_id, cart__user=request.user)
#             if quantity is not None:
#                 cart_item.quantity = quantity
#                 cart_item.save()
#                 cart_item = cart_item.cart
#                 Cart.calculate_total_price()
#                 serializer = CartItemSerializer(cart_item)
#                 return Response(serializer.data, status=status.HTTP_200_OK)
#         except cart_item.DoesNotExist:
#             return Response ({"detail": "cart item not found"},status=status.HTTP_404_NOT_FOUND)
       
        
        
# class CartItemListViewset(mixins.ListModelMixin,GenericViewSet):
#     permission_classes = [AllowAny]
#     serializer_class = CartSerializer
#     queryset = CartItem.objects.all()

#     def list(self, request, *args, **kwargs):
#         cart = Cart.objects.get(user=request.user)
#         queryset = self.get_queryset().filter(cart=cart)
#         serializer = CartItemSerializer(queryset, many=True)
#         return Response(serializer.data)
        


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
                  GenericViewSet):
                  
    
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [AllowAny]


    def create(self, request, *args, **kwargs):
       serializer = self.get_serializer()
       cart = serializer.create(user=request.user)
       return Response(serializer(cart).data, status=status.HTTP_201_CREATED)
    


    def destroy(self, request, *args, **kwargs):
        serializer = self.get_serializer()
        cart = serializer.destroy(user=request.user)
        return Response({'message':'cart was deleted.'})
    

class CartItemViewSet(mixins.CreateModelMixin,
                       mixins.UpdateModelMixin,
                         GenericViewSet):

    queryset = CartItem.objects.all()
    permission_classes = [AllowAny]


    def create(self, request, *args, **kwargs):
        cart_serializer = CartSerializer
        cart = cart_serializer.create(user=request.user)

        cartitem_serializer = CartItemSerializer
        product_id = request.data.get('product_id')
        quantity = request.data.get('quantity', 1)

        cartitem_serializer.add_item(cart, product_id, quantity)
        return Response(cartitem_serializer(cart).data, status=status.HTTP_201_CREATED)
    

    def update(self, request, *args, **kwargs):
        cart_serializer = CartSerializer
        cart = cart_serializer.create(user=request.user)

        cartitem_serializer = CartItemSerializer
        product_id = request.data.get('product_id')
        quantity = request.data.get('quantity', None)
        
        cartitem_serializer.remove_item(cart, product_id, quantity)
        return Response(cartitem_serializer(cart).data, status=status.HTTP_200_OK)

        