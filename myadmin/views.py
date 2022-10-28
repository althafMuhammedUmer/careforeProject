

from operator import index
from unicodedata import category, name
from urllib import request
from django.shortcuts import render,redirect,get_list_or_404
from django.contrib import messages,auth
# from django.contrib.auth.admin import UserAdmin
# from django.contrib.messages.views import SuccessMessageMixin


from Accounts.models import Account
from store.models import Product
from django.contrib.auth.decorators import login_required
from category.models import Category, SubCategory
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from .forms import ProductForm
from orders.models import Order, OrderItem
import datetime
from datetime import datetime as date

import time
import requests




# Create your views here.





def ordercompleted(request, id):
    if request.user.is_superadmin:
        
        order = Order.objects.get(id=id)
        order.status = 'Completed'
        order.save()
        
        return redirect('view_orders')
    else:
        return redirect('/')
    
def orderpending(request, id):
    if request.user.is_superadmin:
        order = Order.objects.get(id=id)
        order.status = 'Pending'
        order.save()
        return redirect('view_orders')
    else:
        return redirect('/')
    
def ordershipping(request, id):
    if request.user.is_superadmin:
        order = Order.objects.get(id=id)
        order.status = 'Out for shipping'
        order.save()
        return redirect('view_orders')
    else:
        return redirect('/')
    
def ordercancel(request, id):
    if request.user.is_superadmin:
        order = Order.objects.get(id=id)
        order.status = 'Cancelled'
        order.save()
        return redirect('view_orders')
    else:
        return redirect('/')
    
    



def viewSingleOrder(request, id):
    orders = Order.objects.filter(id=id).order_by('-created_at')
    context = {
        'orders':orders,
    }
    
    return render(request, 'myadmin2/viewSingleOrder.html',context)
    
    


@login_required(login_url = 'login')
def view_orders(request):
    ordercounter= Order.objects.all()
    order_count = ordercounter.count()
    orders = Order.objects.all().order_by('-created_at')
    context = {
        'orders':orders,
        'order_count':order_count,
    }
    
    return render(request, 'myadmin2/order_view.html', context)

# def myadmin(request):
#     if request.user.is_superadmin:
       
#         admin = request.user
    
#         return render(request, 'myadmin/myadminhome.html', { 'admin':admin })
#     else:
#         return redirect('index')
@login_required(login_url='login')
def myadmin2(request):
    if request.user.is_superadmin:
        current_date = datetime.datetime.now()
        month = current_date.strftime("%B")
        day = date.today().strftime("%A")
        current_time = time.strftime("%H:%M:%S", time.localtime())
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=dfb3784a3e5dd64ae687bcd5f165a29f'
        city = 'calicut'
        city_weather = requests.get(url.format(city)).json()
        weather = {
            'city' : city,
            'temperature' : city_weather['main']['temp'],
            'description' : city_weather['weather'][0]['description'],
            'icon' : city_weather['weather'][0]['icon']
        }
        
        orders = Order.objects.all()
        orders_count = orders.count()
        products = Product.objects.filter(is_available=True)
        product_count = products.count()
        sales = Order.objects.filter(status='Completed')
        sales_count = sales.count()
        
        
        # order_products = OrderItem.objects.all()
        # order_product_dict = {}
        # for order_product in order_products:
        #     if order_product.product.product_name in order_product_dict:
        #         quantity = order_product_dict[order_product.product.product_name]
        #         quantity += order_product.quantity
        #         order_product_dict[order_product.product.product_name] = quantity
        #     else:
        #         order_product_dict[order_product.product.product_name]=order_product.quantity

        # sorted_order_product_dict = dict(sorted(order_product_dict.items(), key=lambda item: item[1], reverse=True))

        # sorted_products_by_sales = list(sorted_order_product_dict.keys())
        # sorted_product_quantity_by_sales = list(sorted_order_product_dict.values())
        
        
        user = Account.objects.filter(is_superadmin=False)
        user_total = user.count() 
       
        
        admin = request.user
        context = {
            'user_total':user_total,
            'admin':admin,
            'current_date':current_date,
            'current_time':current_time,
            'day':day,
            'month':month,
            'weather':weather,
            'orders':orders,
            'orders_count':orders_count,
            'product_count':product_count,
            'sales_count':sales_count,
            
            # 'sorted_product_quantity_by_sales':sorted_product_quantity_by_sales,
            # 'sorted_products_by_sales':sorted_products_by_sales,
            
        
        }
        return render(request,'myadmin2/index.html', context) 
    else:
        return redirect(index)

@login_required(login_url='login')
def myadminlogout(request):
    auth.logout(request)
    # messages.success(request, 'You are logged out')
    return redirect('home')

@login_required(login_url = 'login')
def userdata(request):
    if request.user.is_superadmin:
        admin = request.user
        search_key = request.GET.get(
            'key') if request.GET.get('key') != None else ''
        
        user = Account.objects.filter(is_superadmin=False)
        return render(request, 'myadmin2/userdata.html',{'users':user, 'admin': admin})
    else:
        return redirect('/')

@login_required(login_url = 'login')
def user_delete(request,id):
    if request.user.is_superadmin:
        userid = Account.objects.get(pk=id)
        userid.delete()
        return redirect('userdata')
    else:
        return render(request,'/')


    
@login_required(login_url='login')   
def product_delete(request,id):
    if request.user.is_superadmin:
        productid = Product.objects.get(pk=id)
        productid.delete()
        return redirect('product_details')

# def productAdd(request):
#     product_name =
#     product = Product.objects.create('')      

@login_required(login_url='login')
def product_details(request):
    if request.user.is_superadmin:
        admin = request.user
        product = Product.objects.all()
         
        return render(request, 'myadmin2/apps-e-commerce-products.html',{'products':product, 'admin':admin })  

@login_required(login_url = 'login')
def add_product(request):
    form = ProductForm()
    
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_details')
    context = {
        'form':form
    }
    
    return render(request, 'myadmin2/addproduct.html', context) 

@login_required(login_url = 'login')  
def update_product(request,pk):
    product = Product.objects.get(id=pk)
    form    = ProductForm(instance=product)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_details')
    context = {
        "form" : form
    }
    return render(request, 'myadmin2/update_product.html',context)

@login_required(login_url = 'login')
def delete_product(request,pk):
    product = Product.objects.get(id=pk)
    product.delete()
    return redirect('product_details')

        

class CategoryListView(ListView):
    model = Category
  
    # success_message = "Category added successfully"
    template_name = "myadmin2/category_list.html"



class CategoryCreate(CreateView):
    model = Category
    fields = "__all__"
    template_name = "myadmin2/category_create.html"



class CategoryUpdate(UpdateView):
    model = Category
    # fields = ["category_name", "slug", "description", "category_image"]
    fields = "__all__"
    
    template_name = "myadmin2/category_update.html"
    
@login_required(login_url = 'login')
def category_delete(request, pk):
    category = Category.objects.get(id=pk)
    category.delete()
    return redirect('category_list')