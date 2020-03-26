from django.shortcuts import render

from .models import Product

def list(request):
    products = Product.objects.all()

    context = {"products": products}

    return  render(request, 'products/index.html', context)
