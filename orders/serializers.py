from .models import Order
from rest_framework import serializers

class OrderSerializer(serializers.ModelSerializer):

    order_status = serializers.HiddenField(default='PENDING')

    class Meta:
        model = Order
        fields = ['size', 'order_status', 'quantity']

