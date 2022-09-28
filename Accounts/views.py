from itertools import product
from django.http import HttpResponse
from django.shortcuts import render,redirect
# from . import verify
from .verify import send_otp, verify_otp
from django.contrib.auth import authenticate,login,logout

from .forms import RegistrationForm
from .models import Account
from django.contrib import messages,auth
from django.contrib.auth.decorators import login_required
# from Grocery.views import _cart_id
# from Grocery.models import Cart, CartItem

#verification email
# from django.contrib.sites.shortcuts import get_current_site
# from django.template.loader import render_to_string
# from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
# from django.utils.encoding import force_bytes
# from django.contrib.auth.tokens import default_token_generator
# from django.core.mail import EmailMessage
# from Accounts.mixins import *

# testing view
# def test(request):
#     return render(request, 'Home_page/test.html')


# # def profile(request):
# #     if request.method == 'POST':
# #         name = request.POST['name']
# #         email = request.POST['email']
# #         bio = request.POST['bio']
# #         new_profile = Profile(name=name, email=email, bio=bio)
# #         new_profile.save()
# #         success = 'User ' + name + ' is created sucessfully'
# #         return HttpResponse(success)
        
    



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
            
               
        

   

def loginpage(request):
    if request.user.is_authenticated:
        messages.warning(request, 'you are already logged in ')
        
        
    if request.method == "POST":
        
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        # user = auth.authenticate(email=email, password=password)
        
        if user is not None:
            login(request, user)
          
            # auth.login(request,user)
            messages.success(request, 'you are now logged in')
            if request.user.is_superadmin:
                return redirect('myadmin2')
            else:
                return redirect('dashboard')
        
        else:
            messages.error(request, 'Invalid login credentials')
            return redirect('login')
    return render(request,'accounts/login.html')

@login_required(login_url = 'login')
def logoutpage(request):
    logout(request)
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
        


@login_required(login_url='login')
def dashboard(request):
    return render(request, 'accounts/userdashboard.html')



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