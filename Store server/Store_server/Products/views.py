from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, 'Product\index.html')

def products(request):
    return render(request, 'Product\products.html')
