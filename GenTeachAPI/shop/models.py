from django.db import models
from django.utils import timezone

from user.models import User

class Category(models.Model):
   id = models.AutoField(primary_key=True)
   name = models.CharField(max_length=100)
   img = models.TextField(null=True, blank=True)
   
   def __str__(self):
      return self.name
     
class Product(models.Model):
   id = models.AutoField(primary_key=True)
   name = models.CharField(max_length=100)
   brand = models.CharField(max_length=100)
   img = models.TextField(null=True, blank=True)
   price = models.IntegerField(default=0)
   discount = models.IntegerField(default=0)
   free_ship = models.BooleanField(default=True)
   rate = models.IntegerField(default=0)
   description = models.TextField(null=True, blank=True)
   category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
   
   def __str__(self):
      return self
   
# class Cart(models.Model):
#    id = models.AutoField(primary_key=True)
#    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='carts')
#    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='carts')
#    quantity = models.IntegerField(default=1)
#    created_at = models.DateTimeField(default=timezone.now)
   
#    def __str__(self):
#       return self

class Meta:
   ordering = ['-created_at']
   indexes = [
   models.Index(fields=['created_at'])
]