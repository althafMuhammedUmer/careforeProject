from django.db import models
from django.utils.safestring import mark_safe
from category.models import *
from Accounts.models import *


# Create your models here.
class Banner(models.Model):
    image = models.ImageField(upload_to = 'photos/banner')
    text  = models.CharField(max_length=300)
    
    def image_tag(self):
        return mark_safe('<img src="%s" width="100"  /> '% (self.image.url))
    
    def __str__(self):
        return self.text
    
    
    
    



class Product(models.Model):
    product_name    = models.CharField(max_length=200, unique=True)
    slug            = models.SlugField(max_length=200, unique=True)
    description     = models.TextField(max_length=2500, blank=True)
    # price           = models.FloatField()
    product_discount_price = models.CharField(max_length=200, null=True, blank=True)
    stock        = models.IntegerField()
    is_available    = models.BooleanField(default=True) #status
    Category        = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    subcategorys     =models.ForeignKey(SubCategory,on_delete=models.CASCADE , null=True, blank=True)
    brand            =models.ForeignKey(Brand, on_delete=models.CASCADE,null=True, blank=True)
    is_featured    = models.BooleanField(default=False)
    # color            =models.ForeignKey(Color,on_delete=models.CASCADE,null=True, blank=True)
    # storage          =models.ForeignKey(Storage, on_delete=models.CASCADE , null=True,blank=True)
    
    # quantity        =models.IntegerField()
    
    # items           = models.ForeignKey(Items, on_delete=models.CASCADE)
    created_date    = models.DateTimeField(auto_now_add=True)
    modified_date   = models.DateTimeField(auto_now=True)
    
    
    # def image_tag(self):
    #     return mark_safe('<img src="%s" width="60"   /> '% (self.images.url))
    
    
   
    
    def __str__(self):
        return self.product_name


    
    
class ProductAttribute(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image   = models.ImageField(upload_to = 'photos/products',null=True)
    
    color   = models.ForeignKey(Color, on_delete=models.CASCADE,null=True)
    storage = models.ForeignKey(Storage, on_delete=models.CASCADE,null=True)
    price   = models.PositiveIntegerField()
    quantity =models.IntegerField()
    
    
    class Meta:
        verbose_name_plural='7. ProductAttributes'
        
    def image_tag(self):
        return mark_safe('<img src="%s" width="60"/> '% (self.image.url))
    
    
    
    
    def __str__(self):
        return self.product.product_name
    

# class ProductMedia(models.Model):
#     product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
#     media_type_choice =((1,"image"),(2,"video"))
#     media_type = models.CharField(max_length=255)   
#     title_details = models.CharField(max_length=255)
 
    
    

    
# class Product_Reviews(models.Model):
#     product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
#     user_id  = models.ForeignKey(Account,on_delete=models.CASCADE)
#     rating = models.CharField(default="5",max_length=255)
#     review = models.TextField(default="")
#     created_date = models.DateField(auto_now_add=True)
#     is_active = models.IntegerField(default=1)
    
    
# class ProductReviewVoting(models.Model):
#     product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
#     user_id_voting = models.ForeignKey(Account,on_delete=models.CASCADE)
#     created_date    = models.DateTimeField(auto_now_add=True)
#     modified_date   = models.DateTimeField(auto_now=True)


# class ProductVarient(models.Model):
#     title = models.CharField(max_length=255)
#     created_date    = models.DateTimeField(auto_now_add=True)
    

# class ProductVarientItems(models.Model):
#     product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
#     product_varient_id = models.ForeignKey(ProductVarient,on_delete=models.CASCADE)
#     title = models.CharField(max_length=255)
#     created_date    = models.DateTimeField(auto_now_add=True)
   

# class CustomerOrders(models.Model):
#     product_id = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
#     purchase_price = models.CharField(max_length=255)
#     coupon_code = models.CharField(max_length=255)
#     discount_amount = models.CharField(max_length=255)
#     product_status = models.CharField(max_length=255)
#     created_date    = models.DateTimeField(auto_now_add=True)

# class OrderDeliveryStatus(models.Model):
#     order_id = models.ForeignKey(CustomerOrders, on_delete=models.CASCADE)
#     status = models.CharField(max_length=255)
#     status_message = models.CharField(max_length=255)
#     created_date    = models.DateTimeField(auto_now_add=True)
#     modified_date   = models.DateTimeField(auto_now=True)
    
# class ProductTransaction(models.Model): 
#     product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
#     transaction_type_choices = ((1,"Buy"), (2,"Sell"))
#     transaction_product_count = models.IntegerField(  default=1)
#     transaction_type = models.IntegerField(choices=transaction_type_choices)
#     transaction_description = models.TextField(max_length=300)
#     created_date    = models.DateTimeField(auto_now_add=True)
    
    
    
    
     

    
    
    
    
        