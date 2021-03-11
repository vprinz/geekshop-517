from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from authapp.models import User
from adminapp.forms import UserAdminRegistrationForm


def index(request):
    return render(request, 'adminapp/index.html')


# READ
def admin_users(request):
    context = {'users': User.objects.all()}
    return render(request, 'adminapp/admin-users-read.html', context)


# CREATE
def admin_users_create(request):
    if request.method == 'POST':
        form = UserAdminRegistrationForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin_staff:admin_users'))
    else:
        form = UserAdminRegistrationForm()
    context = {'form': form}
    return render(request, 'adminapp/admin-users-create.html', context)


# UPDATE
def admin_users_update(request):
    return render(request, 'adminapp/admin-users-update-delete.html')


# DELETE
def admin_users_delete(request):
    pass
