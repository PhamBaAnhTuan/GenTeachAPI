from rest_framework import serializers
from .models import Course, Topic
from chat.models import Expert

class CourseSerializer(serializers.ModelSerializer):
   topic_name = serializers.CharField(source='topic.name', read_only=True)
   expert_name = serializers.CharField(source='expert.name', read_only=True)
   expert_img = serializers.CharField(source='expert.img', read_only=True)

   class Meta:
      model = Course
      fields = '__all__'
      
class TopicSerializer(serializers.ModelSerializer):
   courses = serializers.SerializerMethodField()
   def get_courses(self, obj):
      return [course.name for course in obj.courses.all()]
   
   class Meta:
      model = Topic
      fields = '__all__'
      