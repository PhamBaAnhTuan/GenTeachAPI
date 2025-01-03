from rest_framework import serializers
from .models import Video

from chat.models import Expert

class VideoSerializer(serializers.ModelSerializer):
   expert_name = serializers.CharField(source='expert.name', read_only=True)
   expert_img = serializers.CharField(source='expert.img', read_only=True)
   
   class Meta:
      model = Video
      fields = '__all__'