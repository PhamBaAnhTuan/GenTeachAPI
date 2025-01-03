from django.db import models
from chat.models import Expert

class Topic(models.Model):
   id = models.AutoField(primary_key=True)
   name = models.CharField(max_length=100)
   
   def __str__(self):
      return self

class Course(models.Model):
   id = models.AutoField(primary_key=True)
   name = models.CharField(max_length=100)
   expert = models.ForeignKey(Expert, on_delete=models.CASCADE, related_name='courses')
   topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='courses')
   img = models.TextField(null=True, blank=True)
   price = models.IntegerField(default=0)
   discount = models.IntegerField(default=0)
   is_free = models.BooleanField(default=True)
   rate = models.IntegerField(default=5)
   description = models.TextField(null=True, blank=True)
   progress = models.IntegerField(default=0)
   
   def __str__(self):
      return self