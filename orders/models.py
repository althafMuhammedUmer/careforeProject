from django.db import models
from Accounts.models import Account
from store.models import Product

# Create your models here.

    
class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for shipping', 'Out for shipping'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    )
    #   ORDER_STATUS = (
    #     ('Accepted', 'Accepted'),
    #     ('Ready to ship', 'Ready to ship'),
    #     ('On shipping', 'On shipping'),
    #     ('Delivered', 'Delivered'),
    #     ('Cancelled', 'Cancelled'),
    #     ('return', 'return'),
    #     ('Refunded', 'Refunded'),
    # )
    

    user = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    # payment = models.ForeignKey(Payment, on_delete=models.SET_NULL, blank=True, null=True)
    order_number = models.CharField(max_length=20)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    payment_method = models.CharField(max_length=50,null=True, blank=True)
    address_line_1 = models.CharField(max_length=100)
    address_line_2 = models.CharField(max_length=100,  blank=True)
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    order_note = models.TextField(blank=True, null=True)
    total_price = models.FloatField()
    payment_id = models.CharField(max_length=250, null=True, blank=True)
    post_code = models.IntegerField(null=True)
    
    # product_total = models.FloatField(null=True ,blank=True)
    
    # tax = models.FloatField() 
    status = models.CharField(max_length=50, choices=STATUS, default='Pending')
    # ip = models.CharField(blank=True, max_length=20)
    is_ordered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    tracking_no = models.CharField(max_length=150, null=True)
    # order_status = models.CharField(max_length=50, choices=ORDER_STATUS, default='Accepted')
    
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    def __str__(self):
        return '{} - {}'.format(self.id, self.tracking_no)
    
   
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField(null=False)
    quantity = models.IntegerField(null=False)
    
    def __str__(self):
        return '{} {}' .format(self.order.id, self.order.tracking_no)

class Profile(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    phone = models.CharField(max_length=50, null=False)
    address = models.TextField(null=False)
    city = models.CharField(max_length=150, null=False)
    country = models.CharField(max_length=200)
    post_code = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username
    
    
