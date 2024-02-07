from rest_framework import serializers
from .models import Products


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    category = serializers.CharField(max_length=50)
    title = serializers.CharField(max_length=30)
    price = serializers.IntegerField()
    discount = serializers.IntegerField()
    size = serializers.CharField(max_length=20)
    color = serializers.CharField(max_length=30)


# class ProductAddSerializer(serializers.Serializer):
#     id = serializers.IntegerField(required=False)
#     title = serializers.CharField(max_length=30)
#     price = serializers.IntegerField()
#     discount = serializers.IntegerField()
#
#     def create(self, validated_data):
#         return Products.objects.create(**validated_data)

class ProductAddSerializer(serializers.ModelSerializer):
    discount = serializers.IntegerField(write_only=True)

    class Meta:
        model = Products
        fields = ('id', 'title', 'price', 'discount')
        read_only_fields = ['discount']


