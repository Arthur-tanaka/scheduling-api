from rest_framework import serializers
from apps.appointments.models import Appointment

class AppointmentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Appointment
        fields = ['id', 'user', 'service', 'appointment_date', 'created_at', 'status']
        read_only_fields = ['user','created_at']

