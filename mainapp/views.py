from django.shortcuts import render
from django.core.paginator import Paginator

from mainapp.models import Product, ProductCategory


# функции = вьюхи = контроллеры
def index(request):
    context = {'title': 'GeekShop'}
    return render(request, 'mainapp/index.html', context)


def products(request, category_id=None, page=1):
    context = {'title': 'GeekShop - Каталог', 'categories': ProductCategory.objects.all()}
    if category_id:
        products = Product.objects.filter(category_id=category_id).order_by('-price')
    else:
        products = Product.objects.all().order_by('-price')
    paginator = Paginator(products, 3)
    products_paginator = paginator.page(page)
    context.update({'products': products_paginator})
    return render(request, 'mainapp/products.html', context)
