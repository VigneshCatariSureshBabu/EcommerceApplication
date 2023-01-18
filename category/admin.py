from django.contrib import admin

# Importing the Category model here
from .models import Category

# Importing UserAdmin for securing the password to read only
from django.contrib.auth.admin import UserAdmin

# Customing the Category fields in the admin panel mainly for easy viewing
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}
    list_display = ('category_name', 'slug')

# Registering the Category model to view the models in the admin panel
admin.site.register(Category, CategoryAdmin)


