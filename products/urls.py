from django.urls import path

from . import views

urlpatterns = [
    path('product_detail', views.product_detail, name='product_detail'),
    path('products_list', views.products_list, name='products_list'),
]