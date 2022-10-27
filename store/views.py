from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from .models import Product, ProductGallery, WishList, HomeBanner
from category.models import Category
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from Grocery.models import CartItem
from django.db.models import Q


def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
       
            product = Product.objects.filter(Q(product_name__icontains=keyword) | Q(description__icontains = keyword))
         
    context = {
        'products':product
    } 
    
    return render(request,'Home_page/shop-grid.html', context) 

def store(request):
    products = Product.objects.filter(is_available=True)
    category = Category.objects.all()
    
    product_count = products.count()
    
    context = {
        'products': products,
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
        'category':category,
        'product':product,
        'product_gallery':product_gallery,
    }
    return render(request, 'Home_page/product.html', context)

@login_required(login_url='login')
def addwishlist(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            prod_id = request.POST.get('product_id')
            
            product_check = Product.objects.get(id=prod_id)
            if product_check:
                if WishList.objects.filter(user=request.user.id, product_id = prod_id):
                    
                    return JsonResponse({'status': "already added"})
                
                else:
                    WishList.objects.create(user=request.user, product_id = prod_id)
                    return JsonResponse({'status': "added to wishlist"})
            else:
                return JsonResponse({'status': "no such products found"})
        
        else:
            # messages.success(request, 'please login')
            return JsonResponse({'status': "login to continue"})
        
    return render('/')
        
                    
            
    
   
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
    
    
    
