from django.shortcuts import render, redirect, get_object_or_404

# Importing Cart model
from .models import Cart, CartItems

# Importing Product and Variation model
from store.models import Product, Variation

# Importing Django's exception for the case of cart has no products in it
from django.core.exceptions import ObjectDoesNotExist

# To fetch the session id
def _cart_id(request):
    cart= request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart
##

# To add the product based on the product id to the cart
def add_cart(request, product_id):
    # Getting the product using product id
    product = Product.objects.get(id = product_id)
    
    product_variation = []
    
    # Mainly for the variation the request method would be POST 
    if request.method == 'POST':
        #Product Validation for getting color and size
        for item in request.POST:
            key = item
            value = request.POST[key]
            # Mapping the key and value to the variation model
            try:
                # Instead of just passing the product object with all the 
                # project details we have to pass the variation of each 
                # products for adding the products into the cart
                variation = Variation.objects.get(
                    product = product,
                    variation_category__iexact = key, 
                    variation_value__iexact = value)
                ##
                
                product_variation.append(variation)
            except:
                pass
    ##
    
    # Adding the products selected to the cart
    try:
        cart = Cart.objects.get(cart_id = _cart_id(request)) #Card id had Session Id
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id = _cart_id(request)
            )
    cart.save()
    ##
    
    # To save multiple products with different variation to the carts
    # Checking if the Product with same variation exists
    is_cart_item_exists = CartItems.objects.filter(product = product, cart = cart).exists()
    
    # If the products with same variation exist only the count will get 
    # increased else new product list is created in the cart
    if is_cart_item_exists: 
        cart_item =  CartItems.objects.filter(product = product, cart  = cart)
        
        ex_list = []
        id =[]
        # Checking if the current variation already exists
        for item in cart_item:
            existing_variation = item.variation.all()
            ex_list.append(list(existing_variation))
            id.append(item.id)
        # If exist increase the quantity 
        if product_variation in ex_list:
            index = ex_list.index(product_variation)
            item_id = id[index]
            item = CartItems.objects.get(product = product, id = item_id)
            item.quantity = item.quantity + 1
            item.save()
            
        else:
            item = CartItems.objects.create(product = product, quantity = 1, cart = cart)
            # Looping through all the variation of each product
            if len(product_variation) > 0:
                #For seperation different combinations of variation
                item.variation.clear()
                item.variation.add(*product_variation)
            item.save()
    ##
    else:
        cart_item = CartItems.objects.create(product = product, quantity = 1, cart = cart,
            )
        # Looping through all the varaition of each product
        if len(product_variation) >0:
            #For seperation different combinations of variation
            cart_item.variation.clear()
            cart_item.variation.add(*product_variation)
            cart_item.save()
    return redirect('cart') #Redirecting back to cart after adding the items
##

# To remove the single product from the cart
def remove_cart(request, product_id,cart_item_id):
    cart = Cart.objects.get(cart_id = _cart_id(request))
    product = get_object_or_404(Product, id = product_id)
    
    try:
        cart_item = CartItems.objects.get(product = product, cart = cart, id = cart_item_id)
        if cart_item.quantity > 1:
            cart_item.quantity = cart_item.quantity - 1
            cart_item.save()
        else: 
            cart_item.delete()
    except:
        pass
    return redirect('cart')
##

# To remove the complete similar products from the cart
def remove_cart_complete(request, product_id, cart_item_id):
    cart = Cart.objects.get(cart_id = _cart_id(request))
    product = get_object_or_404(Product, id = product_id)
    cart_item = CartItems.objects.get(product = product, cart = cart, id = cart_item_id)
    cart_item.delete()
    return redirect('cart')
##

# To view the product detials in cart also calculating the tax with 2% and 
# calculating the grand total of the products
def cart(request, total =0, quantity=0, cart_items=None):
    tax = 0
    grand_total = 0
    try:
        cart = Cart.objects.get(cart_id = _cart_id(request))
        cart_items =  CartItems.objects.filter(cart= cart, is_active=True)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            quantity += cart_item.quantity
        # For tax calculation
        tax = ( 2 * total ) / 100
        grand_total = total + tax
    except ObjectDoesNotExist:
        pass
    
    context = {
        'total' : total,
        'quantity' :quantity,
        'cart_items' : cart_items,
        'tax' : tax,
        'grand_total' : grand_total
        }
    
    return render(request, 'cart/cart.html', context)
##

# For flushing the sessions created for the carts after the checkout is 
# rendered, so that the cart becomes empty for new session. This is impleted
# since the login specific session are not implement   
def checkout(request):
    request.session.flush() 
    return render(request, 'checkout/checkout.html')
##
    