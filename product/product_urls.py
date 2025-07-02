from django.urls import path,include
from product import views

urlpatterns=[
    path('',views.view_products,name='product-lsit'),
    path('<int:id>',views.view_specific_products,name='product-list')
]