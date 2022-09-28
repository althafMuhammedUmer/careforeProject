from tkinter import CASCADE
from django.db import models
from store.models import ProductAttribute, Product
from Accounts.models import Account

# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(Account, on_delete=CASCADE)
    
