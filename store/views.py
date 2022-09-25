from django.shortcuts import render
from .models import Product,ProductAttribute
from category.models import Category

def store(request):
    products = Product.objects.filter(is_available=True)
    category = Category.objects.all()
    product_attribute = ProductAttribute.objects.all()
    
    product_count = products.count()
    
    context = {
        'product': products,
        'product_attribute':product_attribute,
        'category':category,
        'product_count':product_count,
    }
    return render(request, 'Home_page/shop-grid.html', context)

def product_details(request,id):
    products = Product.objects.get(id=id)
   
    
    
    
    
    return render(request, 'Home_page/product_details.html',{'data':products})
