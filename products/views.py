import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from .models import Products
from .serializers import ProductSerializer, ProductAddSerializer

URL = "https://api.api-ninjas.com/v1/cryptoprice?symbol="


class TestApi(APIView):
    def post(self, request):
        users = User.objects.all()

        username = [user.username for user in users]

        return Response(username)


class ProductApi(APIView):
    def post(self, request):
        product = Products.objects.all()
        serializer = ProductSerializer(instance=product, many=True)
        return Response(data=serializer.data)


class ProductDitailApi(APIView):
    def get(self, request, pk):
        product = Products.objects.get(id=pk)
        serializer = ProductSerializer(instance=product)
        return Response(data=serializer.data)


class ProductAddApi(APIView):
    def post(self, request):
        serializer = ProductAddSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "added"})
        return Response(serializer.errors)


class ProductUpdateApi(APIView):
    def put(self, request, pk):
        queryset = Products.objects.get(id=pk)
        serializer = ProductAddSerializer(data=request.data, instance=queryset, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "update"})
        return Response(serializer.errors)


# ...............................................
# other example for update with API
# class ProductUpdateApi(APIView):
#     def put(self, request, pk):
#         queryset = Products.objects.get(id=pk)
#         serializer = ProductAddSerializer(data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.update(instance=queryset, validated_data=serializer.validated_data)
#             return Response({"message": "update"})
#         return Response(serializer.errors)

class ProductDeleteApi(APIView):
    def delete(self, request, pk):
        queryset = Products.objects.get(id=pk)
        queryset.delete()
        return Response({"message": "delete"})

# class ProductName(APIView):
#     def get(self, request):
#         lists = []
#         product_name = request.GET.get("product_name")
#         product_list = lists.append(product_name)
#         product_loop = [pro["product_name"] for pro in product_name]
#         return Response({"message": f"product {product_list}"})


# class GetCryptoPrice(APIView):
#     def get(self, request):
#         crypto = request.GET.get('crypto')
#         crypto_response = requests.get(f"https://api.nobitex.ir/market/stats")
#         data = crypto_response.json()
#         result = {
#             "symbol": data['symbol'],
#
#         }
#         return Response(data)
