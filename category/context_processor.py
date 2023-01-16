# Importing category model
from .models import Category

# To fetch all the category from the Category list
def menu_links(request):
    links= Category.objects.all()
    return dict(links=links)
