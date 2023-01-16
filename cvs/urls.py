"""
cvs URL Configuration
"""
from django.contrib import admin
from django.urls import path, include

# Importing Views
from . import views
##

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Url for Home Page
    path('',views.home, name='home'),
    ##
    # Url for Store Page
    path('store/',include('store.urls')),
    ##
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # To add the media URL
 

