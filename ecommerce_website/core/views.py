from django.shortcuts import render
from store.models import product

def fontpage(request):
    products = product.objects.all()[:6]  
    return render(request, 'core/fontpage.html', {
        'products': products
    })

def about(request): 
    return render(request, 'core/about.html')
