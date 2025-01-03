from django.db import models

from chat.models import Expert

class Podcast(models.Model):
   id = models.AutoField(primary_key=True)
   name = models.CharField(max_length=200)
   img = models.TextField(null=True, blank=True)
   description = models.TextField(null=True, blank=True)
   duration = models.IntegerField(default=0)
   expert = models.ForeignKey(Expert, on_delete=models.CASCADE, related_name='podcasts')
   
   def __str__(self):
      return self.name