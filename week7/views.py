
from django.shortcuts import render
from store.models import Product
from category.models import Category
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):
    products = Product.objects.all()
    category = Category.objects.all()
    
    context = {
        'product': products,
        'category':category,
    }
    
    return render(request, 'Home_page/index.html', context )