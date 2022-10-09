

from django.db import models

from store.models import Product
from Accounts.models import Account


# Create your models here.

    
    
class CartItem(models.Model):
    user   = models.ForeignKey(Account, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    # Cart    = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField( null=True, blank=True)
    created_at =models.DateTimeField(auto_now_add=True) 
    is_active = models.BooleanField(default=True)
    
    completed = models.BooleanField(default=False, blank=True)
    
    def sub_total(self):
        return self.product.price * self.quantity
    
    def __unicode__(self): # from py3 onwards we use __unicode__ instead of __str__
        return self.product
    

    

    
    
     
    
    
    
    

    
