from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Count
from rest_framework import status
from product.models import Product,Category
from product.serializers import ProductSerializer,CategorySerializer
from rest_framework.views import APIView

'''@api_view(['GET', 'POST']) 
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
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)'''

class ViewProduct(APIView):
    def get(self,request):
        products = Product.objects.select_related('category').all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = ProductSerializer(data=request.data)  # Deserializer
        if serializer.is_valid():
            print(serializer.validated_data)
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

'''@api_view(['GET', 'PUT', 'DELETE'])
def view_specific_products(request, id):
    if request.method == 'GET':
        product = get_object_or_404(Product, pk=id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    if request.method == 'PUT':
        product = get_object_or_404(Product, pk=id)
        serializer = ProductSerializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    if request.method == 'DELETE':
        product = get_object_or_404(Product, pk=id)
        copy_of_product=product
        product.delete()
        serializer=ProductSerializer(copy_of_product)
        return Response(serializer.data,status=status.HTTP_204_NO_CONTENT)'''

class ViewSpecificProduct(APIView):
    def get(self,request,id):
        product = get_object_or_404(Product, pk=id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    def put(self,request):
        product = get_object_or_404(Product, pk=id)
        serializer = ProductSerializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    def delete(self,request,id):
        product = get_object_or_404(Product, pk=id)
        copy_of_product=product
        product.delete()
        serializer=ProductSerializer(copy_of_product)
        return Response(serializer.data,status=status.HTTP_204_NO_CONTENT)

'''@api_view(['GET','POST'])
def view_categories(request):
    if request.method=='GET':
        categories=Category.objects.annotate(product_count=Count('products')).all()
        serializer=CategorySerializer(categories,many=True)
        return Response(serializer.data)
    
    if request.method=='POST':
        serializer=CategorySerializer(data=request.data)
        #  if serializer.is_valid():
        serializer.is_valid(raise_exception=True)       
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
        #  else:
        #       return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)'''
class ViewCategory(APIView):
    def get(self,request):
        categories=Category.objects.annotate(product_count=Count('products')).all()
        serializer=CategorySerializer(categories,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)       
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)

'''@api_view()
def view_specific_category(request,pk):
        category=get_object_or_404(Category,pk=pk)
        serializer=CategorySerializer(category)
        return Response(serializer.data)'''

class ViewSpecificCategory(APIView):
    def get(self,request,id):
        category=get_object_or_404(Category,pk=id)
        serializer=CategorySerializer(category)
        return Response(serializer.data)
    
    def put(self,request,id):
        category=get_object_or_404(Category,pk=id)
        serializer=CategorySerializer(category,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self,request,id):
        category=get_object_or_404(Category,pk=id)
        copy_of_category=category
        category.delete()
        serializer=CategorySerializer(copy_of_category)
        return Response(serializer.data,status=status.HTTP_204_NO_CONTENT)
    

