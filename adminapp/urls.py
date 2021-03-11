from django.urls import path

from adminapp.views import index, admin_users, admin_users_create, admin_users_update, admin_users_delete

app_name = 'adminapp'

urlpatterns = [
    path('', index, name='index'),
    path('users/', admin_users, name='admin_users'),
    path('users-create/', admin_users_create, name='admin_users_create'),
    path('users-update/<int:user_id>/', admin_users_update, name='admin_users_update'),
    path('users-delete/<int:user_id>/', admin_users_delete, name='admin_users_delete'),
]
