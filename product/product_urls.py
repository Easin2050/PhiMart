from django.urls import path,include
from product import views

urlpatterns=[
    path('',views.ProductList.as_view(),name='product-lsit'),
    path('<int:id>',views.ProductDetails.as_view(),name='product-list')
]