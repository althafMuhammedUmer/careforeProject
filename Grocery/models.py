

from django.db import models

from store.models import Product,ProductAttribute
from Accounts.models import Account


# Create your models here.
class Cart(models.Model):
    
    user   = models.ForeignKey(Account, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(ProductAttribute, on_delete=models.CASCADE, blank=True)
    product_qty = models.IntegerField()
  
    # cart_id = models.CharField(max_length=250, blank=True, unique=True)
    created_at = models.DateField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    
    
    # def __str__(self):
    #     return self.product.product_name
    
    
# class CartItem(models.Model):
#     user   = models.ForeignKey(Account, on_delete=models.CASCADE, null=True, blank=True)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     # product_attribute = models.ForeignKey(ProductAttribute, on_delete=models.CASCADE,blank=True)
    
#     Cart    = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)
#     is_active = models.BooleanField(default=True)
    
#     def sub_total(self):
#         return self.product.price * self.quantity
    
#     def __unicode__(self): # from py3 onwards we use __unicode__ instead of __str__
#         return self.product
    

    
    
     
    
    
    
    

    
