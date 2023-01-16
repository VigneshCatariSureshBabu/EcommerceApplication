from django.shortcuts import render

# Importing product model
from .models import Product

# To render the request to the store page
def store(request):
    # To fetch all the products that are available
    products= Product.objects.all().filter(is_available = True)
    
    products_count = products.count()
    
    # Passing value from products into context for rendering
    context = {
        'products': products,
        'products_count' :products_count
        }
    return render(request, 'store/store.html',context)
