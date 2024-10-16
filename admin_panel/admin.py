from django.contrib import admin
from .models import Product  # Import the Product model

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'rating')  # Fields to display in the admin list view
    search_fields = ('name',)  # Searchable fields in the admin list view

admin.site.register(Product, ProductAdmin)  # Register the Product model with the admin site
