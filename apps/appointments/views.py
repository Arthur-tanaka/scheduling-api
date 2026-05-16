from rest_framework import generics
from .serializers import AppointmentSerializer
from apps.appointments.models import Appointment
from apps.appointments.tasks import send_confirmation_email


class AppointmentListView(generics.ListCreateAPIView):
    serializer_class = AppointmentSerializer
    
    def get_queryset(self):
        user = self.request.user
        return Appointment.objects.filter(user=user)
    
    def perform_create(self, serializer):
        appointment = serializer.save(user=self.request.user)
        send_confirmation_email.delay(appointment.id)
        
class AppointmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AppointmentSerializer
    
    def get_queryset(self):
        user = self.request.user
        return Appointment.objects.filter(user=user)