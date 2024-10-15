from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

urlpatterns = [
    path('products/', ProductViewSet.as_view(), name='product-list'),  
    path('products/start_parsing/', ProductViewSet.as_view(), name='product-parse'),
]
