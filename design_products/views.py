from django.shortcuts import render
from django.http import HttpResponse
from design_products.models import DesignProduct, DesignCategory

def index(request, cat_id):
    if cat_id == None:
        cat = DesignCategory.objects.first()
    else:
        cat = DesignCategory.objects.get(pk=cat_id)
    products = DesignProduct.objects.filter(category=cat).order_by("name")
    s = 'Категория: {} <br><br>'.format(cat.name)
    for product in products:
        s = s + '( {} ) {} <br>'.format(product.pk, product.name)
    return HttpResponse(s)
# Create your views here.

