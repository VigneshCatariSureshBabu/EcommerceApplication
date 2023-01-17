from django.shortcuts import render, redirect

# Importing Cart model
from .models import Cart, CartItems

# Importing Product model
from store.models import Product

# To fetch the session id
def _cart_id(request):
    cart= request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

# To add the product to the cart
def add_cart(request, product_id):
    # Storing the product Id into the cart
    product = Product.objects.get(id = product_id)
    try:
        cart = Cart.objects.get(cart_id = _cart_id(request)) #Card id had Session Id
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id = _cart_id(request)
            )
    cart.save()
    
    # To save multiple product and combine all carts
    try: 
        cart_item =  CartItems.objects.get(product = product, cart  = cart)
        cart_item.quantity += 1
        cart_item.save()
    except CartItems.DoesNotExist:
        cart_item = CartItems.objects.create(
            product = product,
            quantity = 1,
            cart = cart
            )
        cart_item.save()
    return redirect('cart') #Redirecting back to cart after adding the items

# To view the product detials in cart
def cart(request):
    total = 0
    quantity = 0
    try:
        cart = Cart.objects.get(cart_id = _cart_id(request))
        cart_items =  CartItems.objects.filter(cart= cart, is_active=True)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            quantity += cart_item.quantity
    except CartItems.ObjectNotExist:
        pass
    
    context = {
        'total' : total,
        'quantity' :quantity,
        'cart_items' : cart_items
        }
    
    return render(request, 'cart/cart.html', context)
  
