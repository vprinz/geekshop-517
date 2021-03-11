from django.shortcuts import render

from authapp.models import User


def index(request):
    return render(request, 'adminapp/index.html')


# READ
def admin_users(request):
    context = {'users': User.objects.all()}
    return render(request, 'adminapp/admin-users-read.html', context)


# CREATE
def admin_users_create(request):
    return render(request, 'adminapp/admin-users-create.html')


# UPDATE
def admin_users_update(request):
    return render(request, 'adminapp/admin-users-update-delete.html')


# DELETE
def admin_users_delete(request):
    pass
