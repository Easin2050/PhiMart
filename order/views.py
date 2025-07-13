from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.mixins import CreateModelMixin,DestroyModelMixin,RetrieveModelMixin
from order.models import Cart,CartItem
from order.serializer import CartSerializer,CartItemSerializer,AddCartItemSerializer
# Create your views here.

class CartViewSet(CreateModelMixin,RetrieveModelMixin,DestroyModelMixin,GenericViewSet):
    queryset=Cart.objects.all()
    serializer_class=CartSerializer

class CartItemViewSet(ModelViewSet):
    serializer_class=CartItemSerializer

    def get_serializer(self):
        if self.request.method=='POST':
            return AddCartItemSerializer()
        return CartItemSerializer

    def get_serializer_context(self):
        return{'cart_id': self.kwarsgs['cart_pk']}

    def get_queryset(self):
        return CartItem.objects.filter(cart_id=self.kwargs['cart_pk'])


