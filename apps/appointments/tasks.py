from django.conf import settings
from celery import shared_task
from django.core.mail import send_mail
from apps.appointments.models import Appointment

@shared_task
def send_confirmation_email(appointment_id):
    appointment = Appointment.objects.get(id=appointment_id)
    
    subject = f'Confirmação de agendamento, cliente{appointment.user.name}'
    message = f'Olá, {appointment.user.name} seu serviço agendado é: {appointment.service.name} as {appointment.appointment_date}'
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [appointment.user.email]
    
    send_mail(subject, message, from_email, recipient_list)