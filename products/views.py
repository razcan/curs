from django.http import HttpResponse
from django.shortcuts import render
from .models import Supplier, Item


def products_list(request):
    return render(request, 'product_list.html')


def product_detail(request):
    return render(request, 'product_detail.html')