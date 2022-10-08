

from email import message
from filecmp import clear_cache
from functools import cache
from multiprocessing import context
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




# Create your views here.

# def myadmin(request):
#     if request.user.is_superadmin:
       
#         admin = request.user
    
#         return render(request, 'myadmin/myadminhome.html', { 'admin':admin })
#     else:
#         return redirect('index')
@login_required(login_url='login')
def myadmin2(request):
    if request.user.is_superadmin:
        admin = request.user
        return render(request,'myadmin2/index.html', {'admin':admin}) 
    else:
        return redirect(index)

@login_required(login_url='login')
def myadminlogout(request):
    auth.logout(request)
    # messages.success(request, 'You are logged out')
    return redirect('index')

def userdata(request):
    if request.user.is_superadmin:
        admin = request.user
        search_key = request.GET.get(
            'key') if request.GET.get('key') != None else ''
        
        user = Account.objects.filter(is_superadmin=False)
        return render(request, 'myadmin2/userdata.html',{'users':user, 'admin': admin})
    else:
        return redirect('/')


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
def product_details2(request):
    if request.user.is_superadmin:
        admin = request.user
        product = Product.objects.all()
         
        return render(request, 'myadmin2/apps-e-commerce-products.html',{'products':product, 'admin':admin })  

def add_product(request):
    form = ProductForm()
    
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_details2')
    context = {
        'form':form
    }
    
    return render(request, 'myadmin2/addproduct.html', context)   
def update_product(request,pk):
    product = Product.objects.get(id=pk)
    form    = ProductForm(instance=product)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_details2')
    context = {
        "form" : form
    }
    return render(request, 'myadmin2/update_product.html',context)

def delete_product(request,pk):
    product = Product.objects.get(id=pk)
    product.delete()
    return redirect('product_details2')

        

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
    

def category_delete(request, pk):
    category = Category.objects.get(id=pk)
    category.delete()
    return redirect('category_list')