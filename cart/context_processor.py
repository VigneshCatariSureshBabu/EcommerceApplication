# Mainly Context-processor are used to make thing global so that we could use
# that for the rendering

# This Context-processor is for counting the number of products that are added
# in each cart 

# Importing the Cart and CartItem model from models
from .models import Cart, CartItems

# Importing the _cart_id function from the cart views
from .views import _cart_id

# Function to count the products and return dynamically
# If the user is admin then it returns nothing else for each user it returns 
# the exact count of number of quantity that are added in the cart
def counter(request):
    cart_count = 0
    # If the admin is logged in do nothing, but the login was not implemented 
    # at the moment since it a demo prototype
    if 'admin' in request.path:
        return {}
    ##
    
    else: 
        # For normal users fetch each product and quantity and gives the exact 
        # count 
        try: 
            cart = Cart.objects.filter(cart_id = _cart_id(request))
            # To fetch just one property for counting the products
            cart_items = CartItems.objects.all().filter(cart = cart[:1])
            for cart_item in cart_items:
                cart_count = cart_count + cart_item.quantity
        ##
        # In case of the cart is empty returns 0
        except Cart.DoesNotExist:
            cart_count = 0
        ##
    return dict (cart_count = cart_count)
##