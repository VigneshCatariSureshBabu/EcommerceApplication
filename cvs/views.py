# For sending the response in the view need to import render 
# from django.shortcuts module
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')