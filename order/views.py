from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import *
from .models import *
from django.http import HttpResponse
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView
# Create your views here.

class OrderViewSet(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class Order_detail(RetrieveAPIView):
    lookup_field = 'id'
    queryset = Order.objects.all()
    serializer_class = Order_detailSerializer


class Order_Update(UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class Order_delete(DestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class Order_create(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer