from django.shortcuts import render
from .models import product

def product_detail(request):
    return render(request, 'store/product_detail.html')
