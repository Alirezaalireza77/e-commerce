# from rest_framework import serializers
# from .models import Cart, CartItem
# from shop.models import Product

# class CartItemSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CartItem
#         fields = ['cart', 'product', 'quantity', 'price']



#     def add_item(self, validated_data):
#         cart = validated_data.get('cart')
#         product = Product.objects.get(id=validated_data.get('product_id'))
#         cart_item, created = CartItem.objects.get_or_create(
#             cart=cart,
#             product=product,
#             defaults={'price': product.price, 'quantity': validated_data.get('quantity')}
#         )

#         if not created:
#             cart_item.quantity += validated_data('quantity', 1)
#             cart_item.save()
#             cart_item.cart.calculate_total_price()
#         cart.calculate_total_price()


    
#     def remove_item(self, validated_data):
#         cart_item_id = validated_data.get('cart_item_id')
#         quantity = validated_data.get('quantity')

#         try:
#             cart_item = CartItem.objects.get(id=cart_item_id, quantity=quantity)
#             if quantity > 1:
#                 quantity -= 1
#                 cart_item.save()
#                 cart_item.cart.calculate_total_price()
#             cart_item.delete()
#         except:       
#             cart_item.DoesNotExist
#             raise serializers.ValidationError('cart item does not exist.')
                
        

# class CartSerializer(serializers.ModelSerializer):
#     items = CartItemSerializer(many=True, source='item', read_only=True)
#     class Meta:
#         model = Cart
#         fields = ['user', 'created_at', 'total_amount', 'cart_key', 'items']
#         read_only_fiels = ['user']


#     def total_amount(self, obj):
#         return obj.calculate_total_price()


#     def create(self, user):
#         user = user if user.is_authenticated else None
        
#         cart, created = Cart.objects.get_or_create(user=user)
#         return cart
    

#     def destroy(self, user):
#         user = user if user.is_authenticated else None
#         cart = Cart.objects.get(user=user)

#         if cart:
#             cart.delete()
#         serializers.ValidationError('cart does not exist.')   
        


from rest_framework import serializers
from .models import Cart, CartItem
from shop.models import Product
import uuid

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['cart', 'product', 'quantity', 'price']


    def validate(self, data):
        product_id = data.get('product_id')
        try:
            product = Product.objects.get(id=product_id)
        except product.DoesNotExist:
            raise serializers.ValidationError('product does not exist.')

        quantity = data.get('quantity', 1)
        if quantity < 1:
            raise serializers.ValidationError('quantity must be atleast 1.')
        return data
    

    def create(self, validated_data):
        cart = validated_data('cart')
        product = validated_data('product')
        quantity = validated_data('quantity')
        
        cart_item, created = CartItem.objects.get_or_create(cart=cart,
                                                            product=product,
                                                            defaults={'quantity': quantity,
                                                                      'price':product.price})
        if not created:
            cart_item.quantity = quantity
            cart_item.save()

        cart_item.cart.calculate_total_price()
        return cart_item
    

    def update(self, instance, validated_data):
        quantity = validated_data.get('quantity', instance.quantity)
        if quantity > 0:
            instance.quantity = quantity
            instance.save()
        else:
            instance.delete()

        instance.cart.calculate_total_price()
        return instance
    


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, source='item', read_only=True)
    class Meta:
        model = Cart
        fields = ['user','created_at', 'total_amount', 'cart_key', 'items']
        read_only_fields = ['user']

    def create(self, validated_data):
        user = validated_data.get('user', None)
        if user is None or not user.is_authenticated:
            cart_key = validated_data.get('cart_key')
            if not cart_key:
                raise serializers.ValidationError('cart-key does not exist.')
            cart, created = Cart.objects.get_or_create(cart_key=cart_key)
        cart, created = Cart.objects.get_or_create(user=user)
        return cart
    

    def update(self, instance, validated_data):
        return instance

        