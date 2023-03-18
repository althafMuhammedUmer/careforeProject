
from django.shortcuts import render
from store.models import Product,HomeBanner
from Accounts.models import UserProfile
from category.models import Category
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404



# Create your views here.

def home(request):
    products = Product.objects.all()
    category = Category.objects.all()
    banner = HomeBanner.objects.get()
    user = request.user
    print(user, "this is current user")
    userprofile = get_object_or_404(UserProfile, user=user)
    # print(userprofile)
    
    context = {
        'products': products,
        'categories':category,
        'banner': banner,
        'userprofile':userprofile,
    }
    
    return render(request, 'Home_page/index.html', context )

def errorpage(request):
    return (request,'Home_page/404.html')