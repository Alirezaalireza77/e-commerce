from django.shortcuts import render
from .models import Cart, CartItem
from shop.models import Product
from django.shortcuts import render, HttpResponse, redirect
from customer.models import Customer
from django.core.exceptions import ValidationError
# Create your views here.


def add_to_card(request, product_id):
    customer = Customer.objects.get(user=request.user)
    cart, created = Cart.objects.get_or_create(customer=customer)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product_id=product_id)

    if cart_item:
        if product_id in cart_item:
            product_id += 1
        else:
            product_id = 1
    else:
        product = Product.objects.get(pk=product_id)
        cart_item = CartItem.objects.create(
            cart = cart,
            product = product_id,
            quantity = 1,
            price = product.price,
        )
    cart.calculate_total_price()
    return redirect('cart')


def remove_from_cart(request, cart_item_id):
    cart_item = CartItem.objects.get(pk=cart_item_id)
    cart = cart_item.cart
    quantity = cart_item.quantity

    if cart_item:
        if len(quantity) > 1:
            quantity -= 1
        cart_item.delete()
    else:
        raise ValidationError('you have not any product in your cart to remove it.')

    cart.calculate_total_price()
    return redirect('cart')


def update_cart(request, cart_item_id, quantity):
    try:
        cart_item = CartItem.objects.get(pk=cart_item_id)
        cart = cart_item.cart
        cart_item.quantity = quantity
        cart_item.save()
        cart.calculate_total_price()
        return redirect('cart')
    except:
        return ValidationError

