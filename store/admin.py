from django.contrib import admin

# Importing product model
from .models import Product, Variation

# Customing the Product field in the admin panel mainly for easy viewing
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('product_name',)}
    list_display = ('product_name', 'price', 'stock', 'category', 
                    'modified_date', 'is_available')
##

# Customing the Variation field in the admin panel mainly for easy viewing
class VariationAdmin(admin.ModelAdmin):
    list_display = ('product', 'variation_category', 'variation_value', 'is_active')
    list_editable = ('is_active',)
    list_filter = ('product', 'variation_category', 'variation_value', 'is_active')
##

# Registering the Product and Product Admin models to view the models in the admin panel
admin.site.register(Product, ProductAdmin)

# Registering the Variation and Variation Admin models to view the models in the admin panel
admin.site.register(Variation, VariationAdmin)