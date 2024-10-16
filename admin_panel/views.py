from django.shortcuts import render
from .models import Product

def index(request):
    return render(request, 'admin_panel/index.html')
    

def products(request):
    return render(request, 'admin_panel/products.html')

def account(request):
    return render(request, 'admin_panel/account.html')

def cart(request):
    return render(request, 'admin_panel/cart.html')

def productsDetails(request):
    return render(request, 'admin_panel/products-details.html')

def all_products(request):
    products = Product.objects.all()  # Fetch all products from the database
    return render(request, 'products.html', {'products': products})