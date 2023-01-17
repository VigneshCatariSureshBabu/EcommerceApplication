# Context-processor for counting the number of products that are added

# Importing the Cart and CartItem model from models
from .models import Cart, CartItems

from .views import _cart_id

# Function to count the products and return dynamically
# If the user is admin then it returns nothing else for each user it returns 
# the exact count 
def counter(request):
    cart_count = 0
    if 'admin' in request.path:
        return {}
    else: 
        try: 
            cart = Cart.objects.filter(cart_id = _cart_id(request))
            # To fetch just one property for counting the products
            cart_items = CartItems.objects.all().filter(cart = cart[:1])
            for cart_item in cart_items:
                cart_count = cart_count + cart_item.quantity
        except Cart.DoesNotExist:
            cart_count = 0
    return dict (cart_count = cart_count)