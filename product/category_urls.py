from django.urls import path,include
from product import views

urlpatterns=[
    path('',views.CategoryList.as_view(),name='category'),
    path('<int:id>/',views.ViewSpecificCategory.as_view(),name='view-specific-category'),
]