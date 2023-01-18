from django.contrib import admin

# Importing Cart model
from .models import Cart, CartItems
##

# Customing the Cart field in the admin panel mainly for easy viewing
class CartAdmin(admin.ModelAdmin):
    list_display = ('cart_id', 'date_added')

class CartItemsAdmin(admin.ModelAdmin):
    list_display = ('product', 'cart', 'quantity', 'is_active')
##

# Registering the Cart models to view the models in the admin panel
admin.site.register(Cart, CartAdmin)
admin.site.register(CartItems, CartItemsAdmin)
##