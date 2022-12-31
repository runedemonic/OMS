from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class Order_detailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'