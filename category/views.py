from category.models import Category
from store.models import Product
from django.shortcuts import render


# Create your views here.

def store(request):
    products = Product.objects.filter(is_available=True)
    links = Category.objects.all()  # fetch all categories

    context = {
        'products': products,
        'links': links,  # match your template
        'product_count': products.count(),
    }
    return render(request, 'category/girls.html', context)
