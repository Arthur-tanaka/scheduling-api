from apps.services.models import Service
from rest_framework import generics
from .serializers import ServiceSerializer


class ServiceListView(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    
class ServiceDetailView(generics.RetrieveAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    