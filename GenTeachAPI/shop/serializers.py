from .models import Product, Category
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
   products = serializers.SerializerMethodField()
   def get_products(self, obj):
      return [product.name for product in obj.products.all()]

   class Meta:
      model = Category
      fields = '__all__'
      
class ProductSerializer(serializers.ModelSerializer):
   category_name = serializers.CharField(source='category.name', read_only=True)

   class Meta:
      model = Product
      fields = '__all__'