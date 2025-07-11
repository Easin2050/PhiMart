from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.mixins import CreateModelMixin,DestroyModelMixin,RetrieveModelMixin
from order.models import Cart,CartItem
from order.serializer import CartSerializer,CartItemSerializer
# Create your views here.

class CartViewSet(CreateModelMixin,RetrieveModelMixin,DestroyModelMixin,GenericViewSet):
    queryset=Cart.objects.all()
    serializer_class=CartSerializer

class CartItemViewSet(ModelViewSet):
    serializer_class=CartItemSerializer

    def get_queryset(self):
        return CartItem.objects.filter(cart_id=self.kwargs['cart_pk'])


