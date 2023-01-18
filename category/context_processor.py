# Mainly Context-processor are used to make thing global so that we could use
# that for the rendering

# This Context-processor is for providing the links of categories that are 
# added to our application 

# Importing category model
from .models import Category

# To fetch all the category from the Category list and return and this is used
# in the navbar under All Category
def menu_links(request):
    links= Category.objects.all()
    return dict(links=links)
##