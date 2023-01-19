from django.shortcuts import render, get_object_or_404

# Importing product model
from .models import Product

# Importing category model
from category.models import Category

# Importing methods and CartItems model from Cart app
from cart.views import _cart_id
from cart.models import CartItems

# Importing paginator for restricting the number of products to be viewed in
# the store view
from django.core.paginator import Paginator

# Importing django's Q module for complex queries
from django.db.models import Q

# To render the request to the store page and restrict the number of products 
# to be displayed in the store page for easy viewing
def store(request, category_slug = None):
    
    # Assigning None as default for Catagories and products as initial value
    categories = None
    products = None
    ##
    
    # If categories exist then we have to get the category else raise 404 error
    if category_slug != None:
        categories = get_object_or_404(Category, slug= category_slug)
        products = Product.objects.filter(category = categories, 
                                          is_available = True)
        # Here the products to be displayed is restricted to 3 for demo pupose
        # by changing the value we could increase or decrease the number of
        # products to be viewed
        paginator = Paginator(products, 3)
        ##
        
        # Exact pagination of number of products to be stored here
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        products_count = products.count()
        ##
    else:
        # To fetch all the products that are available
        products= Product.objects.all().filter(
            is_available = True).order_by('id')
        ##
        
        # Here the products to be displayed is restricted to 3 for demo pupose
        # by changing the value we could increase or decrease the number of
        # products to be viewed
        paginator = Paginator(products, 3)
        ##
        
        # Exact pagination of number of products to be stored here
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        products_count = products.count()
        ##
    
    # Passing value from products into context for rendering
    context = {
        'products': paged_products,
        'products_count' :products_count
        }
    ##
    return render(request, 'store/store.html',context)
##

# To view the product detials into the html page
def product_details(request, category_slug, product_slug):
    try: 
        single_product = Product.objects.get(category__slug = category_slug, 
                                             slug=product_slug)
        # To check item already exist in the cart
        in_cart = CartItems.objects.filter(cart__cart_id = _cart_id(request), 
                                           product = single_product).exists()      
    except Exception as e:
        raise e
    # Passing value from products into context for rendering
    context = {
        'single_product': single_product,
        'in_cart' : in_cart
        }
    return render(request,'store/product_details.html', context)
##

# To search the product by its name
def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Product.objects.order_by('created_date').filter(
                # Need to search the product that matches the keyword using
                # Complex query
                Q(description__icontains = keyword) | 
                Q(product_name__icontains = keyword) | 
                Q(slug__icontains = keyword))
                ##
            products_count = products.count()
    context= {
        'products' : products,
        'products_count' : products_count
        
        }
           
            
    return render(request, 'store/store.html',context)
##