from django.shortcuts import render, redirect, get_object_or_404

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
        cart_item.quantity = cart_item.quantity + 1
        cart_item.save()
    except CartItems.DoesNotExist:
        cart_item = CartItems.objects.create(
            product = product,
            quantity = 1,
            cart = cart
            )
        cart_item.save()
    return redirect('cart') #Redirecting back to cart after adding the items

# To remove the single product from the cart
def remove_cart(request, product_id):
    cart = Cart.objects.get(cart_id = _cart_id(request))
    product = get_object_or_404(Product, id = product_id)
    cart_item = CartItems.objects.get(product = product, cart = cart)
    if cart_item.quantity > 1:
        cart_item.quantity = cart_item.quantity - 1
        cart_item.save()
    else: 
        cart_item.delete()
        
    return redirect('cart')

# To remove the complete similar products from the cart
def remove_cart_complete(request, product_id):
    cart = Cart.objects.get(cart_id = _cart_id(request))
    product = get_object_or_404(Product, id = product_id)
    cart_item = CartItems.objects.get(product = product, cart = cart)
    cart_item.delete()
    return redirect('cart')
# To view the product detials in cart
def cart(request, total =0, quantity=0, cart_items=None):
    
    try:
        cart = Cart.objects.get(cart_id = _cart_id(request))
        cart_items =  CartItems.objects.filter(cart= cart, is_active=True)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            quantity += cart_item.quantity
        # For tax calculation
        tax = ( 2 * total ) / 100
        grand_total = total + tax
    except CartItems.ObjectNotExist:
        pass
    
    context = {
        'total' : total,
        'quantity' :quantity,
        'cart_items' : cart_items,
        'tax' : tax,
        'grand_total' : grand_total
        }
    
    return render(request, 'cart/cart.html', context)
  

    
    