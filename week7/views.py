
from django.shortcuts import render
from store.models import Product,Banner,ProductAttribute
from category.models import Category
from django.contrib.auth.decorators import login_required


# Create your views here.
# @login_required(login_url='login')
def home(request):
    data=Product.objects.filter(is_featured = False).order_by('-id')

    banner = Banner.objects.all()
    # category = Category.objects.all()
    
    
    
    context = {
           
        'product': data,
        'banner': banner,
        # 'category':category,
        
    }
    
    return render(request, 'Home_page/index.html', context )