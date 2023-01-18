from django.shortcuts import render

# Does nothing just for summary page view renderer
def checkout(request):
    return render(request, 'checkout/checkout.html')
##