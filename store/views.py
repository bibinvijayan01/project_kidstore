from django.shortcuts import render, redirect
from .models import Product

def store(request):
    products = Product.objects.all()
    return render(request, 'store/store.html', {"products": products})

def add_to_cart(request, id):
    print("Product added:", id)
    return redirect('store')
