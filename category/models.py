
from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=255) 
    category_image = models.ImageField(upload_to = 'photos/categories', blank=True)
    entered_date = models.DateField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        
    def get_absolute_url(self):
        return reverse("category_list")
    
    
    def __str__(self):
        return self.category_name
    
    
class SubCategory(models.Model):
    subcategory_name=models.CharField(max_length=300,unique=True)
    slug=models.SlugField(max_length=300,unique=True)
    enter_date=models.DateTimeField(auto_now_add=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE, null=True, blank=True)
    Subcategory_image = models.ImageField(upload_to = 'photos/categories',null=True, blank=True)
    
    
    class Meta:
        verbose_name = 'SubCategory'
        verbose_name_plural = 'SubCategories'
    def __str__(self):
        return self.subcategory_name     

    
# class Items(models.Model):
#     item_name = models.CharField(max_length=300, unique=True)
#     slug = models.SlugField(max_length=300, unique=True)
#     item_img = models.ImageField(upload_to= 'images/category', blank=True)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     class Meta:
#         verbose_name = 'item'
#         verbose_name_plural = 'items'
#     def __str__(self):
#         return self.item_name
    
    
    
    

    
