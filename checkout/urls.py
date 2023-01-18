"""
store URL Configuration
"""
from django.urls import path

# Importing Views
from . import views
##

urlpatterns = [    
    # Url for Checkout Page
    path('',views.checkout, name='checkout'),
    
]
 

