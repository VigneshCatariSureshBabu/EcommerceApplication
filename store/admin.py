from django.contrib import admin

# Importing product model
from .models import Product

# Product Model
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'product_url': ('product_name',)}
    list_display = ('product_name', 'price', 'stock', 'category', 
                    'modified_date', 'is_available')

# Registering the Product model
admin.site.register(Product, ProductAdmin)