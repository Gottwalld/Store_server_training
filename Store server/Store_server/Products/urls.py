from django.urls import path
from Products.views import products

app_name = 'Products'

urlpatterns = [
    
    path('', products, name='index')
]
