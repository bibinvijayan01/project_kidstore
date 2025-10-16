from django.shortcuts import render, get_object_or_404
from store.models import Product

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id, is_available=True)
    
    context = {
        'product': product,
    }
    return render(request, 'store/product.html', context)
