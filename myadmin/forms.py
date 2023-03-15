
from email.policy import default
from django import forms
from store.models import Product
from category.models import Category, SubCategory


cat_choices = Category.objects.all().values_list('category_name', 'category_name')
sub_cat_choices = SubCategory.objects.all().values_list('subcategory_name', 'subcategory_name')

cat_choices_list = []

for item in cat_choices:
    cat_choices_list.append(item)
    
    
sub_cat_choices_list = []
for item in sub_cat_choices:
    sub_cat_choices_list.append(item)



class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["product_name",
                 "slug",
                 "description",
                 "price",
                 "product_discount_price",
                 "images",
                 "stock",
                 "Category",
                 "subcategorys",
                
                 ]
        widgets = {
            'product_name': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'product_discount_price': forms.TextInput(attrs={'class': 'form-control'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
            'Category': forms.Select(choices=cat_choices_list , attrs={'class': 'form-control'}),
            'subcategorys': forms.Select(choices=sub_cat_choices_list,  attrs={'class': 'form-control'}),
            
            
          
            
        }