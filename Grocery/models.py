

from django.db import models

from store.models import Product
from Accounts.models import Account


# Create your models here.
class Cart(models.Model):
    
    user   = models.ForeignKey(Account, on_delete=models.CASCADE, null=True, blank=True)
    
    cart_id = models.CharField(max_length=250, blank=True, unique=True)
    date_added = models.DateField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.cart_id
    
    
class CartItem(models.Model):
    user   = models.ForeignKey(Account, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    # Cart    = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)
    
    def sub_total(self):
        return self.product.price * self.quantity
    
    def __unicode__(self): # from py3 onwards we use __unicode__ instead of __str__
        return self.product
    

    
    
     
    
    
    
    

    
