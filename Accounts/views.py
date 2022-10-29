
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render,redirect
# from . import verify
from .verify import send_otp, verify_otp


from .forms import RegistrationForm, UserForm, UserProfileForm
from .models import Account, UserProfile
from django.contrib import messages,auth
from django.contrib.auth.decorators import login_required

from Grocery.models import  CartItem
from orders.models import Order, OrderItem
#verification email
# from django.contrib.sites.shortcuts import get_current_site
# from django.template.loader import render_to_string
# from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
# from django.utils.encoding import force_bytes
# from django.contrib.auth.tokens import default_token_generator
# from django.core.mail import EmailMessage
# from Accounts.mixins import *





# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email      = request.POST['email']
            phone_number     = request.POST['phone_number']
            password   = request.POST['password']
            
            
            request.session['first_name'] = first_name
            request.session['last_name'] = last_name
            request.session['username'] = username
            
            request.session['email'] = email
            request.session['phone_number'] = phone_number
            request.session['password'] = password
            
            
            send_otp(phone_number)
            return redirect('verify_code')
        else:
            messages.error(request, "You are already registered ")
        
    form = RegistrationForm() 
    
    context = {
        'form':form,
    }
    return render(request,'accounts/register.html', context)
            
            # #user Activation
            # if request.POST == 'email':
                
            #     current_site = get_current_site(request)
            #     mail_subject = 'please activate your Account'
            #     message = render_to_string('accounts/account_verification_email.html', {
            #         'user':user,
            #         'domain': current_site,
            #         'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            #         'token': default_token_generator.make_token(user),
            #     })
            #     to_email = email
            #     send_email = EmailMessage(mail_subject, message, to=[to_email])
            #     send_email.send() 
            # messages.success(request, 'Registration successful. Please check your email to verify your account')
                # return redirect('/accounts/login/?command=verification&email='+email)
            
               
        

   

def login(request):
    if request.method == "POST":
        
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email=email, password=password)
        
        if user is not None:
            
           
            auth.login(request,user)
            messages.success(request, 'you are now logged in')
            if request.user.is_superadmin:
                return redirect('myadmin2')
            else:
                return redirect('home')
        
        else:
            messages.error(request, 'Invalid login credentials')
            return redirect('login')
    return render(request,'accounts/login.html')

@login_required(login_url = 'login')
def logout(request):
    auth.logout(request)
    messages.success(request,'You are logged out')
    return redirect('login')


# def activate(request, uidb64, token):
#     try:
#         uid = urlsafe_base64_decode(uidb64).decode()
#         user = Account._default_manager.get(pk=uid)
#     except(TypeError, ValueError, OverflowError, Account.DoesNotExist):
#         user = None
#     if user is not None and default_token_generator.check_token(user,token):
#         user.is_active = True
#         user.save()
#         messages.success(request, 'congratulations! Your account is activated. ')
#         return redirect('login')
#     else:
#         messages.error(request, 'Invalid Activation link')
#         return redirect('register')
        
#### user dashboard ###

@login_required(login_url='login')
def dashboard(request):
    
    userprofile, _ = UserProfile.objects.get_or_create(user_id=request.user.id)
    
    order= Order.objects.order_by('-created_at').filter(user_id = request.user.id, is_ordered=True)
    order_count = order.count()
    context={
        'order_count':order_count,
        'userprofile':userprofile,
        
       
    }
    
    return render(request, 'accounts/dashboard.html', context)

@login_required(login_url='login')
def my_orders(request):
    # orders= Order.objects.order_by('-created_at').filter(user_id = request.user.id, is_ordered=True)
    
    orders = Order.objects.filter(user=request.user, is_ordered=True).order_by('-created_at')
    context = {
        'orders':orders,
    }
    return render(request, 'accounts/myorders.html', context)

@login_required(login_url='login')
def edit_profile(request):
    userprofile = get_object_or_404(UserProfile, user=request.user)
    if request.method == "POST":
        user_form  = UserForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "your profile has been updated")
            return redirect('edit_profile')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = UserProfileForm(instance=userprofile)
    
    context = {
        
        'user_form':user_form,
        'profile_form':profile_form,
        'userprofile':userprofile,
        
    }
        
    return render(request, 'accounts/edit_profile.html', context)


@login_required(login_url='login')
def change_password(request):
    if request.method == "POST":
        current_password = request.POST['current_password']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']
        
        user = Account.objects.get(username__exact=request.user.username) # exact is checking username exactly present , iexact is without case sensitive
        
        if new_password == confirm_password:
            success = user.check_password(current_password)
            if success:
                user.set_password(new_password)
                user.save()
                messages.success(request , "password updated successfully")
                # auth.logout(request)
                return redirect('change_password')
            else:
                messages.error(request, "please enter valid current password")
                return redirect('change_password')
        else:
            messages.error(request, "password doesnot match")
            return redirect('change_password')
        
        
        
    return render(request, 'accounts/changepassword.html')

@login_required(login_url='login')
def order_detail(request,id):
    order_detail = OrderItem.objects.filter(order_id=id)
    order = Order.objects.get(id=id)
    print(order_detail)
    context = {
        'order_detail': order_detail,
        'order':order,
    }
    return render(request, 'accounts/user_order_detail.html', context)


### user dashboard ends ###


def verify_code(request):
    if request.method == 'POST':
        otp_check = request.POST.get('otp')
        phone_number=request.session['phone_number']
        
        verify= verify_otp(phone_number,otp_check)
        
        if verify:
            messages.success(request,'account has created successfuly please login now') 
            
            
            first_name = request.session['first_name']
            last_name  = request.session['last_name']
            email      = request.session['email']
            username   = request.session['username']
            
            phone_number = request.session['phone_number']
            password =   request.session['password']
            
            
            
            user = Account.objects.create_user(
                username = username,
                first_name = first_name,
                last_name = last_name,
                email  = email,
                phone_number = phone_number,
                password = password,
                  
            )
            
            user.is_verified = True
            
            user.save()
            messages.success(request, 'Registration successful')
            return redirect('login')
        else:
            messages.error(request, 'Invalid otp recheck')
            return redirect ('verify_code')
        
    return render(request, 'accounts/verify.html')