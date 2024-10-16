from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),  # This maps the homepage to the index view
    path('products.html',views.products,name='products'),
    path('account.html',views.account,name='account'),
    path('cart.html',views.cart,name='cart'),
    path('products-details.html',views.productsDetails,name='products Details'),
    path('products/', views.all_products, name='all_products'), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)