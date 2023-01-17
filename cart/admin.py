from django.contrib import admin
# Importing Cart model
from .models import Cart, CartItems



# Registering the Cart models
admin.site.register(Cart)
admin.site.register(CartItems)