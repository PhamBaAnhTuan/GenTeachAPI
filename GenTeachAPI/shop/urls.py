from django.urls import path, include
from shop.views import ProductViewSet, CategoryViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'category', CategoryViewSet, basename='category')
router.register(r'product', ProductViewSet, basename='product')

urlpatterns = [
   path('', include(router.urls))
]
