from django.db import models
from category.models import *
from Accounts.models import *


# Create your models here.



class Product(models.Model):
    product_name    = models.CharField(max_length=200, unique=True)
    slug            = models.SlugField(max_length=200, unique=True)
    description     = models.TextField(max_length=2500, blank=True)
    price           = models.FloatField()
    product_discount_price = models.CharField(max_length=200, null=True, blank=True)
    images          = models.ImageField(upload_to = 'photos/products', null=True, blank=True)
    stock        = models.IntegerField()
    is_available    = models.BooleanField(default=True)
    Category        = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    subcategorys=models.ForeignKey(SubCategory,on_delete=models.CASCADE , null=True, blank=True)
    # quantity        =models.IntegerField()
    
    # items           = models.ForeignKey(Items, on_delete=models.CASCADE)
    created_date    = models.DateTimeField(auto_now_add=True)
    modified_date   = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.product_name

class ProductGallery(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'photos/products/productgallery')
    
    def __str__(self):
        return self.product.product_name
    
    class Meta:
        verbose_name = 'productgallery'
        verbose_name_plural = 'productgallery'
        
class WishList(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    
    
     

    
    
    
    
        