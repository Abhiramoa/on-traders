from django.shortcuts import render
from .models import Product
def home(request):
    return render(request, 'shop/index.html')
def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop/product_list.html', {'products': products})

