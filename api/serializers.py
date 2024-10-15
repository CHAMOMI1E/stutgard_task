from rest_framework import serializers
from .models import Product

class ProductParseSerializer(serializers.Serializer):
    nm_id = serializers.IntegerField(required=True, help_text="Артикул товара Wildberries")


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__' 
