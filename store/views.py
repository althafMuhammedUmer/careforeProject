from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Product, ProductGallery, WishList, HomeBanner
from category.models import Category
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from Grocery.models import CartItem
from django.db.models import Q
import requests 


def testweather(request):
    
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=dfb3784a3e5dd64ae687bcd5f165a29f'
    city = 'KANNUR'
    city_weather = requests.get(url.format(city)).json()
    weather = {
        'city' : city,
        'temperature' : city_weather['main']['temp'],
        'description' : city_weather['weather'][0]['description'],
        'icon' : city_weather['weather'][0]['icon']
    }
    context = {
        'weather':weather,
    }
    return render(request, 'Home_page/testweather.html', context)

@login_required(login_url='login')
def addwishlist(request, id):
    if request.user.is_authenticated:
        
    
        product = Product.objects.get(id=id)
        product_id = request.GET.get('id')
        
        if WishList.objects.filter(user=request.user.id,product_id=product):
            messages.success(request, 'already added')
            return redirect('/')
        else:
            newwishlish = WishList.objects.create(user=request.user, product=product)
            newwishlish.save()
            messages.success(request, 'wishlist added successfully')
        
        
            return redirect('home')
    
        



def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
       
            product = Product.objects.filter(
                Q(product_name__icontains=keyword) | 
                Q(description__icontains = keyword) |
                Q(Category__category_name__icontains = keyword) |
                Q(subcategorys__subcategory_name__icontains = keyword)
                                             )
         
    context = {
        'products':product
    } 
    
    return render(request,'Home_page/shop-grid.html', context) 

def store(request, category_slug=None):
    category = None
    products = None
    
    categories = Category.objects.all()
    if category_slug != None:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(Category=category, is_available=True)
        product_count = products.count()
    else:
        
        products = Product.objects.filter(is_available=True)
        
        
        product_count = products.count()
    
    context = {
        'products': products,
        'categories':categories,
        'product_count':product_count,
    }
    return render(request, 'Home_page/shop-grid.html', context)


def product_details(request, slug):
    product = Product.objects.get(slug=slug)
    product_gallery = ProductGallery.objects.filter(product__slug=product.slug)
    print(product_gallery)
    
    
    categories = Category.objects.all()
    context = {
        'categories':categories,
        'product':product,
        'product_gallery':product_gallery,
    }
    return render(request, 'Home_page/product.html', context)

# @login_required(login_url='login')
# def addwishlist(request):
#     if request.method == "POST":
#         if request.user.is_authenticated:
#             prod_id = request.POST.get('product_id')
            
#             product_check = Product.objects.get(id=prod_id)
#             if product_check:
#                 if WishList.objects.filter(user=request.user.id, product_id = prod_id):
                    
#                     return JsonResponse({'status': "already added"})
                
#                 else:
#                     WishList.objects.create(user=request.user, product_id = prod_id)
#                     return JsonResponse({'status': "added to wishlist"})
#             else:
#                 return JsonResponse({'status': "no such products found"})
        
#         else:
#             # messages.success(request, 'please login')
#             return JsonResponse({'status': "login to continue"})
        
#     return render('/')
        
                    
            
    
   
@login_required(login_url='login')
def viewWishlist(request,):
    if request.user.is_authenticated:
        
        
    
        wishlist = WishList.objects.filter(user=request.user.id)
        
        context = {
            'wishlist':wishlist,
        }
        return render(request, 'Home_page/wishlist.html', context)
    else:
        messages.success(request, 'login to continue')
        return render('login')

@login_required(login_url='login')
def deletewishlist(request, product_id):
    if request.user.is_authenticated:
        
        product = Product.objects.get(id=product_id)
        wishlist = WishList.objects.get(product_id =product, user=request.user)
        wishlist.delete()
        messages.success(request, 'deleted successfully')
        
        return redirect('wishlist')
    
def pagenotfound(request,exception):
    return render (request, 'Home_page/404.html')

def homebanner(request):
    banner = HomeBanner.objects.all()
    context = {
        'banner':banner,
    }
    return render(request, 'Home_page/index.html', context)
    
    
    
