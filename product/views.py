from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Count
from rest_framework import status
from product.models import Product,Category,Review
from product.serializers import ProductSerializer,CategorySerializer,ReviewSerializer
from rest_framework.views import APIView
from rest_framework.mixins import CreateModelMixin,ListModelMixin
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from product.filters import ProductFilter
from rest_framework.filters import SearchFilter,OrderingFilter
from product.pagination import DefaultPagination

class ProductViewSet(ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    filter_backends=[DjangoFilterBackend,SearchFilter, OrderingFilter]
    filterset_class=ProductFilter
    pagination_class=DefaultPagination
    search_fields=['name','description']
    ordering_fields=['name','updated_at']

    def destroy(self,request,*args,**kwargs):
        product=self.get_object()
        if product.stock>10:
            return Response({'message':'Product with more than 10 stock could not be deleted'})
        self.perform_destroy(product)
        return Response(status=status.HTTP_204_NO_CONTENT)

class CategoryViewSet(ModelViewSet):
    queryset=Category.objects.annotate(product_count=Count('products')).all()
    serializer_class=CategorySerializer

class ReviewViewSet(ModelViewSet):
    serializer_class=ReviewSerializer

    def get_queryset(self):
        return Review.objects.filter(product_id=self.kwargs['product_pk'])

    def get_serializer_context(self, *args, **kwargs):
        return {'product_id':self.kwargs['product_pk']}




