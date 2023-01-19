from django.db import models

# Importing Category Model
from category.models import Category

# To import the reverse
from django.urls import reverse

# To add the products in the store model and for displaying the products that 
# are uploaded into the application
class Product(models.Model):
    # Basic product details
    product_name = models.CharField(max_length = 50, unique = True)
    slug = models.SlugField(max_length = 100, unique = True)
    description = models.TextField(max_length =255 , blank =True)
    price = models.FloatField()
    image = models.ImageField(upload_to = 'photos/product')
    stock = models.IntegerField()
    is_available = models.BooleanField(default= True)
    
    # Incase if we delete the Category then all products belongs to that
    # Category should be deleted, this is done using models.CASCADE
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    ##
    
    # With the help of the reverser function we could able to  retrieve the url
    # from the urls.py file for to retreive the url like '/shoes/puma-ferari/'
    # for sending the Categoryname/productname to the cart
    def get_url(self):
        return reverse('product_details', args= [self.category.slug, self.slug])
    ##
    
    # For getting the product name
    def __str__(self):
        return self.product_name
    ##
##

# For seperating different criteria mainly helps in for product variation. 
# Variation in this demo project is only done using the colors and sizes of the
# products
class VariationManager(models.Manager):
    def colors(self):
        return super(VariationManager, self).filter(
            variation_category = 'color', is_active = True)
    def sizes(self):
        return super(VariationManager, self).filter(
            variation_category = 'size', is_active = True)
##
# Creating a variation tuple with Color and size variation
variation_category_choice = {
    ('color','color'),('size','size')
    }
##

# Variation model for different variations in the product selection like 
# different sizes, colors and sending the variation value to adding 
# the products into the cart with its variation details
class Variation(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    variation_category = models.CharField(
        max_length = 100, choices = variation_category_choice)
    variation_value = models.CharField(max_length = 100)
    is_active = models.BooleanField(default = True)
    created_date = models.DateTimeField(auto_now = True)
    
    # Trigerring the Variation Manager function 
    objects = VariationManager()
    ##
    def __str__(self):
        return self.variation_value
 ##   