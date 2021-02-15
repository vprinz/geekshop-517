from django.shortcuts import render


# функции = вьюхи = контроллеры
def index(request):
    return render(request, 'mainapp/index.html')


def products(request):
    return render(request, 'mainapp/products.html')
