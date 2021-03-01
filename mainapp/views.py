import os
import json

from django.shortcuts import render

from mainapp.models import Product, ProductCategory

dir = os.path.dirname(__file__)


# функции = вьюхи = контроллеры
def index(request):
    context = {'title': 'GeekShop'}
    return render(request, 'mainapp/index.html', context)


def products(request, id=None):
    context = {
        'title': 'GeekShop - Каталог',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'mainapp/products.html', context)
