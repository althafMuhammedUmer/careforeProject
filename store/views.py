from django.shortcuts import render
from .models import Product, ProductGallery
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


def product_details(request, slug):
    product = Product.objects.get(slug=slug)
    product_gallery = ProductGallery.objects.filter(product__slug=product.slug)
    print(product_gallery)
    
    
    category = Category.objects.all()
    context = {
        'categories':category,
        'product':product,
        'product_gallery':product_gallery,
    }
    return render(request, 'Home_page/product.html', context)
