from django.contrib import admin

# Importing the Account model here
from .models import Account

# Importing the UserAdmin to restrict the access of account details
from django.contrib.auth.admin import UserAdmin

# Class for Restricting the SuperUser account details
class AccountAdmin(UserAdmin):
    list_display = ('email', 'username', 'last_login', 'is_admin')
    
    # Other mandatory parameters
    filter_horizontal= ()
    list_filter = ()
    # Mainly protects the password non-editable
    fieldsets = ()
    

# For Registering the model for administration
admin.site.register(Account, AccountAdmin)