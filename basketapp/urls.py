from django.urls import path

from basketapp.views import basket_add

app_name = 'authapp'

urlpatterns = [
    path('basket-add/<int:product_id>/', basket_add, name='basket_add'),
]
