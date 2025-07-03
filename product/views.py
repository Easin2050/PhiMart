from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Count
from rest_framework import status
from product.models import Product,Category
from product.serializers import ProductSerializer,CategorySerializer
# Create your views here.

@api_view(['GET', 'POST']) 
def view_products(request):
    if request.method == 'GET':
        products = Product.objects.select_related('category').all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)  # Deserializer
        if serializer.is_valid():
            print(serializer.validated_data)
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view()
def view_specific_products(request,id):
        product=get_object_or_404(Product,pk=id)
        # product_dict={"id": product.id,"name":product.name,"unit_price":product.price}
        serializer=ProductSerializer(product)
        return Response(serializer.data)

    
@api_view(['GET','POST'])
def view_categories(request):
    if request.method=='GET':
        categories=Category.objects.annotate(product_count=Count('products')).all()
        serializer=CategorySerializer(categories,many=True)
        return Response(serializer.data)
    
    if request.method=='POST':
         serializer=CategorySerializer(data=request.data)
         if serializer.is_valid():
              print(serializer.validated_data)
              serializer.save()
              return Response(serializer.data,status=status.HTTP_201_CREATED)
         else:
              return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)

@api_view()
def view_specific_category(request,pk):
        category=get_object_or_404(Category,pk=pk)
        serializer=CategorySerializer(category)
        return Response(serializer.data)