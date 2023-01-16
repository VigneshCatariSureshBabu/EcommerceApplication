from django.db import models

# Importing the reverse module
from django.urls import reverse

# Creating category model

class Category(models.Model):
    category_name = models.CharField(max_length = 20, unique = True)
    slug = models.SlugField(max_length = 100, unique = True)
    description = models.TextField(max_length = 255, blank = True)
    category_image = models.ImageField(upload_to= 'photos/categories', blank = True)
    
    # Inorder to make the correction to the category in the plural form as
    # "categories" we have to change the Meta class and change the verbose_name
    
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        
    # For fetching the category url for each category
    def get_url(self):
        return reverse('products_by_category', args = [self.slug])
        
    # Return the Category name
    def __str__(self):
        return self.category_name
