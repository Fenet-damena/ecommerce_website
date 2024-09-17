from django.shortcuts import render, get_object_or_404
from .models import product

def product_detail(request, slug):
    products=get_object_or_404(product,slug=slug)
    return render (request,'store/product_detail.html',{'products':products})
