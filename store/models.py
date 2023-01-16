from django.db import models

# Importing Category Model
from category.models import Category

# For each store we have to create a product model
class Product(models.Model):
    product_name = models.CharField(max_length = 50, unique = True)
    product_url = models.SlugField(max_length = 100, unique = True)
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
    
    def __str__(self):
        return self.product_name
