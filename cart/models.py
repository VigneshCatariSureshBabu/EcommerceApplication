from django.db import models

# Importing Product Model, Variation model
from store.models import Product, Variation

# Cart models for getting storing the cart details like Cart Id and the date 
# the cart is added
class Cart(models.Model):
    cart_id = models.CharField(max_length = 50, blank = True)
    date_added = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.cart_id
##

# This model used to pick all the products from the specific cart and helps
# for performing variation when choosing the products with different criteria
class CartItems(models.Model):
    # Incase if we delete the product then products belongs to that
    # particular cart should be deleted, this is done using models.CASCADE
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    # For storing the product variation of each with similar variation
    variation = models.ManyToManyField(Variation, blank = True)
    ##
    
    # Making it ForeignKey so that this field could be used in other models
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    ##
    
    quantity = models.IntegerField()
    is_active = models.BooleanField(default = True)
    
    # For calculating the total in each cart
    def calculate_total(self):
        return self.product.price * self.quantity
    ##
    
    # Since we need the unicode of the product __unicode__ for rending 
    # an object which represents the strings
    def __unicode__(self):
        return self.product
    ##
##