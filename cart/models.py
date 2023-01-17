from django.db import models

# Importing Product Model
from store.models import Product, Variation

# Cart models for payment with Id and date
class Cart(models.Model):
    cart_id = models.CharField(max_length = 50, blank = True)
    date_added = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.cart_id

# Cart Items models for all the products
class CartItems(models.Model):
    # Incase if we delete the product then products belongs to that
    # particular cart should be deleted, this is done using models.CASCADE
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    # For storing the product variation
    variation = models.ManyToManyField(Variation, blank = True)
    
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default = True)
    
    def calculate_total(self):
        return self.product.price * self.quantity
    
    def __unicode__(self):
        return self.product