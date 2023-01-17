from django.db import models

# Importing Category Model
from category.models import Category

# To import the reverse
from django.urls import reverse

# For each store we have to create a product model
class Product(models.Model):
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
    
    def get_url(self):
        return reverse('product_details', args= [self.category.slug, self.slug])
    
    def __str__(self):
        return self.product_name


# For seperating different criteria
class VariationManager(models.Manager):
    def colors(self):
        return super(VariationManager, self).filter(variation_category = 'color', is_active = True)
    def sizes(self):
        return super(VariationManager, self).filter(variation_category = 'size', is_active = True)
# Creating a tuple
variation_category_choice = {
    ('color','color'),('size','size')
    }

# For different variations in the product selection like different siz, color,etc.
class Variation(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    variation_category = models.CharField(max_length = 100, choices = variation_category_choice)
    variation_value = models.CharField(max_length = 100)
    is_active = models.BooleanField(default = True)
    created_date = models.DateTimeField(auto_now = True)
    
    objects = VariationManager()
    
    def __str__(self):
        return self.variation_value
    