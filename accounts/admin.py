from django.contrib import admin

# Importing the Account model 
from .models import Account

# Importing the UserAdmin to restrict the access of account details
from django.contrib.auth.admin import UserAdmin

# Class for Restricting the SuperUser account details
class AccountAdmin(UserAdmin):
    list_display = ('email', 'username', 'last_login', 'is_admin')
    
    # Other mandatory parameters for filtering
    filter_horizontal= ()
    list_filter = ()
    ##
    
    # Mainly protects the password non-editable so that the user passwords are
    # read-only
    fieldsets = ()
    ##  
##

# For Registering the model to view the models in the admin panel
admin.site.register(Account, AccountAdmin)
##