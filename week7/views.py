
from django.shortcuts import render
from store.models import Product,HomeBanner
from category.models import Category
from django.contrib.auth.decorators import login_required



# Create your views here.

def home(request):
    products = Product.objects.all()
    category = Category.objects.all()
    banner = HomeBanner.objects.get()
    
    context = {
        'products': products,
        'categories':category,
        'banner': banner,
    }
    
    return render(request, 'Home_page/index.html', context )

def errorpage(request):
    return (request,'Home_page/404.html')