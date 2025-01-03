from rest_framework import serializers
from .models import Expert
from study.models import Course
from video.models import Video
      
class ExpertSerializer(serializers.ModelSerializer):
   courses = serializers.SerializerMethodField()
   def get_courses(self, obj):
      return [course.name for course in obj.courses.all()]
   
   videos = serializers.SerializerMethodField()
   def get_videos(self, obj):
      return [video.caption for video in obj.videos.all()]
   
   podcasts = serializers.SerializerMethodField()
   def get_podcasts(self, obj):
      return [podcast.name for podcast in obj.podcasts.all()]

   class Meta:
      model = Expert
      fields = '__all__'