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
    # For different category listing
    path('<slug:category_slug>/',views.store, name='products_by_category'),
    # For opening the exact product
    path('<slug:category_slug>/<slug:product_slug>/',views.product_details, name='product_details'),
]
 
