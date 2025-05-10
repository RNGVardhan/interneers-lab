# views.py

# from django.shortcuts import render
from rest_framework import filters, status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product
from .serializers import ProductSerializer

# To view all the products
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    filter_backends = [filters.OrderingFilter]
    ordering_fields = ["name", "description", "category", "price", "brand", "quality", "imported_date", "sold_date"]
    ordering = ["-imported_date"]       # default

# To view one product
class ProductDetail(APIView):
    def get(self, request):
        queryset = Product.objects.all()

# To create a new product
class ProductCreate(APIView):
    def post(self, request):
        data = request.data

        required_fields = {"name", "description", "category", "price", "brand", "quality", "imported_date", "sold_date"}

        absent_fields = set(data.keys()) - required_fields
        if len(absent_fields) > 0:
            return Response(f"Error: fields [{", ".join(absent_fields)}] need to be provided.", status.HTTP_400_BAD_REQUEST)
