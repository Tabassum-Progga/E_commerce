from django.shortcuts import render
from .models import *

# Create your views here.

def products(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, template_name='ProductsManagement/Products.html',context=context)


def orders(request):
    orders = Order.objects.all()
    context = {
        'orders': orders
    }
    return render(request, template_name='ProductsManagement/Order.html',context=context)