from django.urls import path

from basketapp.views import basket_add, basket_delete

app_name = 'basketapp'

urlpatterns = [
    path('basket-add/<int:product_id>/', basket_add, name='basket_add'),
    path('basket-delete/<int:id>/', basket_delete, name='basket_delete'),
]
