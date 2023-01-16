from django.contrib import admin

# Importing the Category model here
from .models import Category

# Importing UserAdmin for securing the password to read only
from django.contrib.auth.admin import UserAdmin

# Category Model
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'category_url': ('category_name',)}
    list_display = ('category_name', 'category_url')

# Registering the Category model
admin.site.register(Category, CategoryAdmin)


