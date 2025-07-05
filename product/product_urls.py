from django.urls import path,include
from product import views

urlpatterns=[
    path('',views.ViewProduct.as_view(),name='product-lsit'),
    path('<int:id>',views.ViewSpecificProduct.as_view(),name='product-list')
]