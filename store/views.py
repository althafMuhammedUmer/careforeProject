from django.shortcuts import render
from .models import Product
from category.models import Category

def store(request):
    products = Product.objects.filter(is_available=True)
    category = Category.objects.all()
    
    product_count = products.count()
    
    context = {
        'product': products,
        'category':category,
        'product_count':product_count,
    }
    return render(request, 'Home_page/shop-grid.html', context)
