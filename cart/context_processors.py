from .cart import Cart

# this makes that Cart be available in all of my project
def cart(request):
    return {'cart': Cart(request)}