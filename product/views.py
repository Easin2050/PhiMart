from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from product.models import Product,Category
from product.serializers import ProductSerializer
# Create your views here.

@api_view()
def view_specific_products(request,id):
        product=get_object_or_404(Product,pk=id)
        # product_dict={"id": product.id,"name":product.name,"unit_price":product.price}
        serializer=ProductSerializer(product)
        return Response(serializer.data)

    
@api_view()
def view_category(response):
    return Response({"message":"Cateogory View"})