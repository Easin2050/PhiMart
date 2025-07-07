from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Count
from rest_framework import status
from product.models import Product,Category
from product.serializers import ProductSerializer,CategorySerializer
from rest_framework.views import APIView
from rest_framework.mixins import CreateModelMixin,ListModelMixin
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView

'''class ViewProduct(APIView):
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
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)'''

class ProductList(ListCreateAPIView):
    queryset=Product.objects.select_related('category').all()
    serializer_class=ProductSerializer
    
    '''def get_queryset(self):
        return Product.objects.select_related('category').all()

    def get_serializer_class(self):
        return ProductSerializer'''

    # it method will be used when there is a logical work is there
    
    '''def get_serializer(self):
        return {'request':self.request}'''

class ProductDetails(RetrieveUpdateDestroyAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    lookup_field='id'
    
'''class ViewCategory(APIView):
    def get(self,request):
        categories=Category.objects.annotate(product_count=Count('products')).all()
        serializer=CategorySerializer(categories,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)       
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)'''

class CategoryList(ListCreateAPIView):
    queryset=Category.objects.annotate(product_count=Count('products')).all()
    serializer_class=CategorySerializer

class CategoryDetails(RetrieveUpdateDestroyAPIView):
    queryset=Category.objects.annotate(product_count=Count('products')).all()
    serializer_class=CategorySerializer
    lookup_field='id'

'''class ViewSpecificCategory(APIView):
    def get(self,request,id):
        category=get_object_or_404(Category.objects.annotate(product_count=Count('products')),pk=id)
        serializer=CategorySerializer(category)
        return Response(serializer.data)
    
    def put(self,request,id):
        category=get_object_or_404(Category.objects.annotate(product_count=Count('products')),pk=id)
        serializer=CategorySerializer(category,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self,request,id):
        category=get_object_or_404(Category.objects.annotate(product_count=Count('products')),pk=id)
        copy_of_category=category
        category.delete()
        serializer=CategorySerializer(copy_of_category)
        return Response(serializer.data,status=status.HTTP_204_NO_CONTENT)
    

'''