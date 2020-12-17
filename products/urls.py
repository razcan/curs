from django.urls import path

from . import views

urlpatterns = [
    path('product_detail/<int:id>', views.product_detail, name='product_detail'),
    path('supplier_detail/<int:id>', views.supplier_detail, name='supplier_detail'),
    path('supplier_list', views.supplier_list, name='supplier_list'),
    path('products_list', views.products_list, name='products_list'),
]