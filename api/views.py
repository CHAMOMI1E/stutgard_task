from rest_framework import status
from .models import ParseWB, Product
from .serializers import ProductParseSerializer, ProductSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action
from celery import shared_task

class ProductViewSet(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['post'])
    def post(self, request, format=None):
        serializer = ProductParseSerializer(data=request.data)
        if serializer.is_valid():
            nm_id = serializer.validated_data['nm_id']
            parse_product_task.delay(nm_id)
            return Response({"status": "Task started"}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@shared_task
def parse_product_task(nm_id):
    ParseWB(nm_id).parse()