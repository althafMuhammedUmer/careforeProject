
from django.shortcuts import render
from store.models import Product

# Create your views here.
def index( request):
    products_list = Product.objects.all().filter(is_available=True)
    
    context = {
        'products':products_list,
    }
    
    return render(request,'Home_page/index.html', context)
