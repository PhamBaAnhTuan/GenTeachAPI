
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny

from oauth2_provider.contrib.rest_framework.authentication import OAuth2Authentication

from .models import Expert
from .serializers import ExpertSerializer

class ExpertViewSet(viewsets.ModelViewSet):
   authentication_classes = [OAuth2Authentication]
   permission_classes = [IsAuthenticated]
   
   queryset = Expert.objects.all()
   serializer_class = ExpertSerializer
   
   def get_permissions(self):
      if self.action in ['list','retrieve']:
         return [AllowAny()]
      if self.action in ['create', 'update', 'partial_update', 'destroy']:
         return [IsAuthenticated()]
      return super().get_permissions()