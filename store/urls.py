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
    
]
 

