
from django.shortcuts import render
from store.models import Product
from category.models import Category
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):
    products = Product.objects.all()
    category = Category.objects.all()
    
    context = {
        'products': products,
        'categories':category,
    }
    
    return render(request, 'Home_page/index.html', context )

def errorpage(request):
    return (request,'Home_page/404.html')