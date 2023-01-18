# For sending the response in the view need to import render 
# from django.shortcuts module
from django.shortcuts import render

# Importing product model
from store.models import Product

# To view all the products with it's details in the home page
def home(request):
    
    # To fetch all the products that are available
    products= Product.objects.all().filter(is_available = True)
    
    # Passing value from products into context for rendering
    context = {
        'products': products
        }
    
    
    return render(request, 'home.html', context)
##