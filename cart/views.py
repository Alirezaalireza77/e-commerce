from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Cart, CartItem
from .serializers import CartItemSerializer, CartSerializer
from shop.models import Product


class CartItemView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        cart = Cart.objects.get(customer=request.user)
        product_id = request.data.get('product_id')
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product_id=product_id)
        quantity = request.data.get('quantity', 1)

        if not created:
            cart_item.quantity += 1
            cart_item.save()
        else:
            cart_item.quantity = quantity
            cart_item.price = cart_item.product.price
            cart_item.save()

        cart.calculate_total_price()
        serializer = CartItemSerializer(cart_item)
        return Response(serializer.data, status=status.HTTP_201_created)
        

    def delete(self, request, *args, **kwargs):
        cart_item_id = request.data.get('cart_item_id')
        quantity = request.data.get('quantity')
        try:
            cart_item = CartItem.objects.get(id=cart_item_id, cart__customer=request.user, quantity=quantity)
            if cart_item.quantity > 1:
                cart_item -= 1
                cart_item = cart_item.cart
                Cart.calculate_total_price()
                serializer = CartItemSerializer(cart_item)
                return Response(serializer.data, status = status.HTTP_200_OK)
            cart_item.delete()
            cart_item = cart_item.cart
            Cart.calculate_total_price()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except cart_item.DoesNotExist:
            return Response({"detail" : "cart item not found."}, status= status.HTTP_404_NOT_FOUND)
        

    def put(self, request, *args, **kwargs):
        cart_item_id = request.data.get('cart_item_id')
        quantity = request.data.get('quantity')
        try:
            cart_item = CartItem.objects.get(id=cart_item_id, cart__customer=request.user)
            if quantity is not None:
                cart_item.quantity = quantity
                cart_item.save()
                cart_item = cart_item.cart
                Cart.calculate_total_price()
                serializer = CartItemSerializer(cart_item)
                return Response(serializer.data, status=status.HTTP_200_OK)
        except cart_item.DoesNotExist:
            return Response ({"detail": "cart item not found"},status=status.HTTP_404_NOT_FOUND)
       
        
    def get_queryset(self):
        cart_item = CartItem.objects.filter(customer=self.request.user)
        return Product.objects.filter(cart_item__in=cart_item)


class CartItemListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        cart_items = CartItem.objects.filter(customer=request.user)
        serializer = CartSerializer(cart_items, many=True)
        return Response(serializer.data, status =status.HTTP_200_OK)