from rest_framework import serializers
from .models import *


class ProductWithImageSerializer(serializers.ModelSerializer):

    image = serializers.ImageField(max_length=None, use_url=True)
    
    class Meta:
        model = Product
        #fields = ['id' , 'namee' , 'price' , 'image']
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id' , 'namee', 'price']


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class AddImageProSerializer(serializers.ModelSerializer):

    serializers.ImageField(max_length=None, use_url=True)
    
    class Meta:
        model = Product
        fields = ['image']