

from django import forms
from store.models import Product




class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["product_name",
                 "slug",
                 "description",
                #  "price",
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
            # 'price': forms.TextInput(attrs={'class': 'form-control'}),
            'product_discount_price': forms.TextInput(attrs={'class': 'form-control'}),
          
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
            'Category': forms.Select(attrs={'class': 'form-control'}),
            'subcategorys': forms.Select(attrs={'class': 'form-control'}),
            
            
          
            
        }