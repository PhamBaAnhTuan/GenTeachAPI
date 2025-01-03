from django.db import models

class Expert(models.Model):
   id = models.AutoField(primary_key=True)
   name = models.CharField(max_length=100)
   img = models.TextField(null=True, blank=True)
   rate = models.IntegerField(default=0)
   is_online = models.BooleanField(default=False)
   follower = models.IntegerField(default=0)
   
   def __str__(self):
      return self.name