from django.db import models

# We have to import the Base User module from the Django authentication model
# and we are replacing the default login for admin and creating custom user 
# login
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Creating Account Manager model for validating the user input while 
# creating a account
class MyAccountManager(BaseUserManager):
    
    # For creating a normal user for login
    def create_user(self, first_name, last_name, 
                   username, email, password = None):
        # For user input validation and creating the user
        # The validation is done on the mandatory fields like email address
        # and user name
        if not email:
            raise ValueError("Please enter your Email Address")
        
        if not username:
            raise ValueError("Please enter a valid username for login")
        ##
        # Creating user and normalizing the email for case insensitive
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
            )
        user.set_password(password)
        user.save(using = self._db)
        return user
    ##
    
    # For the super user login with all the previledge
    def create_superuser(self, first_name, 
                        last_name, username, email, password):
            # Creating as an object with all the fields for user for storing it
            # in db
            user = self.create_user(
                email = self.normalize_email(email), 
                username = username, 
                password= password,
                first_name = first_name, 
                last_name = last_name, 
                )
            user.is_admin = True
            user.is_active = True
            user.is_staff = True
            user.is_superadmin = True
            user.save(using = self._db)
            ##
            return user
     ##   
            
# Creating Account model for customized user account and this class is used for
# the creation of the user account
class Account(AbstractBaseUser):
    
    # Basic User Details
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    email = models.EmailField(max_length = 50, unique = True)
    username = models.CharField(max_length = 50, unique = True)
    phone_number = models.CharField(max_length = 50)
    ##
    
    # Authentication Details
    date_joined = models.DateTimeField(auto_now_add = True)
    last_login = models.DateTimeField(auto_now_add = True)
    is_admin = models.BooleanField(default = False)
    is_staff = models.BooleanField(default = False)
    is_active = models.BooleanField(default = False)
    is_superadmin = models.BooleanField(default = False)
    ##
    
    # Ustomizing the login fields by replacing the username with 
    # the Email address
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    ##
    
    # Object for triggering the AccountManager so that the user accounts are 
    # created based on the Account Manager validation
    object = MyAccountManager()
    
    # Return email for authentiction
    def __str__(self):
        return self.email
    ##
    
    # For defining permission for admin user
    def has_perm(self, permission, object = None):
        return self.is_admin
    
    def has_module_perms(self, addLable):
        return True
    ##