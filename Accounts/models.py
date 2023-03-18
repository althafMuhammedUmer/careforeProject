from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# from django.contrib.auth.models import PermissionsMixin
# Create your models here.

class MyAccountManager(BaseUserManager):
    def create_user(self,username,first_name,last_name,phone_number, email, password=None):
        if not email:
            raise ValueError('User must have an email address')
        
        if not phone_number:
            raise ValueError('user must have a phone number')
        
        
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            
            first_name = first_name,
            last_name = last_name,
            phone_number = phone_number
            
            
        )
        
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, username,phone_number,  password,first_name,last_name):
        user = self.create_user(
            first_name= first_name,
            last_name= last_name,
            email = self.normalize_email(email),
            phone_number=phone_number,
            username = username,
            password = password,
              
            
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        
        user.save(using = self._db)
        
        return user
    
        
        
        




class Account(AbstractBaseUser):
    first_name      = models.CharField(max_length=50)
    last_name       = models.CharField(max_length=50)
    username        = models.CharField(max_length=50, unique=True)
    email           = models.EmailField(max_length=250, unique=True )
    phone_number    = models.CharField(max_length=14, null=True)
    
    
    
    
    #required field
    
    date_joined     = models.DateTimeField(auto_now_add=True)
    last_login      = models.DateTimeField(auto_now_add=True)
    is_admin        = models.BooleanField(default=False)
    is_staff        = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=True)
    is_superadmin   = models.BooleanField(default=False)
    is_verified     = models.BooleanField(default=False)
    # otp_verified    = models.BooleanField(default=False)
    
    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [ 'username','first_name', 'last_name', 'phone_number']
    
    objects = MyAccountManager()
    
    def __str__(self):
        return self.email
    
    
    # mandatory functions
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, add_label):
        return True

class UserProfile(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    address_line_1 = models.CharField( max_length=200, null=True, blank=True)
    address_line_2 = models.CharField(blank=True, max_length=200)
    profile_picture = models.ImageField(blank=True, upload_to='UserProfile')
    city = models.CharField(blank=True, max_length=25)
    state = models.CharField(blank=True, max_length=25)
    country = models.CharField(blank=True, max_length=25)
    
    def __str__(self):
        return self.user.username
    
    def full_address(self):
        return f'{self.address_line_1} {self.address_line_2}'
    
    def username(self):
        return self.user.username
    
    
    
    
    
    
    
    
    
    
    

