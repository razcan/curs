from django.http import HttpResponse
from django.shortcuts import render
from .models import Supplier, Item
from django.http import JsonResponse

def products_list(request):
    results = Item.objects.all()
    return render(request, 'product_list.html',{'results': results})


def product_detail(request, id):
    try:
        product = Item.objects.get(id=id)
        data = {"product": {
                    "name": product.name,
                    "description": product.description,
                    "image": product.image.url,
                    "price": product.price,
                    "code": product.code,
                    "category": product.category,   
                    "supplier": product.supplier.name               
                }}
        response = JsonResponse(data)
    except Product.DoesNotExist:
        response = JsonResponse({
            "error": {
                "code": 404,
                "message": "product not found!"
            }},
            status=404)
    return response