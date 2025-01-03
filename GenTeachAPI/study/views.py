from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny

from oauth2_provider.contrib.rest_framework.permissions import OAuth2Authentication

from .models import Topic, Course
from .serializers import CourseSerializer, TopicSerializer

class TopicViewSet(viewsets.ModelViewSet):
   authentication_classes = [OAuth2Authentication]
   permission_classes = [IsAuthenticated]
   
   queryset = Topic.objects.all()
   serializer_class = TopicSerializer
   
   def get_permissions(self):
      if self.action in ['list', 'retrieve']:
         return [AllowAny()]
      if self.action in ['create', 'update', 'partial_update', 'destroy']:
         return [IsAuthenticated()]
      return super().get_permissions()
   
class CourseViewSet(viewsets.ModelViewSet):
   authentication_classes = [OAuth2Authentication]
   permission_classes = [IsAuthenticated]
   
   queryset = Course.objects.all()
   serializer_class = CourseSerializer
   
   def get_permissions(self):
      if self.action in ['list', 'retrieve']:
         return [AllowAny()]
      if self.action in ['create', 'update', 'partial_update', 'destroy']:
         return [IsAuthenticated()]
      return super().get_permissions()