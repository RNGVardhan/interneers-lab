# views.py

# from django.shortcuts import render
from rest_framework import filters, status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product
from .serializers import ProductSerializer

products = []

# To view all the products in the database
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    filter_backends = [filters.OrderingFilter]
    ordering_fields = ["name", "description", "category", "price", "brand", "quality", "imported_date", "sold_date"]
    ordering = ["-imported_date"]       # default

# To view all the in-memory products
class ProductList(APIView):
    def get(self, request):
        return Response(products)

# To view one product
class ProductDetail(APIView):
    def get(self, request):
        searched_name = request.query_params.get("q", "").strip().lower()
        if searched_name:
            for product in products:
                if product["name"].strip().lower() == searched_name:
                    return Response(product, status.HTTP_200_OK)
            return Response("No such product in the inventory.", status.HTTP_204_NO_CONTENT)
        return Response("No parameters provided. Please search with ?q=", status.HTTP_400_BAD_REQUEST)

# To create a new product
class ProductCreate(APIView):
    def post(self, request):
        # queryset = Product.objects.all()

        data = request.data

        required_fields = {"name", "description", "price"}

        absent_fields = required_fields - set(data.keys())
        if len(absent_fields) > 0:
            return Response(f"Error: fields [{", ".join(absent_fields)}] need to be provided.", status.HTTP_400_BAD_REQUEST)

        products.append(data)
        return Response("Product created successfully!", status.HTTP_201_CREATED)
