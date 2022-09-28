from tkinter import CASCADE
from django.db import models
from store.models import ProductAttribute, Product
from Accounts.models import Account

# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    product_attribute = models.ForeignKey(ProductAttribute, on_delete=models.CASCADE)
    product_qty  = models.FloatField(null=False, blank=False)
    created_at   =models.DateTimeField(auto_now_add=True)
    
