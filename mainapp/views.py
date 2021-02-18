from django.shortcuts import render


# функции = вьюхи = контроллеры
def index(request):
    a = 1
    return render(request, 'mainapp/index.html')


def products(request):
    return render(request, 'mainapp/products.html')
