from django.shortcuts import render
from .models import Product, Category

from .serializers import ProductSerializer, CategorySerializer

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny

from oauth2_provider.contrib.rest_framework.authentication import OAuth2Authentication

class CategoryViewSet(viewsets.ModelViewSet):
   authentication_classes = [OAuth2Authentication]
   permission_classes = [AllowAny]
   
   queryset = Category.objects.all()
   serializer_class = CategorySerializer
   
   def get_permissions(self):
      if self.action in ['list', 'retrieve']:
         return [AllowAny()]
      if self.action in ['create', 'update', 'partial_update', 'destroy']:
         return [IsAuthenticated()]
      return super().get_permissions()

class ProductViewSet(viewsets.ModelViewSet):
   authentication_classes = [OAuth2Authentication]
   permission_classes = [AllowAny]
   
   queryset = Product.objects.all()
   serializer_class = ProductSerializer
   
   def get_permissions(self):
      if self.action in ['list', 'retrieve']:
         return [AllowAny()]
      if self.action in ['create', 'update', 'partial_update', 'destroy']:
         return [IsAuthenticated()]
      return super().get_permissions()