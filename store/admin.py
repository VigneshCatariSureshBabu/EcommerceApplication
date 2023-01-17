from django.contrib import admin

# Importing product model
from .models import Product, Variation

# Product Model
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('product_name',)}
    list_display = ('product_name', 'price', 'stock', 'category', 
                    'modified_date', 'is_available')


# Variation Model
class VariationAdmin(admin.ModelAdmin):
    list_display = ('product', 'variation_category', 'variation_value', 'is_active')
    list_editable = ('is_active',)
    list_filter = ('product', 'variation_category', 'variation_value', 'is_active')

# Registering the Product model
admin.site.register(Product, ProductAdmin)

#Registering the Variation model for storing in the backend
admin.site.register(Variation, VariationAdmin)