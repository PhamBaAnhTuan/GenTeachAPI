from django.db import models

from chat.models import Expert

class Video(models.Model):
   id = models.AutoField(primary_key=True)
   url = models.TextField(blank=True, null=True)
   caption = models.TextField(blank=True, null=True)
   expert = models.ForeignKey(Expert, on_delete=models.CASCADE, related_name='videos')
   like = models.IntegerField(null=True, blank=True)
   comment = models.IntegerField(null=True, blank=True)
   share = models.IntegerField(null=True, blank=True)
   
   def __str__(self):
      return self