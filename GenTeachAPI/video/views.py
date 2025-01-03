from oauth2_provider.contrib.rest_framework.authentication import OAuth2Authentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet

from .models import Video

from .serializers import VideoSerializer

class VideoViewSet(ModelViewSet):
   authentication_classes = [OAuth2Authentication]
   permission_classes = [IsAuthenticated]
   
   queryset = Video.objects.all()
   serializer_class = VideoSerializer
   
   def get_permissions(self):
      if self.action in ['list', 'retrieve']:
         return [AllowAny()]
      if self.action in ['create', 'update', 'partial_update', 'destroy']:
         return [IsAuthenticated()]
      return super().get_permissions()