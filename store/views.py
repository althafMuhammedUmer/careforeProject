from email.mime import image
from django.shortcuts import render
from .models import Product,ProductAttribute
from category.models import Category,Color


def store(request):
    # products = Product.objects.all() 
    products=Product.objects.all()
    category = Category.objects.all()
    product_attribute = ProductAttribute.objects.all()
    
    
    
    
    CatId = request.GET.get('categories')
    ColorId = request.GET.get('color')
    if CatId:
         products=Product.objects.filter(Category=CatId)
         
    elif ColorId:
        products = Product.objects.filter(productattribute__color=ColorId)
        
    else:
        products=Product.objects.all()
        
    
    
   
    
        
   
   
    
    product_count = Product.objects.count()
    
    context = {
        'product': products,
        'category':category,
        'product_count':product_count,
        'product_attribute':product_attribute,
        
    }
    return render(request, 'Home_page/shop-grid.html', context)

def product_details(request,slug,id):
    products = Product.objects.get(id=id)
   
    
    
    
    
    return render(request, 'Home_page/product_details.html',{'data':products})
