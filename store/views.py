from django.shortcuts import render, get_object_or_404

# Importing product model
from .models import Product

# Importing category model
from category.models import Category

# To render the request to the store page
def store(request, category_slug = None):
    
    # Assigning None as default for Catagories and products
    categories = None
    products = None
    
    # If categories exist then we have to get the category else raise 404 error
    if category_slug != None:
        categories = get_object_or_404(Category, slug= category_slug)
        products = Product.objects.filter(category = categories, is_available = True)
        products_count = products.count()
    else:
        # To fetch all the products that are available
        products= Product.objects.all().filter(is_available = True)
        products_count = products.count()
    
    # Passing value from products into context for rendering
    context = {
        'products': products,
        'products_count' :products_count
        }
    return render(request, 'store/store.html',context)

# To view the product and its detials
def product_details(request, category_slug, product_slug):
    try: 
        single_product = Product.objects.get(category__slug = category_slug, slug=product_slug)
    except Exception as e:
        raise e
    # Passing value from products into context for rendering
    context = {
        'single_product': single_product,
        }
    return render(request,'store/product_details.html', context)