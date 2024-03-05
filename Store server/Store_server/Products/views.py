from django.shortcuts import render, HttpResponse

from Products.models import Product_Category, Product

def index(request):
    context = {
        'title':'Title`s store',
        'user_name':'qwerty',
        'promo': True,
    }
    
    return render(request, 'Product\index.html', context)

def products(request):
    context = {
        'title':'Store - Каталог товаров',
        'user_name':'qwerty',
        'products_item': Product.objects.all(),
        'category' : Product_Category.objects.all(), 
    }
    return render(request, 'Product\products.html', context)
