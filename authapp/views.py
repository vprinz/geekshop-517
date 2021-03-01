from django.shortcuts import render


def login(request):
    return render(request, 'authapp/login.html')


def register(request):
    return render(request, 'authapp/register.html')
