# from .models import Product,ProductAttribute


# def get_filters(request):
#     cats = Product.objects.distinct().values('Category__category_name', 'Category__id')
#     colors = ProductAttribute.objects().values('Color__title', 'Color__id', 'Color__color_code')
#     storages  = ProductAttribute.objects().values('Storage__title', 'Storage__id')
    
#     data ={
#         'cats':cats,
#         'colors':colors,
#         'storages':storages
        
#     }
#     return data