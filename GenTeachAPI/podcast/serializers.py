from rest_framework import serializers

from .models import Podcast

from chat.models import Expert

class PodcastSerializer(serializers.ModelSerializer):
   expert_name = serializers.CharField(source='expert.name', read_only=True)
   
   class Meta:
      model = Podcast
      fields = '__all__'