"""
Cart URL Configuration
"""
from django.urls import path

# Importing Views
from . import views
##

urlpatterns = [    
    # Url for Cart Page
    path('',views.cart, name='cart'),
    # Url for adding to cart Page
    path('add_cart/<int:product_id>/',views.add_cart, name='add_cart'),
    
]