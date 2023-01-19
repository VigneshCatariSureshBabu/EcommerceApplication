"""
store URL Configuration
"""
from django.urls import path

# Importing Views
from . import views
##

urlpatterns = [    
    # Url for Store Page
    path('',views.store, name='store'),
    ##
    # Url for different category listing
    path('category/<slug:category_slug>/',views.store,
         name='products_by_category'),
    ##
    # Url for opening the exact product
    path('category/<slug:category_slug>/<slug:product_slug>/',
         views.product_details, name='product_details'),
    ##
    # Url for product search functionality
    path('search/',views.search, name='search'),
    ##
]
 

