from rest_framework import serializers
from .models import Product, ProductOption, ProductMedia, ProductSelling, ProductComposition, ProductSize, ProductColor, ProductCertificate

class ProductParseSerializer(serializers.Serializer):
    nm_id = serializers.IntegerField(required=True, help_text="Артикул товара Wildberries")

class ProductOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOption
        fields = '__all__'

class ProductMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductMedia
        fields = '__all__'

class ProductSellingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSelling
        fields = '__all__'

class ProductCompositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductComposition
        fields = '__all__'

class ProductSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSize
        fields = '__all__'

class ProductColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductColor
        fields = '__all__'

class ProductCertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCertificate
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    options = ProductOptionSerializer(many=True, read_only=True)
    media = ProductMediaSerializer(many=True, read_only=True)
    selling_info = ProductSellingSerializer(many=True, read_only=True)
    compositions = ProductCompositionSerializer(many=True, read_only=True)
    sizes = ProductSizeSerializer(many=True, read_only=True)
    colors = ProductColorSerializer(many=True, read_only=True)
    certificates = ProductCertificateSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'
