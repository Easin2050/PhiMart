from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin,RetrieveModelMixin
from order.models import Cart
from order.serializer import CartSerializer
# Create your views here.

class CartViewSet(CreateModelMixin,RetrieveModelMixin,GenericViewSet):
    queryset=Cart.objects.all()
    serializer_class=CartSerializer

