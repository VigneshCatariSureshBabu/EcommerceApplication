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
    # Url for removing single product from the cart Page
    path('remove_cart/<int:product_id>/<int:cart_item_id>/',views.remove_cart, name='remove_cart'),
    # Url for removing complete products from the cart Page
    path('remove_cart_complete/<int:product_id>/<int:cart_item_id>/',views.remove_cart_complete, name='remove_cart_complete'),\
    # Url for checkout page after the cart page    
    path('checkout/', views.checkout, name = 'checkout')
    
]